from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

@app.get("/lesson", response_class=PlainTextResponse)
def generate_lesson(topic: str):
    prompt = f"""
    Create a lesson plan for: {topic}
    Output in CSV format (no headers, one line):
    Title,Objective,Duration,Materials,Steps,"MCQ1: A) B) C) D) Answer: A"
    """
    resp = model.generate_content(prompt)
    return resp.text.strip()