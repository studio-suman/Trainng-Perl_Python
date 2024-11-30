#
# 
# Google Gemini API Based AI Model
# Sourced from Open Source
# Compiled by Suman Saha v2.0
# Date : 30th November 2024
# 

import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#genai.configure(api_key=api_Key)


#gemini function added

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

#convert pdf to text
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

input_prompt ="""

### As a skilled Application Tracking System (ATS) with advanced knowledge in technology and data science, your role is to meticulously evaluate a candidate's resume based on the provided job description. 

### Your evaluation will involve analyzing the resume for relevant skills, experiences, and qualifications that align with the job requirements. Look for key buzzwords and specific criteria outlined in the job description to determine the candidate's suitability for the position.

### Provide a detailed assessment of how well the resume matches the job requirements, highlighting strengths, weaknesses, and any potential areas of concern. Offer constructive feedback on how the candidate can enhance their resume to better align with the job description and improve their chances of securing the position.

### Your evaluation should be thorough, precise, and objective, ensuring that the most qualified candidates are accurately identified based on their resume content in relation to the job criteria.

### Remember to utilize your expertise in technology and data science to conduct a comprehensive evaluation that optimizes the recruitment process for the hiring company. Your insights will play a crucial role in determining the candidate's compatibility with the job role.
resume={text}
jd={jd}
### Evaluation Output:
1. Calculate the percentage of match between the resume and the job description. Give a number out of 100 and some explanation.
2. Highlights and Lowlights of the resume.
3. Identify any key keywords that are missing from the resume in comparison to the job description.
"""
#4. Offer specific and actionable tips to enhance the resume and improve its alignment with the job requirements.

input_prompt2 = """

### As a skilled Technical Interview Panel with advanced knowledge in technology and data science, your role is to meticulously evaluate a employer job description and provide technical Questions. 

### Your evaluation will involve analyzing the job description for relevant skills, experiences that align with the job requirements. Look for key buzzwords and specific criteria outlined in the job description to determine the potential Questions and Answers.

### Your evaluation should be thorough, precise, and objective, ensuring that the most relevant Questions and Answers are found that provide algorithm

jd={jd}
### Evaluation Output:
1. Provide most relevant Questions and Answers in multiple choice options limiting to 5 options in below format A, B, C, D
2. Provide atleast min 15 Questions and Answers span around 20 minutes duration
3. Generate Real Use Case wise Questions and logical Question and avoid salary based questions
4. Provide min 5 Code Sample Based Questions are mandatory
"""
##streamlit

#st.header("WDC Smart ATS")

st.title("Smart Job Description Resume AI")
st.text("Improve your ATS resume score Match")
jd = st.text_area("Paste job description here")

option = st.radio(
    "Please Select Below Options",
    ("Resume", "Job Description"),
    index= None# Using tuple instead of separate strings
)

if option == "Resume":
    uploaded_file= st.file_uploader("Upload Resume", type="pdf", help= "Please upload the pdf")
    

submit =  st.button('Get The Score')
if submit:
   if option == "Resume":
    if uploaded_file is not None:
        text =  input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt.format(text=text,jd=jd))
        st.subheader(response)
   else :
        response=get_gemini_response(input_prompt2.format(jd=jd))
        st.subheader(response) 
