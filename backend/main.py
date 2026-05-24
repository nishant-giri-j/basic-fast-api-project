from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_AP_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

app = FastAPI()

origins = [
    "http://localhost:5173",  # Common React/Vue dev port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed origins
    allow_credentials=True,           # Allow cookies/auth headers
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], 
)
class PromptRequest(BaseModel):
    prompt: str
    

@app.get("/")
def home():
    return {"message": "welcome to HOMEC PAGE"}

@app.post("/generate")
def generate_text(request: PromptRequest):

    response = model.generate_content(request.prompt)
    return {
        "response": response.text
    }