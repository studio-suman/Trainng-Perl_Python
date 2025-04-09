from huggingface_hub import User
import streamlit as st
import pandas as pd
import pdfplumber
import docx
from langchain_ollama import ChatOllama
import re
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from CustomDocxBoiler import generate_docx
import LLMLab45

# Function to parse PDF
def parse_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text.strip().replace('\n', ' ').replace('\r', '')
    except Exception as e:
        st.error(f"Error parsing PDF: {e}")
        return ""

# Function to parse DOCX
def parse_docx(file):
    try:
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        st.error(f"Error parsing DOCX: {e}")
        return ""

# Function to parse resume text
def parse_resume(text):
    name = re.search(r'\*\*Name:\*\* ([^\n]+)', text, re.IGNORECASE)
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.search(r'\b\d{10}\b', text)
    education = re.search(r'\*\*Education:\*\*\n((?:\t\+ [^\n]+\n)+)', text, re.IGNORECASE)
    experience = re.search(r'\*\*Experience:\*\*\n((?:\t\+ [^\n]+\n)+(?:\t\t- [^\n]+\n)+)', text, re.IGNORECASE)
    skills = re.search(r'\*\*Skills:\*\* \n((?:\t\+ [^\n]+\n)+)', text, re.IGNORECASE)
    
    parsed_data = {
        'Name': name.group(1).strip() if name else 'N/A',
        'Email': email.group(0) if email else 'N/A',
        'Phone': phone.group(0) if phone else 'N/A',
        'Education': education.group(1).strip() if education else 'N/A',
        'Experience': experience.group(1).strip() if experience else 'N/A',
        'Skills': skills.group(1).strip() if skills else 'N/A'
    }
    print(parsed_data)
    return parsed_data

#String Output Parser
parser = StrOutputParser()
# Load LLaMA model
def run_llm_chain(resume):
    llama_model = ChatOllama(
    model="llama3.2:latest",
    temperature=0,
    num_gpu=0
    )

    #llama_model = LLMLab45.LlamaLLM()

    prompt_template = PromptTemplate(
        
        input_variables=["resume"],
        template= """Could you please provide the following details based on {resume} and based your vast technical and analytical experience into below categories?
            Name: look for the candidate's name,
            Email: look for entries email address with @,
            Phone: look for the phone number with 10 digits,
            Education: look for education information,
            Experience: Overall experience in years and experience description,
            Skills: Technical skills worked and list the skills "," separated by
            give me the output in json format"""
        )

    # Create LangChain LLMChain
    llm_chain = LLMChain(llm=llama_model, prompt=prompt_template)
    #llm_chain = prompt_template | llama_model

    # Run LLMChain
    result = llm_chain.run(resume=resume)

    return result


# Streamlit app
st.title("Resume Parser with LLM")

uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=['pdf', 'docx'])

if uploaded_files:
    data = []
    for uploaded_file in uploaded_files:
        if uploaded_file.type == "application/pdf":
            text = parse_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = parse_docx(uploaded_file)
        parsed_data = run_llm_chain(text)
        data.append(parsed_data)
        st.json(parsed_data) #
        data.append(parsed_data)
        #generate_docx(parsed_data)  # Uncommented to generate DOCX for each parsed resume
        
    if data:
        df = pd.DataFrame(data, index=None)
        st.dataframe(df)
        #generate_docx(df)
    else:
        st.warning("No valid resumes were parsed.")
    
