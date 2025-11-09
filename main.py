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
    Create a lesson plan for: {topic}
    Output in CSV format, one line, no headers, no quotes:
    Title,Objective,Duration,Materials,Steps,MCQ1,MCQ2,MCQ3,MCQ4,MCQ5
    """
    try:
        resp = model.generate_content(prompt)
        # Возвращаем только текст, без JSON
        return resp.text.strip()
    except Exception as e:
        return f"Error,{str(e)}"