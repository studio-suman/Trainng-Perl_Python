import streamlit as st
from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict
import pdfplumber
import json
from langchain.prompts import PromptTemplate
from docx import Document
from doc3 import generate_formatted_resume
from LLMLab45 import LlamaLLM

# Define the Pydantic model for structured output
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
    - Experience with Roles and Responsibilities
    - Education

    Provide the output in JSON format with the following keys:
    - Name
    - Email
    - Phone
    - Summary
    - Skills
    - Experience
    - Education

    Resume text:
    {resume_text}
    """
)

# Initialize LLM
llm = LlamaLLM()

def read_resume(uploaded_file):
    try:
        if uploaded_file.type == "text/plain":
            return uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                return "".join([page.extract_text() for page in pdf.pages])
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        st.error(f"An error occurred while reading the resume: {e}")
        return None

def parse_resume(resume_text):
    try:
        summarised_text = llm._call("Kindly provide summary of profile, ensuring to include full name, email address, phone number, only single list of technical skills without categorizing, details of business capabilities, an overview of functional capabilities and complete professional experience along with roles and responsibilities if any" + resume_text, user="user")
        formatted_prompt = prompt_template.format(resume_text=summarised_text)
        parsed_resume = llm._call(prompt=formatted_prompt, user="user")
        if isinstance(parsed_resume, dict):
            parsed_resume = json.dumps(parsed_resume)
        parsed_resume_dict = json.loads(parsed_resume)
        return parsed_resume_dict['data']['content']
    except Exception as e:
        st.error(f"An error occurred while parsing the resume: {e}")
        return None

# Streamlit application to upload resumes and parse them
st.title("ResuMatic")

uploaded_files = st.file_uploader("Upload your resumes", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files:
    parsed_results = []
    for uploaded_file in uploaded_files:
        resume_text = read_resume(uploaded_file)
        if resume_text:
            parsed_result = parse_resume(resume_text)
            if parsed_result:
                parsed_results.append(parsed_result)
                generate_formatted_resume(parsed_result)  
    if parsed_results:
        st.json(parsed_results)
        st.success("Resumes generated successfully!")
else:
    st.info("Please upload resumes to parse.")
