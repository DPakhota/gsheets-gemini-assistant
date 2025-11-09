from fastapi import FastAPI
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")  # ← ЭТА МОДЕЛЬ РАБОТАЕТ

app = FastAPI(title="Google Sheets AI Assistant")

@app.get("/")
def home():
    return JSONResponse("""
    <h1>Google Sheets AI Lesson Assistant</h1>
    <p>Use: <code>/lesson?topic=Python</code></p>
    <p><a href="/docs">Open Swagger UI</a></p>
    """)

@app.get("/lesson")
def generate_lesson(topic: str):
    prompt = f"""
    Create a lesson plan for: {topic}
    Output in CSV format (no headers):
    Title,Objective,Duration,Materials,Steps,5 MCQ with answers
    """
    resp = model.generate_content(prompt)
    return JSONResponse(content={"csv": resp.text})