from fastapi import FastAPI
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")  # ← ЭТА МОДЕЛЬ РАБОТАЕТ

app = FastAPI(title="Google Sheets AI Assistant")

@app.get("/lesson")
def generate_lesson(topic: str):
    prompt = f"""
    Create a lesson plan for: {topic}
    Output in CSV format (no headers):
    Title,Objective,Duration,Materials,Steps,5 MCQ

    Example:
    Python Basics,Learn variables and loops,60 min,Computer,1. Print,2. Variables,3. Loops,What is print()?,A) Loop,B) Output,C) Input,D) Error,Answer: B
    """
    resp = model.generate_content(prompt)
    return JSONResponse(content={"csv": resp.text})