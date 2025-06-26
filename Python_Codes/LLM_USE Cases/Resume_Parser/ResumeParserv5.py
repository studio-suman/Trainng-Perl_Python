#Final Version Ready for Deployment v5.1 18 June 2025

from click import password_option
import streamlit as st
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import logging
import pdfplumber
import json
import os
from generate_resume import layout3, layout1, layout2 # docx templates for different layouts
import ResumeParservDTS
from pydantic import BaseModel, EmailStr
from typing import List
from langchain.prompts import PromptTemplate
from LLMLab45 import LlamaLLM  # Your custom LLM wrapper

# Configure logging to enabled
logging.basicConfig(filename='resume_generator.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
 
# Define the Pydantic model for structured output
class Resume(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: str
    summary: str
    skills: List[str]
    certifications: List[str]
    experience: List[dict]
    education: List[dict]

class User(BaseModel):
    username: str
    password: str

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
                #return "".join([page.extract_text() for page in pdf.pages if page.extract_text()])
                text = ""
                for page in pdf.pages:
                    # Extract regular text
                    if page.extract_text():
                        text += page.extract_text() + "\n"
 
                    # Extract tables
                    tables = page.extract_tables()
                    for table in tables:
                        for row in table:
                            text += "\t".join(cell if cell else "" for cell in row) + "\n"
            return text
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        logging.error(f"Error reading resume: {e}")
        st.error("Please try to upload again")
        return None

#New Code 
def parse_resume(resume_text):
    try:
        summarised_text = llm._call(
            "Kindly provide summary of profile, ensuring to include full name, email address, phone number, only single list of technical skills without categorizing, details of business capabilities, an overview of functional capabilities and complete professional experience along with roles and responsibilities if any,special notes read the entire profile before summarising as there can be multiple prifile formats emmeded one below another, Read profile till the end and the summarise" + resume_text,
            user="user"
        )
        formatted_prompt = prompt_template.format(resume_text=summarised_text)
        parsed_response = llm._call(prompt=formatted_prompt, user="user")
        #st.write(parsed_resume)
 
        if isinstance(parsed_response, dict) and "data" in parsed_response and "content" in parsed_response["data"]: # type: ignore
            parsed_text = parsed_response["data"]["content"] # type: ignore
        else:
            parsed_text = parsed_response

        if isinstance(parsed_text, str):
            parsed_text = parsed_text.strip()
            if parsed_text.startswith("```json"):
                parsed_text = parsed_text.replace("```json", "").strip()
            if parsed_text.endswith("```"):
                parsed_text = parsed_text.replace("```", "").strip()
                print(type(parsed_text))
            parsed_resume = json.loads(parsed_text)
            
            return parsed_resume
    except Exception as e:
        logging.error(f"Error parsing resume: {e}")
        st.error("Please try to upload again")
        return None
 
# ... [imports and initial setup remain unchanged] ...
 
# Helper function to generate and offer download
def generate_and_offer_download(parsed_result, layout_function):
    try:
        save_path = os.path.join(os.path.expanduser("~"), "Documents", "resumeparser")
        os.makedirs(save_path, exist_ok=True)
        resume_json = json.dumps(parsed_result)
        file_path = layout_function(resume_json, save_path)
 
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download",
                    data=f.read(),
                    file_name=file_name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            #st.success("Resume generated and ready for download!")
        else:
            logging.error("Failed to generate resume. Please check the logs or try again.")
            st.error("Please try to upload again")
    except Exception as e:
        logging.error(f"Error generating or downloading resume: {e}")
        st.error("Please try to upload again")
 
# Layout selection functions
def option_one(parsed_result):
    st.success("Layout 1 selected!")
    generate_and_offer_download(parsed_result, layout1)
 
def option_two(parsed_result):
    st.success("Layout 2 selected!")
    generate_and_offer_download(parsed_result, layout2)  # Replace with layout2 if available
 
def option_three(parsed_result):
    st.success("Layout 3 selected!")
    generate_and_offer_download(parsed_result, layout3)  # Replace with layout3 if different


# Image layout options
images = [
    ("Kallisti", "./New folder/Layout1.png", option_one),
    ("Phaedon", "./New folder/Layout2.png", option_two),
    ("Erasmos", "./New folder/Layout3.png", option_three),
]

user = User(username="admin", password="password123")

# Recruit Agent
def show_recruit_agent():
        st.markdown("### 📄 Recruitment Agent")
        st.write("Generate a structured profile using the selected layout for a given profile.")
        #st.markdown("<h1 style='font-size: 30px;'>📄 Recruitment Agent</h1>", unsafe_allow_html=True)
        st.markdown("<h8 style='font-size: 16px;'>Upload your resume</h8>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload your resume", label_visibility="collapsed", type=["pdf", "docx"])
    
        parsed_result = None
        
        if uploaded_file is not None:
            with st.spinner(f"Processing {uploaded_file.name}..."):
                resume_text = read_resume(uploaded_file)
                if resume_text:
                    parsed_result = parse_resume(resume_text)
        
        if parsed_result:
            #st.json(parsed_result)
            st.markdown(f"### Parsed Result for: {uploaded_file.name}") # type: ignore
            if isinstance(parsed_result, str):
                try:
                    parsed_result = json.loads(parsed_result)
                except json.JSONDecodeError as e:
                    logging.error(f"Failed to decode parsed result: {e}")
                    st.error("Please try to upload again")
                    st.stop()
        
            if not isinstance(parsed_result, dict):
                logging.error("Parsed result is not a dictionary. Cannot proceed.")
                st.error("Please try to upload again")
                st.stop()
        
            if 'Name' not in parsed_result:
                logging.error("The 'Name' field is missing in the parsed result.")
                st.error("Please try to upload again")
                st.stop()
        
            # Layout selection UI
            st.markdown("<h8 style='font-size: 16px;'>Choose a Layout:</h8>", unsafe_allow_html=True)
            cols = st.columns(3, vertical_alignment="center")
            for i, (title, img_path, func) in enumerate(images):
                with cols[i]:
                    st.image(img_path, use_container_width=False)
                    if st.button(f"Layout: {title}", use_container_width=True):
                        func(parsed_result)

# Sales Agent
def show_sales_agent():
        st.markdown("### 📈 Sales Agent Page")
        st.write("Generate a one-slide PowerPoint presentation for the given profile.")
        ResumeParservDTS.ppt_call()

# Admin Page
def show_admin_page():
   st.title("Admin Page")
   st.subheader("Add New User")
   new_username = st.text_input("New Username", key="new_username")
   new_password = st.text_input("New Password", type="password", key="new_password")
   if st.button("Add User"):
       if new_username and new_password:
           st.session_state.users[new_username] = new_password
           st.success(f"User '{new_username}' added successfully.")
       else:
           st.error("Please enter both username and password.")

   st.subheader("Add Token")
   new_token = st.text_input("New Token", key="new_token")
   if st.button("Add Token"):
       if new_token:
           st.session_state.tokens.append(new_token)
           st.success("Token added successfully.")
       else:
           st.error("Please enter a token.")

   st.write("Current Tokens:")
   for token in st.session_state.tokens:
       st.write(f"- {token}")

   if st.button("Back to Welcome Page"):
       st.session_state.page = "Welcome Page"

# Welcome page
def show_welcome_page():  
    if st.session_state.page == "Welcome":
        st.session_state.page = "Welcome"
    st.sidebar.markdown("## 📋 Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Recruitment Agent", "Sales Agent", "Build Your Resume(WIP)","Admin"])
    # Page Routing
    if page == "Welcome":
        st.session_state.page = "Welcome"
        st.markdown("### 👋 Welcome to LLM - Powered TalentStream Pro!")
        st.markdown(
        "<br> <br> A cutting-edge solution using advanced LLM technology to automate resume extraction and streamline document formatting for recruitment and sales support. <br> The system offers three predefined document formats, ensuring consistency and efficiency for agents. It also supports sales teams in creating one-slide PowerPoint presentations for RFPs. <br> In an upcoming enhancement, users will have the option to upload custom templates for automatic conversion of resumes. TalentStream Pro revolutionizes recruitment and sales processes, enhancing overall efficiency and consistency.",unsafe_allow_html=True)
    elif page == "Recruitment Agent":
        show_recruit_agent()
    elif page == "Sales Agent":
        show_sales_agent()
    elif page == "Build Your Resume(WIP)":
        st.markdown("### 📝 Build Your Resume")
        st.write("This feature will allow you to create a resume from scratch.")
    elif page == "Admin":
        st.session_state.page = "Admin"
        show_admin_page()
    
    #st.sidebar.info("Use this panel to navigate or view instructions.")
    st.sidebar.markdown("### 🔍 Instructions")
    st.sidebar.write("""
    1. Upload your resume in PDF, DOCX format.
    2. Wait for the resume to be parsed.
    3. Choose your preferred layout.
    4. Download the generated resume.
    """)
    st.sidebar.markdown("### 👤 Logged in as: `" + st.session_state.username + "`")   

def show_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])  # Center the input box

    with col2:
        st.markdown("#### Welcome to TalentStream Pro")
        user_name = st.text_input("Username", key="user_name")
        pass_word = st.text_input("Password", type="password", key="pass_word")

        if st.button("Login"):
            if user_name in st.session_state.users and st.session_state.users[user_name] == pass_word:
                st.session_state.logged_in = True
                st.session_state.username = user_name
                st.session_state.page = "Welcome"
            else:
                st.error("Invalid username or password")

# Streamlit UI
st.set_page_config(page_title='TalentStream Pro', initial_sidebar_state = 'auto')

# Initialize session state variables
if 'logged_in' not in st.session_state:
       st.session_state.logged_in = False
if 'username' not in st.session_state:
       st.session_state.username = ""
if 'users' not in st.session_state:
       st.session_state.users = {"admin": "password123", "krishnakanth": "password123", "manish": "password123"}   # Default admin user
if 'tokens' not in st.session_state:
       st.session_state.tokens = []

if "page" not in st.session_state:
       st.session_state.page = "Welcome"


# Display appropriate page
if st.session_state.logged_in:
    show_welcome_page()
else:
    show_login_page()
