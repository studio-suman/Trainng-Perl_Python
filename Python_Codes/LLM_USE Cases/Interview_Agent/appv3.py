import os
from pydantic import Extra
import requests
from typing import Any, List, Mapping, Optional
import json
import ast
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
# Run chain
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_ollama import OllamaEmbeddings # type: ignore
import warnings
warnings.filterwarnings('ignore')
 
##################################
 
os.environ["token"] = "Bearer token|21031658-00bd-47ae-bbcb-c4d9e6c1146f|c87e47bd3697e43906884735e46c827bfc7dee361628b9e7ad26d369bfadc098"
token = os.environ["token"]
 
#################################
 
from typing import ClassVar
 
parser = StrOutputParser()
 
class LlamaLLM(LLM):
    llm_url: ClassVar[str] = 'https://api.lab45.ai/v1.1/skills/completion/query'
   
    backend:        Optional[str]   = 'gpt-35-turbo-16k'
    temp:           Optional[float] = 0.7
    top_p:          Optional[float] = 0.1
    top_k:          Optional[int]   = 40
    n_batch:        Optional[int]   = 8
    n_threads:      Optional[int]   = 4
    n_predict:      Optional[int]   = 256
    max_tokens:     Optional[int]   = 256
    repeat_last_n:  Optional[int]   = 64
    repeat_penalty: Optional[float] = 1.18
 
    class Config:
        extra = Extra.forbid
 
    @property
    def _llm_type(self) -> str:
        return "gpt-35-turbo-16k"
   
    @property
    def _get_model_default_parameters(self):
        return {
            "max_tokens": self.max_tokens,
            #"n_predict": self.n_predict,
            "top_k": self.top_k,
            "top_p": self.top_p,
            "temperature": self.temp,
            #"n_batch": self.n_batch,
            #"repeat_penalty": self.repeat_penalty,
            #"repeat_last_n": self.repeat_last_n,
        }
 
    def _call(
        self,
        prompt: str,
        user: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
 
        payload = {
        "messages": [
            {
            "content": prompt,
            "role": user
            }
        ],
        "skill_parameters": {
            "model_name": "gpt-35-turbo-16k",
            "max_output_tokens": 4096,
            "temperature": 0,
            "top_k": 5
        },
        "stream_response": False
        }
 
        headers = {"Content-Type": "application/json","Authorization": token}
 
        response = requests.post(self.llm_url, json=payload, headers=headers, verify=False)
 
       # print("API Response:", response.json())
        response.raise_for_status()
 
        return response.json()  # get the response from the API
 
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "llmUrl": self.llm_url,
            'model_parameters': self._get_model_default_parameters
           
            }
   
################################################################################################
 
 
from pydantic import BaseModel
from typing import Dict
 
class InterviewQA(BaseModel):
    questions_and_answers: Dict[str, str]
 
####################################################PYDANTIC OUTPUT PARSER
   
llm = LlamaLLM()
user="user"
 
import streamlit as st
import fitz  # PyMuPDF
import docx
import re
 
# ---------------------- File Reading Functions ----------------------
 
def read_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text() # type: ignore
    return text
 
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text
 
def extract_text_from_txt(file):
    return file.read().decode('utf-8')
 
# ---------------------- LLM Interaction Functions ----------------------
 
def analyze_jd_resume_match(job_description, resume):
    prompt = f"""
Compare the following Job Description and Candidate Resume. Provide a detailed summary including:
 
1. Technical Skill Match
2. Functional Skill Match
3. Experience Relevance
4. Domain Knowledge Alignment
5. Soft Skills Match
6. Overall Match Percentage between 1 to 100, give exact percentage
 
Job Description:
{job_description}
 
Candidate Resume:
{resume}
"""
    response = llm._call(prompt, user)
    content = response['data']['content'] # type: ignore
    match = re.search(r"(\d+)%", content)
    score = int(match.group(1)) if match else 0
    return content, score
 
def generate_interview_questions(job_description):
    prompt = f"""
Given the following Job Description: {job_description}
 
Generate a structured set of 100 interview questions **along with their answers** to assess the candidate's expertise. Do not categorize the questions. Return them as a flat dictionary where each key is a question and each value is its corresponding answer.
 
Ensure the questions cover a mix of:
- Basic concepts
- Intermediate knowledge
- Advanced skills
- Specialized domain expertise
 
Return the output as a JSON object that conforms to the following Pydantic model:
 
class InterviewQA(BaseModel):
    questions_and_answers: Dict[str, str]
"""
    response = llm._call(prompt, user)
    response = safe_parse_json(response['data']['content'])  # type: ignore
    return response  # type: ignore
 
def simulate_interview(job_description, resume, responses):
    prompt = f"Job Description:\n{job_description}\n\nCandidate Resume:\n{resume}\n\nInterview Responses:\n{responses}\n\nAnalyze the candidate's skills based on the interview responses."
    response = llm._call(prompt, user)
    return response['data']['content'] # type: ignore


