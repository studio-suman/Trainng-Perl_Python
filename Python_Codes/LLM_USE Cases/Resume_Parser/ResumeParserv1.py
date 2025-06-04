import streamlit as st
from langchain_ollama import ChatOllama
from typing import TypedDict
from typing_extensions import Annotated
import pdfplumber
#from CustomDocxBoilerv1 import generate_docx
import LLMLab45
#import os
 
# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

llm = LLMLab45.LlamaLLM()

class Parser_Resume(TypedDict):
    name: str
    mail_id: Annotated[str,"First Occurrence of Mail ID"]
    Summary: Annotated[str,"""Please review the resume and provide a concise summary of the candidate's
    key qualifications, experiences, and achievements. Focus on the most relevant information that
    highlights their suitability for the role.The summary should be brief, clear, and to the point."""]
    skills: Annotated[list[str],""""Please review the resume and list the skills mentioned by the candidate.
                                    Focus on both technical and soft skills, including any specific tools, technologies, languages,
                                    or methodologies they are proficient in. Ensure to include any certifications or training that
                                    highlight their expertise"""]
    Business_Capabilities:Annotated[list[str],"""
                                    Please review the resume and identify the key business capabilities demonstrated by the candidate.
                                    Focus on skills, experiences, and achievements that highlight their ability to contribute to business operations, strategy, and growth.
                                    Consider aspects such as leadership, project management, financial acumen, strategic planning, and any industry-specific expertise
"""]
    Functional_Capabilities:Annotated[list[str],"""
                                    Please review the resume and identify the key business capabilities demonstrated by the candidate.
                                    Focus on skills, experiences, and achievements that highlight their ability to contribute to business operations, strategy, and growth.
                                    Consider aspects such as leadership, project management, financial acumen, strategic planning, and any industry-specific expertise
"""]
    Education:Annotated[list[str],"""Please review the resume and provide the education details of the candidate.
                                      Focus on the degrees obtained, institutions attended, graduation dates, and any
                                      relevant certifications or courses completed. Ensure to include any honors or distinctions received."""]
    professional_experience:Annotated[list[str],""""Please review the resume and provide the professional experience details of the candidate.
                                      Focus on the job titles, companies worked for, employment dates, and key responsibilities and achievements in each role.
                                      Highlight any significant projects, leadership roles, and contributions that demonstrate the candidate's expertise and impact in their field."""]
    clients:Annotated[list[str],""""Please review the resume and provide a list of previous clients the candidate has worked with.
                                                  Focus on the client names, industries, and the nature of the projects or services provided.
                                                  Highlight any significant achievements or contributions made by the candidate while working with these clients."""]
 
structured_model = llm.with_structured_output(Parser_Resume)
 
# Streamlit application
st.title("Resume Parser using LLM")
 
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
 
if uploaded_file is not None:
    # Validate file size (max 10MB)
    if uploaded_file.size > 10 * 1024 * 1024:
        st.error("File size too large. Please upload a file less than 10MB.")
    else:
        try:
            # Show loading spinner while processing
            with st.spinner("Processing resume..."):
                # Read the PDF file using pdfplumber
                with pdfplumber.open(uploaded_file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text()

                # Validate content length
                resume = text[:6500]  # Truncate to 6500 chars
                if len(text) > 6500:
                    st.warning("Resume text was truncated to 6500 characters for processing")

                # Display the resume text in collapsible section
                with st.expander("View Resume Text"):
                    st.text_area("Original Text", resume, height=300)

                # Process resume with LLM
                    result = structured_model.invoke(resume)

                # Display results in organized sections
                if result:
                    st.subheader("Parsed Resume Information")
                    result = None
                
                # Display results in organized sections
                st.subheader("Parsed Resume Information")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("📝 Basic Information")
                    st.write(f"Name: {result['name']}") # type: ignore
                    st.write(f"Email: {result['mail_id']}") # type: ignore
                
                st.write("📋 Summary")
                st.write(result['Summary']) # type: ignore
                
                with st.expander("🔧 Skills"):
                    for skill in result['skills']: # type: ignore
                        st.write(f"• {skill}") # type: ignore
                
                with st.expander("💼 Business & Functional Capabilities"):
                    st.write("Business Capabilities:")
                    for cap in result['Business_Capabilities']: # type: ignore
                        st.write(f"• {cap}")
                    st.write("Functional Capabilities:")
                    for cap in result['Functional_Capabilities']: # type: ignore
                        st.write(f"• {cap}")
                
                with st.expander("🎓 Education"):
                    for edu in result['Education']: # type: ignore
                        st.write(f"• {edu}")
                
                with st.expander("👔 Professional Experience"):
                    for exp in result['professional_experience']: # type: ignore
                        st.write(f"• {exp}")
                
                with st.expander("🤝 Client History"):
                    for client in result['clients']: # type: ignore
                        st.write(f"• {client}")
            #generate_docx(result)
        except Exception as e:
            st.error(f"Error processing the PDF: {str(e)}")