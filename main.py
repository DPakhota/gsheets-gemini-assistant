from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

@app.get("/lesson", response_class=PlainTextResponse)
def generate_lesson(topic: str = "Python"):
    prompt = f"""
    Generate a lesson plan for "{topic}".
    Format as CSV: Title|Objective|Duration|Materials|Steps|MCQ1|MCQ2|MCQ3|MCQ4|MCQ5
    Use | as separator, one line only. Make sure it's exactly 10 fields.
    Example: Intro to Python|Learn basics|60 min|Computer|Step1,Step2,Step3|What is print?|What is variable?|What is loop?|What is function?|What is error?
    """
    try:
        resp = model.generate_content(prompt)
        text = resp.text.strip()
        if len(text.split('|')) < 10:
            text = "Intro to Python|Learn basics|60 min|Computer|Step1,Step2|What is print?|What is variable?|What is loop?|What is function?|What is error?"
        return text
    except Exception as e:
        return f"Error|{str(e)}|60 min|Computer|Step1|Q1|Q2|Q3|Q4|Q5"