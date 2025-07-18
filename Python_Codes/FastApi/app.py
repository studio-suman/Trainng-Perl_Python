from fastapi import FastAPI

app = FastAPI()

# Creating Endpoints
# Localhost Endpoint

@app.get('/home')
def home():
    return {"Data": "Hello World! 1st Fast API"}
