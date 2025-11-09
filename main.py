from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI(title="Google Sheets AI Assistant")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Google Sheets AI Lesson Assistant</h1>
    <p>Use: <code>/lesson?topic=Python</code></p>
    <p><a href="/docs">Open Swagger UI</a></p>
    """

@app.get("/lesson")
def generate_lesson(topic: str):
    prompt = f"""
    Create a lesson plan for: {topic}
    Output in CSV format (no headers):
    Title,Objective,Duration,Materials,Steps,5 MCQ with answers
    """
    resp = model.generate_content(prompt)
    return JSONResponse(content={"csv": resp.text})