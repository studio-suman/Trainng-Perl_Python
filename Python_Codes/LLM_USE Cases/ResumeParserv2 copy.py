from pydantic import BaseModel, Field, ValidationError
from typing import List
import streamlit as st
from docx import Document
import pdfplumber
import json
from langchain.prompts import PromptTemplate
from doc1 import generate_resume
from LLMLab45 import LlamaLLM

#Define the Pydantic model for structured output
class Resume(BaseModel):
    name: str = Field(..., description="The name of the candidate")
    email: str = Field(..., description="The email address of the candidate")
    phone: str = Field(..., description="The phone number of the candidate")
    summary: str = Field(..., description="A brief summary of the candidate's profile")
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
    - Summary
    - Skills
    - Experience with Roles and Resposibilities
    - Education

    Provide the output in JSON format with the following keys:
    - name
    - email
    - phone
    - summary
    - skills
    - experience
    - education

    Resume text:
    {resume_text}
    """
)

# Initialize LLM
llm = LlamaLLM()

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
                with pdfplumber.open(uploaded_file) as pdf:
                    resume_text = ""
                    for page in pdf.pages:
                        resume_text += page.extract_text()
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = Document(uploaded_file)
                resume_text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

            summarised_text = llm._call("Kindly provide a comprehensive summary of profile, ensuring to include full name, email address, phone number, summary, a list of skills, details of business capabilities, an overview of functional capabilities, and complete professional experience" + resume_text, user="user")
            
            
            # Parse the resume using LLM chain
            formatted_prompt = prompt_template.format(resume_text=summarised_text)
            parsed_resume = llm._call(prompt=formatted_prompt, user="user")
            
            # Ensure parsed_resume is a JSON string
            if isinstance(parsed_resume, dict):
                parsed_resume = json.dumps(parsed_resume)

            parsed_resume_dict = json.loads(parsed_resume)
            parsed_result = parsed_resume_dict['data']['content']

            # Display parsed resume data
            st.json(parsed_result)
            #st.write(summarised_text)
            try:
                #generate_resume(parsed_result)
                st.success("Resume generated successfully!")
            except Exception as e:
                st.error(f"An error occurred while generating the resume: {e}")
            

    except Exception as e:
        st.error(f"An error occurred while reading the resume: {e}")
else:
    st.info("Please upload a resume to parse.")
