import io
import os
import time
from docx import Document
from openai import OpenAI
from langchain_openai import AzureChatOpenAI
from pydantic import Extra, SecretStr
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional
import requests
import streamlit as st
from sympy import true

st.set_page_config(page_title='Smart JD AI', initial_sidebar_state = 'auto',page_icon="favicon.ico") #page_icon="🦈"


col1, col2 = st.columns([10,60])
with col1:
    st.image("favicon.png")
with col2:
    st.title("ChatJob Description") 

client_id = "8dea253e-4cae-467b-88a5-88df4477c79f" #client_id_KK:"66ab59c3-896d-4de8-a2e9-3148b18ceeca" # client_id_suman#"8dea253e-4cae-467b-88a5-88df4477c79f"

os.environ["token"] = "Bearer token|123675a6-95f6-4fb7-bc95-30095472ae3a|02de311fd83421a7fd637bf34dc8f959caa29f39888d2919e4b9640a2220224b"
token = os.environ["token"]

from typing import ClassVar
parser = StrOutputParser()

#Calling Custom LLM Class for calling Lab45 API functions
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

    """ class Config:
        extra = Extra.forbid """

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

def lab45agent(prompt):
    # Define the API endpoint for interacting with the agents chatAPI
    agents_endpoint = f"https://api.lab45.ai/v1.1/agent_chat_session/query"  # The endpoint where agent-related operations are available

    # Set the headers for the request, including content type, accepted response format, and authorization token
    headers = {
        'Content-Type': "application/json",  # The content type is set to JSON, meaning the body will be JSON-encoded
        'Accept': "text/event-stream, application/json",  # The client expects either event-stream or JSON as the response format
        'Authorization': token  # Replace <api_key> with your actual API key for authentication
    }

    # Define the payload (request body) for the API call, which contains the conversation details and instructions for the agent
    payload = {
        "conversation_id": "",  
        "messages": [  
            {
                "content": prompt,  
                "name": "Suman",
                "role": "user"
            }
        ],
        "party_id": client_id,  # The unique ID of the party (here it is the agent_id which is generated in agents api)
        "party_type": "Agent",
        "save_conversation": False,  
        "stream_response": False
    }

    response = requests.post(agents_endpoint, headers=headers, json=payload)

    # Print the response from the API call to inspect the result (status code, content, etc.)
    return response.json()

def get_docx(text):
    document = Document()
    document.add_paragraph(text)
    ai_out = io.BytesIO()
    document.save(ai_out)
    return ai_out.getvalue()
def download_button(response):
    try:
        st.download_button(
                    label="Click here to download",
                    data=get_docx(response),
                    file_name="Generated_Output-"+time.strftime("%d%b%y")+".docx",
                    mime="docx"
                    )
    except Exception as e:
        st.error(f"An error occurred while generating the file: {e}")


 ####Upload section to upload documents
# if "uploader_visible" not in st.session_state:
#     st.session_state["uploader_visible"] = False
# def show_upload(state:bool):
#     st.session_state["uploader_visible"] = state
    
# with st.chat_message("system",avatar="🧑‍💻"):
#     cols= st.columns((3,1,1))
#     cols[0].write("Do you want to upload a file?")
#     cols[1].button("Yes", use_container_width=True, on_click=show_upload, args=[True]) # type: ignore
#     cols[2].button("No", use_container_width=True, on_click=show_upload, args=[False]) # type: ignore

# if st.session_state["uploader_visible"]:
#     with st.chat_message("system",avatar="🧑‍💻"):
#         file = st.file_uploader("Upload your data")
#         if file:
#             with st.spinner("Processing your file"):
#                  time.sleep(5) #<- dummy wait for demo.      
# #Senior Java Developer with Core Java L2, Spring Boot L2, Hibernate L2, Selenium L2 "

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can you help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        #show_upload(False)
    # with st.chat_message("system",avatar="🧑‍💻"):
    #     cols= st.columns((3,1,1))
    #     option = st.radio(
    # "Please Select Below Options",
    # ("Resume", "Questions From Job Description", "Generate Job Description"),
    # index= None# Using tuple instead of separate strings
    # )
    with st.chat_message("assistant"):
        #response = client._call(prompt,user) #calling custom LLM class
        response = lab45agent(prompt)
        parsed_result = response['data']['content'] #type: ignore
        parsed = parser.invoke(parsed_result) #type: ignore
        #download_button(parsed)
        st.markdown(parsed)
        #st.write_stream(response_generator(parsed))
        st.session_state.messages.append({"role": "assistant", "content": parsed})
