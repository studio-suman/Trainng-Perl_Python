import os
from openai import OpenAI
from langchain_openai import AzureChatOpenAI
from pydantic import Extra, SecretStr
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional
import requests
import streamlit as st

st.title("ChatJob Description")


os.environ["token"] = "Bearer token|123675a6-95f6-4fb7-bc95-30095472ae3a|02de311fd83421a7fd637bf34dc8f959caa29f39888d2919e4b9640a2220224b"
token = os.environ["token"]

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

client = LlamaLLM()

skill1="Core Java L1"
skill2="Spring Boot L2"
skill3="Hibernate L3"
skill4="Selenium L4"
title="Senior Java Full Stack Developer"
user = "system"
prompt1 = """As a skilled Technical Interview Panel with advanced knowledge in technology and data science, your role is to meticulously evaluate a employer job description and provide detailed job description having below points outlined.
            Use the mentioned skills & title to generate the job description, where L1 means Beginner, L2 means Intermediate, L3 means Advanced, and L4 means Expert,
            1. **Job Title and Summary**:
            - "What are the key responsibilities?"
            
            2. **Key Responsibilities**:
            - "List the main roles and responsibilities as per title and combination of skill along with proficiency"

            3. **Qualifications and Skills**:
            - "What qualifications are required?"
            - "List the essential skills needed and mention the level of expertise required."

            4. **Experience Requirements**:
            - "How many years of experience are needed?"
            - "What type of previous experience is beneficial?"

            """ + skill1 + skill2 + skill3 + skill4 + title
prompt2 =   """
            Use the mentioned skills & title to generate the job description, where L1 means Beginner, L2 means Intermediate, L3 means Advanced, and L4 means Expert,
            Job Title and Summary:
            "What are the key responsibilities?"
            Key Responsibilities:
            "List the main roles and responsibilities as per title and combination of skill along with proficiency"
            Qualifications and Skills:
            "What qualifications are required?"
            "List the essential skills needed and mention the level of expertise required."
            Experience Requirements:
            "How many years of experience are needed?"
            "What type of previous experience is beneficial?"
            """ + skill1 + skill2 + skill3 + skill4 + title



if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can you help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client._call(prompt,user)
        parsed_result = response['data']['content'] #type: ignore
        parsed = parser.invoke(parsed_result)
        st.markdown(parsed)