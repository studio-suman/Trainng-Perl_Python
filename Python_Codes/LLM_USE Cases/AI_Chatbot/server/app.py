
import bcrypt
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt
import psycopg2
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from LLMLab45 import LlamaLLM

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: str
    password: str

class ChatRequest(BaseModel):
    message: str

SECRET_KEY = "secret"


@app.post("/api/login")
def login(data: LoginRequest):
    try:
        conn = psycopg2.connect(
            dbname="chatbot",
            user="postgres",
            password="sumansaha",
            host="localhost"
        )
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM users WHERE email=%s", (data.email,))
        result = cur.fetchone()
        print(result)
        if result:
            stored_hash = result[0]
            # If using bcrypt hashed passwords:
            if bcrypt.checkpw(data.password.encode(), stored_hash.encode()):
                token = jwt.encode({"email": data.email}, SECRET_KEY, algorithm="HS256")
                return {"token": token}
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

prompt_template = """You are Interactive Chat Agent, and respond politely and with human touch, witty answers where required"""

@app.post("/api/chat")
def chat(data: ChatRequest):
    # db = Chroma(persist_directory="./chroma_db", embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"))
    # qa = RetrievalQA.from_chain_type(llm=LlamaLLM(), retriever=db.as_retriever())
    llm=LlamaLLM()
    print(data.message)
    response = llm._call(f"{prompt_template}{data.message}","user")
    #response = qa.run(data.message)
    return {"response": response['data']['content']} # type: ignore