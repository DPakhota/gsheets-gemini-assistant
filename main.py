from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import google.generativeai as genai
import os

# ← ИСПРАВЛЕНО: Укажи версию API v1
genai.configure(api_key=os.getenv("GEMINI_API_KEY"), api_version="v1")
model = genai.GenerativeModel("gemini-1.5-flash-latest")  # ← Правильная модель

app = FastAPI()

@app.get("/lesson", response_class=PlainTextResponse)
def generate_lesson(topic: str = "Python"):
    prompt = f"Lesson plan for {topic}. CSV: Title|Objective|Duration|Materials|Steps|MCQ1|MCQ2|MCQ3|MCQ4|MCQ5"
    try:
        resp = model.generate_content(prompt)
        return resp.text.strip().replace("\n", " ")
    except Exception as e:
        return "Python Intro|Learn basics|60 min|PC|Step1|Q1|Q2|Q3|Q4|Q5"