# filepath: rag_implementation.py

import os
from langchain_community.document_loaders import PyPDFDirectoryLoader # type: ignore
from langchain.embeddings import HuggingFaceEmbeddings # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain.chains import RetrievalQA # type: ignore
from langchain_ollama.llms import OllamaLLM # type: ignore
from langchain_ollama import OllamaEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_openai import AzureChatOpenAI


os.environ["AZURE_OPENAI_API_KEY"] = "ce53c5fce80c4503927244333e40634c"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://wdc-chat-llm.openai.azure.com/"
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = "gpt-4o"
os.environ["OPENAI_API_VERSION"] = "2024-06-01"



# Load documents from a local folder
def load_documents_from_folder(folder_path):
    #loader = DirectoryLoader(folder_path,glob="**/*.pdf",show_progress=True)
    loader = PyPDFDirectoryLoader(folder_path)
    documents = loader.load()
    return documents

# Embed and vectorize documents using FAISS
def embed_and_vectorize_documents(documents):
    embeddings = OllamaEmbeddings(model="llama3.2")
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

# Implement RAG
def implement_rag(vector_store, query):
    """     llm  = OllamaLLM(
    model="llama3.2",
    top_k=3
    ) """
    
    llm = AzureChatOpenAI(
    azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    api_version = os.environ["OPENAI_API_VERSION"],
    temperature= 0.3
    )
    
    retriever = vector_store.as_retriever()
    rag_chain = RetrievalQA(llm=llm, retriever=retriever)
    result = rag_chain.run(query)
    return result

messages = [
    SystemMessage(content="As Technical Recruiter Evaluate the following resumes"),
    HumanMessage(content="Hello Recruiter"),
]

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template)]
)

if __name__ == "__main__":
    folder_path = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\Temp2\Resume"
    query = ChatPromptTemplate.from_messages(
    [("system", system_template)])

    # Load documents
    documents = load_documents_from_folder(folder_path)

    # Embed and vectorize documents
    vector_store = embed_and_vectorize_documents(documents)

    # Implement RAG and get the result
    result = implement_rag(vector_store, query)
    print(result)
    