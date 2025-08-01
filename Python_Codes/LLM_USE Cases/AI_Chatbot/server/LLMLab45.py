import os
from dotenv import load_dotenv
from pydantic import Extra
import requests
from typing import Any, List, Mapping, Optional, ClassVar

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain.prompts import PromptTemplate
# Run chain
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_ollama import OllamaEmbeddings # type: ignore

parser = StrOutputParser()
load_dotenv()


class LlamaLLM(LLM):
    llm_url: ClassVar[str] = 'https://api.lab45.ai/v1.1/skills/completion/query'
    
    
    @property
    def _llm_type(self) -> str:
        return "gpt-35-turbo-16k"
    
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
        os.environ["TOKEN"] = "Bearer token|4353b65f-2b1b-4e15-9d6c-47bd024700ac|389496b55d294f224d491863705ea80c3b1e723be3183cf9ff3db246fee1ca03"
        token = os.getenv("TOKEN")
        print(token)
        headers = {"Content-Type": "application/json","Authorization": token}

        response = requests.post(self.llm_url, json=payload, headers=headers, verify=False)

       # print("API Response:", response.json())
        response.raise_for_status()

        return response.json()  # get the response from the API

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "llmUrl": self.llm_url
            }