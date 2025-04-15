from pydantic import BaseModel, Field, ValidationError
from typing import List
import streamlit as st
from docx import Document
import pdfplumber
import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from CustomDocxBoilerv1 import generate_docx

 
# Define the Pydantic model for structured output
class Resume(BaseModel):
    name: str = Field(..., description="The name of the candidate")
    email: str = Field(..., description="The email address of the candidate")
    phone: str = Field(..., description="The phone number of the candidate")
    skills: List[str] = Field(..., description="A list of skills possessed by the candidate")
    experience: List[str] = Field(..., description="A list of work experiences of the candidate")
    education: List[str] = Field(..., description="A list of educational qualifications of the candidate")
 
# Define the prompt template for resume parsing
prompt_template = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    Extract the following information from the resume:
    - Name
    - Email
    - Phone
    - Skills
    - Experience
    - Education
 
    Provide the output in JSON format with the following keys:
    - name
    - email
    - phone
    - skills
    - experience
    - education
 
    Resume text:
    {resume_text}
    """
)
 
# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)
 
# Create the LLM chain for resume parsing
resume_parser_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
)
 
# Streamlit application to upload resume and parse it
st.title("Resume Parser")
 
uploaded_file = st.file_uploader("Upload your resume", type=["txt", "pdf", "docx"])
 
if uploaded_file is not None:
    try:
        with st.spinner("Processing resume..."):
            # Read the uploaded file content
            if uploaded_file.type == "text/plain":
                resume_text = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/pdf":
                # pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                # resume_text = ""
                # for page_num in range(pdf_document.page_count):
                #     page = pdf_document.load_page(page_num)
                #     resume_text += page.get_text()
                    # Read the PDF file using pdfplumber
                    with pdfplumber.open(uploaded_file) as pdf:
                        resume_text = ""
                        for page in pdf.pages:
                            resume_text += page.extract_text()
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = Document(uploaded_file)
                resume_text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
       
        # Parse the resume using LLM chain
        parsed_resume = resume_parser_chain.run(resume_text=resume_text)
       
        # Validate and clean the output
        try:
            # Ensure the output is valid JSON
            resume_data = json.loads(parsed_resume)
            resume_data = Resume.parse_obj(resume_data)
            # Display parsed resume data
            st.json(resume_data.dict())
            generate_docx(resume_data)
        except (json.JSONDecodeError, ValidationError) as e:
            st.error(f"An error occurred while processing the resume: {e}")
            st.write(f"Raw output: {parsed_resume}")
    except Exception as e:
        st.error(f"An error occurred while reading the resume: {e}")
else:
    st.info("Please upload a resume to parse.")