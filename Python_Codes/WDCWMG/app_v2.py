import os
from openai import OpenAI
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("ChatGPT-like clone")

os.environ["AZURE_OPENAI_API_KEY"] = "ce53c5fce80c4503927244333e40634c"

client = OpenAI(api_key="ce53c5fce80c4503927244333e40634c",
                base_url="https://wdc-chat-llm.openai.azure.com/")

client = AzureChatOpenAI(
    azure_endpoint = "https://wdc-chat-llm.openai.azure.com/",
    api_key= SecretStr(os.environ["AZURE_OPENAI_API_KEY"]),
    azure_deployment = "gpt-4o",
    api_version = "2024-06-01",
    temperature= 0.3
)
parser = StrOutputParser()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.invoke(prompt)
        parsed = parser.invoke(response)
        st.markdown(parsed)