def safe_parse_json(raw_json: str):
        # Step 1: Remove Markdown formatting
        cleaned = re.sub(r"^```json|```$", "", raw_json.strip(), flags=re.MULTILINE).strip()
 
        # Step 2: Try standard JSON parsing
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass
 
        # Step 3: Try using ast.literal_eval (handles Python-style dicts)
        try:
            return ast.literal_eval(cleaned)
        except (ValueError, SyntaxError):
            pass
 
        # Step 4: Try fixing common issues manually
        cleaned = cleaned.replace('\n', '\\n').replace('\r', '')
        cleaned = re.sub(r'(?<!\\)"', '\\"', cleaned)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return None


# ---------------------- Streamlit App ----------------------
 
st.title("Interactive Interview Simulator")
 
# Initialize session state variables
for key in ["interview_stage", "questions", "responses", "allow_interview", "start_interview", "match_score", "match_summary"]:
    if key not in st.session_state:
        st.session_state[key] = 0 if key == "interview_stage" else [] if key in ["questions", "responses"] else False if key in ["allow_interview", "start_interview"] else None
 
# Upload job description
job_description_file = st.file_uploader("Upload Job Description (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
if job_description_file:
    if job_description_file.type == "application/pdf":
        job_description = read_pdf(job_description_file)
    elif job_description_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        job_description = extract_text_from_docx(job_description_file)
    elif job_description_file.type == "text/plain":
        job_description = extract_text_from_txt(job_description_file)
    st.text_area("Job Description", job_description, height=200)
else:
    job_description = None
 
# Upload candidate resume
resume_file = st.file_uploader("Upload Candidate Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
if resume_file:
    if resume_file.type == "application/pdf":
        resume = read_pdf(resume_file)
    elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume = extract_text_from_docx(resume_file)
    elif resume_file.type == "text/plain":
        resume = extract_text_from_txt(resume_file)
    st.text_area("Candidate Resume", resume, height=200)
else:
    resume = None
 
# JD-Resume Matching Analysis
if job_description and resume:
    if st.button("Analyze JD-Resume Match"):
        match_summary, match_score = analyze_jd_resume_match(job_description, resume)
        st.session_state.match_summary = match_summary
        st.session_state.match_score = match_score
        st.session_state.start_interview = False  # Reset interview flag
 
# Display match results
if st.session_state.match_score is not None:
    st.subheader("JD-Resume Matching Summary")
    st.text_area("Matching Analysis", st.session_state.match_summary, height=300)
 
    if st.session_state.match_score < 60:
        st.warning(f"Overall Match Score is {st.session_state.match_score}%. This is considered low.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Continue and Apply Anyway"):
                st.session_state.allow_interview = True
                st.session_state.start_interview = True
        with col2:
            if st.button("Skip This Role"):
                st.session_state.allow_interview = False
                st.session_state.start_interview = False
    else:
        st.success(f"Overall Match Score is {st.session_state.match_score}%. You are a good fit!")
        st.session_state.allow_interview = True
        st.session_state.start_interview = True
 
# Generate Interview Questions
if st.session_state.start_interview and st.session_state.allow_interview and not st.session_state.questions:
      
    parsed = generate_interview_questions(job_description)
    #parsed = safe_parse_json(raw_json)
    st.json(parsed, expanded=False)  # Display the raw JSON for debugging
    if parsed and isinstance(parsed, dict):
        qa_dict = {
            q.strip(): a.strip()
            for q, a in parsed.items()
            if isinstance(q, str) and isinstance(a, str)
        }
        st.session_state.questions = [(q, a) for q, a in qa_dict.items()]
        st.session_state.interview_stage = 0
        st.session_state.responses = []
        st.session_state.start_interview = False
    else:
        st.error("Failed to parse interview questions. Please try again.")
 
# Conduct interview
if st.session_state.questions and st.session_state.allow_interview:
    if st.session_state.interview_stage < len(st.session_state.questions):
        question, expected_answer = st.session_state.questions[st.session_state.interview_stage]
        st.write(f"**Question {st.session_state.interview_stage + 1}:** {question}")
 
        answer_key = f"answer_{st.session_state.interview_stage}"
        if answer_key not in st.session_state:
            st.session_state[answer_key] = ""
 
        st.session_state[answer_key] = st.text_input("Your answer:", value=st.session_state[answer_key])
 
        if st.button("Submit Answer"):
            st.session_state.responses.append({
                "question": question,
                "expected_answer": expected_answer,
                "user_answer": st.session_state[answer_key]
            })
            st.session_state.interview_stage += 1
            st.success("Answer submitted. Proceed to next question.")
        
        if st.button("Next"):
            st.rerun()

    else:
        st.write("Interview completed. Generating skill analysis report...")
        formatted_responses = "\n".join(
            f"Q: {r['question']}\nExpected: {r['expected_answer']}\nUser: {r['user_answer']}"
            for r in st.session_state.responses
        )
        report = simulate_interview(job_description, resume, formatted_responses)
        st.text_area("Skill Analysis Report", report, height=300)