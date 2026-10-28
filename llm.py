import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-3.5-flash-lite"

SYSTEM_PROMPT = "You are a summarizer. Summarize the text in 3 short bullet points."

def summarize(text: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=text,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )
    return response.text

def translate(text: str , language: str) -> str:
    prompt=f"Translate the user's text into {language}. Reply with only the translation."
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=text,
        config=types.GenerateContentConfig(system_instruction=prompt),

    )
    return response.text

EXTRACT_PROMPT = EXTRACT_PROMPT = """Extract information from the job post.
Reply ONLY with JSON in exactly this format:
{"title": "...", "company": "...", "location": "...", "skills": ["...", "..."]}
If something is missing, use null (use [] for skills)."""

def extract_job(text:str) -> dict:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=text,
        config=types.GenerateContentConfig(system_instruction=EXTRACT_PROMPT,response_mime_type="application/json",),
        )
    return json.loads(response.text)

    


# if __name__ == "__main__":
#     print(summarize("Python is a popular programming language. It is used for web development, data science, automation, and AI. It is known for readable code and a large community of libraries."))
#     print(translate("How are you today?", "Nepali"))
#     print(extract_job("Acme Software is hiring a Backend Python Developer in Kathmandu. You will build REST APIs with FastAPI and PostgreSQL. Experience with Docker is a plus."))
