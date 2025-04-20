import streamlit as st
from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from typing import TypedDict, Annotated
import pdfplumber
from langchain_core.output_parsers import StrOutputParser
from LLMLab45 import LlamaLLM
 
# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

llm = LlamaLLM()

class Parser_Resume(TypedDict):
    Summary: Annotated[str,"""Please review the resume and provide a concise summary of the candidate's
    key qualifications, experiences, and achievements.. The summary should be brief, clear, and to the point."""]
    mail_id: Annotated[str,"First Occurrence of Mail ID"]
    skills: Annotated[list[str],""""Please review the resume and list the skills mentioned by the candidate.
                                    Focus on  technical skills, including any specific tools, technologies, languages,
                                    or methodologies they are proficient in. Ensure to include any certifications or training that
                                    highlight their expertise."""]
    Business_Capabilities: Annotated[list[str],"""
                                    Please review the resume and identify the key business capabilities demonstrated by the candidate.
                                    Focus on skills, experiences, and achievements that highlight their ability to contribute to business operations, strategy, and growth.
                                    Consider aspects such as leadership, project management, financial acumen, strategic planning, and any industry-specific expertise."""]
    Functional_Capabilities: Annotated[list[str],"""
                                    Please review the resume and identify the key functional capabilities demonstrated by the candidate.
                                    Focus on skills, experiences, and achievements that highlight their ability to contribute to business operations, strategy, and growth.
                                    Consider aspects such as leadership, project management, financial acumen, strategic planning, and any industry-specific expertise."""]
    Education: Annotated[list[str],"""Please review the resume and provide the education details of the candidate.
                                      Focus on the degrees obtained, institutions attended, graduation dates, and any
                                      relevant certifications or courses completed. Ensure to include any honors or distinctions received."""]
    professional_experience: Annotated[list[str],""""Please review the resume and provide the professional experience details of the candidate.
                                      Focus on the job titles, companies worked for, employment dates, and key responsibilities and achievements in each role.
                                      Highlight any significant projects, leadership roles, and contributions that demonstrate the candidate's expertise and impact in their field."""]
    clients: Annotated[list[str],""""Please review the resume and provide a list of previous clients the candidate has worked with.
                                                  Focus on the client names, industries, and the nature of the projects or services provided.
                                                  Highlight any significant achievements or contributions made by the candidate while working with these clients."""]
 
structured_model = llm.with_structured_output(Parser_Resume)
 
# Streamlit application
st.title("Resume Parser")
 
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
 
if uploaded_file is not None:
    try:
        # Read the PDF file using pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
       
        if text:
            # Summarize the text before giving it to the LLM to create structured output
            summarised_text = llm.invoke("Kindly provide a comprehensive summary of your profile, ensuring to include your full name, email address, phone number, a list of your skills, details of your business capabilities, an overview of your functional capabilities, and a summary of your professional experience" + text)
            summarised_text_struc = summarised_text  # Use the summarised text directly as it is a string
            st.text_area("Summarized Text", summarised_text_struc, height=400)
           
            # Store the text in the resume variable
            resume = summarised_text_struc
           
            # Invoke the structured model with the resume text
            result = structured_model.invoke(resume)
            st.write(result)
        else:
            st.error("Failed to extract text from the PDF. Please upload a valid resume.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF file to proceed.")