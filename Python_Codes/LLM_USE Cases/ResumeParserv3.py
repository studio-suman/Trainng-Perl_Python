import streamlit as st
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import pdfplumber
import json
import os
from generate_resume import generate_formatted_resume_layout2_with_dividers
from pydantic import BaseModel
from typing import List
from langchain.prompts import PromptTemplate
from LLM45 import LlamaLLM  # Your custom LLM wrapper
 
# Define the Pydantic model for structured output
class Resume(BaseModel):
    name: str
    email: str
    phone: str
    summary: str
    skills: List[str]
    certifications: List[str]
    experience: List[dict]
    education: List[dict]
 
# Prompt template for resume parsing
prompt_template = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    Extract the following information from the resume:
    - Name
    - Email
    - Phone
    - Linkedin Look for any linkedin.com profile mentioned in the resume
    - Summary
    - Skills
    - Certifications
    - Experience with Roles and Responsibilities
    - Education OR Academic Profile
 
    Provide the output in JSON format with the following keys:
    - Name
    - Email
    - Phone
    - Linkedin
    - Summary
    - Skills
    - Certifications
    - Experience
    - Education
 
    For each experience, extract:
    - Title
    - Company
    - Duration
    - Roles and Responsibilities (as a list)
 
    For each education entry, extract:
    - Degree
    - Institution
    - Duration or Year
 
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
                return "".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        st.error(f"Error reading resume: {e}")
        return None
 
def parse_resume(resume_text):
    try:
        summarised_text = llm._call(
            "Kindly provide summary of profile, ensuring to include full name, email address, phone number, only single list of technical skills without categorizing, details of business capabilities, an overview of functional capabilities and complete professional experience along with roles and responsibilities if any" + resume_text,
            user="user"
        )
        formatted_prompt = prompt_template.format(resume_text=summarised_text)
        parsed_resume = llm._call(prompt=formatted_prompt, user="user")
 
        if isinstance(parsed_resume, str):
            parsed_resume = json.loads(parsed_resume)
 
        if isinstance(parsed_resume, dict) and "data" in parsed_resume and "content" in parsed_resume["data"]:
            parsed_resume = parsed_resume["data"]["content"]
 
        return parsed_resume
    except Exception as e:
        st.error(f"Error parsing resume: {e}")
        return None
 
# Streamlit UI
st.title("📄 Resume Parser")
 
uploaded_file = st.file_uploader("Upload your resume", type=["txt", "pdf", "docx"])
 
parsed_result = None
 
if uploaded_file is not None:
    with st.spinner("Reading and parsing resume..."):
        resume_text = read_resume(uploaded_file)
        if resume_text:
            parsed_result = parse_resume(resume_text)
 
if parsed_result:
    if isinstance(parsed_result, str):
        try:
            parsed_result = json.loads(parsed_result)
        except json.JSONDecodeError as e:
            st.error(f"Failed to decode parsed result: {e}")
            st.stop()
 
    if not isinstance(parsed_result, dict):
        st.error("Parsed result is not a dictionary. Cannot proceed.")
        st.stop()
 
    if 'Name' not in parsed_result:
        st.error("The 'Name' field is missing in the parsed result.")
        st.stop()
 
    st.subheader("📋 Parsed Resume Data")
    st.json(parsed_result)
 
    # Save and offer download
    save_path = os.path.join(os.path.expanduser("~"), "Documents", "resumeparser")
    os.makedirs(save_path, exist_ok=True)
 
    try:
        resume_json = json.dumps(parsed_result)
        file_path = generate_formatted_resume_layout2_with_dividers(resume_json, save_path)
 
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Formatted Resume",
                    data=f.read(),
                    file_name=file_name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            st.success("Resume generated and ready for download!")
        else:
            st.error("Failed to generate resume. Please check the logs or try again.")
    except Exception as e:
        st.error(f"Error generating or downloading resume: {e}")