import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import pdfplumber
import re
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
import win32com.client as win32
import pythoncom
import win32com.client as win32
import logging


# Initialize logging
logging.basicConfig(filename='email_monitor2.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to generate job description using Ollama 3.2 local LLM
def generate_job_description(job_desc, skills):
    # Initialize Ollama LLM
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0
    )
   
    # Prepare the prompt for the LLM
    prompt = f"Generate a job description based on the following details:\n\nJob Description: {job_desc}\n\nSkills:\n"
    for skill, level in skills.items():
        prompt += f"- {skill}: {level}\n"
   
    # Generate the job description using Ollama 3.2 local LLM
    generated_desc = llm.invoke(prompt)
 
    # Parse the output using StrOutputParser
    parser = StrOutputParser()
    generated_desc = parser.parse(str(generated_desc.content))
    return generated_desc
 
# Streamlit app
st.title("Recruitment Agent AI")
 
# Create tabs
tab1, tab2 = st.tabs(["JDGenerator", "Resume Ranker"])
 
with tab1:
    # Create a container for the submit button and align it to the top right
    button_container = st.container()
    with button_container:
        st.markdown(
            """
            <style>
            .stButton button {
                float: right;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
 
    # Input for job description
    col1, col2 = st.columns([4, 1])
    with col1:
        job_desc = st.text_input("Enter JD Role")
 
    # Input for number of skills
    with col2:
        num_skills = st.number_input("Number of Skills", min_value=1, max_value=5, step=1, key="num_skills")
 
    # Inputs for skills and levels in parallel columns
    skills = {}
    for i in range(num_skills):
        col1, col2 = st.columns([4, 1])  # Adjust column width ratio to make skill input text larger and level input shorter
        with col1:
            skill = st.text_input(f"Skill {i+1}", key=f"skill_{i+1}", max_chars=50)  # Increase max_chars for skill input
        with col2:
            level = st.selectbox(f"Level {i+1}", ["L1", "L2", "L3", "L4"], key=f"level_{i+1}")
        skills[skill] = level
 
    # Button to generate job description
    if st.button("Generate Job Description", key="generate_button"):
        generated_desc = generate_job_description(job_desc, skills)
        st.text_area("Generated Job Description", value=generated_desc, height=300)
 
with tab2:
    # Load job description and resumes
    job_description = st.text_area("Enter Job Description")
    uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=["pdf"])
 
    # Function to read resumes from PDF files and extract email addresses
    def read_resumes(files):
        resumes = []
        emails = []
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
 
        for file in files:
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                resumes.append(text)
 
                # Extract email addresses from the text
                email_matches = re.findall(email_pattern, text)
                if email_matches:
                    emails.append(email_matches)  # Assuming the first match is the candidate's email
 
        return resumes, emails
 
    # Function to rank resumes using LangChain and Ollama
    def rank_resumes_ollama(job_desc, resumes):
        llm = ChatOllama(
            model="llama3.2:latest",
            temperature=0,
            num_gpu = 0
        )
        prompt_template = PromptTemplate(
            input_variables = ["job_desc", "resume"],
            template = """Match the following job description with the resume and provide a score between 1-100 and also provide matching reason in one sentence:
            Job Description:{job_desc}
            Resume:{resume}
            Score:
            Match Reason:"""
        )
        chain = LLMChain(llm=llm, prompt=prompt_template)
 
        scores = []
        match_reason = []
        for resume in resumes:
            response = chain.run({"job_desc": job_desc, "resume": resume})
            print(response)
            score_match = re.search(r'Score:\s*(\d+)', response)
            match_reason_match = re.search(r'Match Reason:\s*(.*)', response)
            if score_match:
                score1 = int(score_match.group(1))
                scores.append(float(score1))  # Convert score to float
            else:
                scores.append(0)  # Assign a default score if no match is found
            if match_reason_match:
                match = match_reason_match.group(1) # type: ignore
                match_reason.append(match)  # Convert score to float
            else:
                match_reason.append(0)  # Assign a default score if no match is found
        return scores, match_reason
    df_results_out=pd.DataFrame()
    
    def send_emails(df):
        try:
            pythoncom.CoInitialize()  # Initialize the COM library
            outlook = win32.Dispatch('outlook.application')
            print(df)
            for index, row in df.iterrows():
                mail = outlook.CreateItem(0)
                mail.To = str(row['Email']),
                mail.Subject = 'Congratulations! You have Been Shortlisted for the Position'
                mail.Body = f"Dear Candidate,\n\nWe have reviewed your resume and found it suitable for the following job role:\n\nYour resume score is: {row['Score']}%\nMatching Reason: {row['Match Reason']}\n\nBest regards,\nRecruitment Team"
                mail.Send()
            print("Emails sent successfully.")
        except Exception as e:
            logging.error(f"Error sending emails{e}")
            print(f"An error occurred: {e}")

    # if st.button("Match"):
        
    #     if uploaded_files:
    #         resumes, emails = read_resumes(uploaded_files)
    #         scores, match_reason = rank_resumes_ollama(job_description, resumes)
            
    #         st.write("Ranked Resumes:")
    #             # Create a DataFrame to store the results
    #         df_results = pd.DataFrame({
    #             'File Name': [file.name for file in uploaded_files],
    #             'Score': scores,
    #             'Email': emails,
    #             'Match Reason': match_reason,
    #             'Resume Text': resumes  # Optional: Include resume text if needed for further processing or analysis
    #             })
    #         df_results_out = pd.concat([df_results_out, df_results], ignore_index=True)
    #     st.dataframe(df_results_out)
    #     #send_emails(df_results_out)
        
    #     # Button to send emails to candidates based on DataFrame results
    #     if st.button("Send Emails", key="send_emails"):
    #         try:
    #             print("Button Clicked")
    #             st.write("Email Button Clicked")
    #             send_emails(df_results_out)
    #             st.dataframe(df_results_out)
    #         except Exception as e:
    #             logging.error(f'Error Encountered: {e}')
        # Initialize session state for buttons
if 'df_results_out' not in st.session_state:
    st.session_state.df_results_out = pd.DataFrame()

if st.button("Match"):
    if uploaded_files:
        resumes, emails = read_resumes(uploaded_files)
        scores, match_reason = rank_resumes_ollama(job_description, resumes)
        
        st.write("Ranked Resumes:")
        # Create a DataFrame to store the results
        df_results = pd.DataFrame({
            'File Name': [file.name for file in uploaded_files],
            'Score': scores,
            'Email': emails,
            'Match Reason': match_reason,
            'Resume Text': resumes  # Optional: Include resume text if needed for further processing or analysis
        })
        st.session_state.df_results_out = pd.concat([st.session_state.df_results_out, df_results], ignore_index=True)
    st.dataframe(st.session_state.df_results_out)
    #send_emails(st.session_state.df_results_out)

    # Button to send emails to candidates based on DataFrame results
if st.button("Send Emails", key="send_emails"):
    try:
        print("Button Clicked")
        st.write("Email Button Clicked")
        send_emails(st.session_state.df_results_out)
        #st.dataframe(st.session_state.df_results_out)
        st.session_state.df_results_out = pd.DataFrame()
    except Exception as e:
        logging.error(f'Error Encountered: {e}')