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
import json
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
    # name = re.search(r'\*\*Name:\*\* ([^\n]+)', text, re.IGNORECASE)
    # email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    # phone = re.search(r'\b\d{10}\b', text)
    # education = re.search(r'\*\*Education:\*\*\n((?:\t\+ [^\n]+\n)+)', text, re.IGNORECASE)
    # experience = re.search(r'\*\*Experience:\*\*\n((?:\t\+ [^\n]+\n)+(?:\t\t- [^\n]+\n)+)', text, re.IGNORECASE)
    # skills = re.search(r'\*\*Skills:\*\* \n((?:\t\+ [^\n]+\n)+)', text, re.IGNORECASE)
    
    name = re.search(r'Name:\s*(.*)', text)
    email = re.search(r'Email:\s*(.*)', text)
    phone = re.search(r'Phone:\s*(.*)', text)
    education = re.search(r'Education:\s*(.*?)(?=Experience:)', text, re.DOTALL)
    experience = re.search(r'Experience:\s*(.*?)(?=Skills:)', text, re.DOTALL)
    skills = re.search(r'Skills:\s*(.*)', text)

    parsed_data = {
        'Name': name.group(1).strip() if name else 'N/A',
        'Email': email.group(1) if email else 'N/A',
        'Phone': phone.group(1) if phone else 'N/A',
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
            Skills: Parse the Technical skills worked and list the skills "," separated by.
            """
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
        llm_result = run_llm_chain(text)
        parsed_data = parse_resume(llm_result)
        data.append(parsed_data)
              
    if data:
        df = pd.DataFrame({   
            'Name': [d['Name'] for d in data],
            'Email': [d['Email'] for d in data],
            'Phone': [d['Phone'] for d in data],
            'Education': [d['Education'] for d in data],
            'Experience': [d['Experience'] for d in data],
            'Skills': [d['Skills'] for d in data]
        })
        print(llm_result,"*****")
        st.dataframe(df)
        # for index, row in df.iterrows():  # generate the docx from each dataframe row
        #     generate_docx(row)  
        #     st.success(f"Generated DOCX for {row['Name']}")  
        
    else:
        st.warning("No valid resumes were parsed.")
