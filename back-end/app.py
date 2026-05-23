from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# MODEL
model = genai.GenerativeModel("gemini-2.5-flash")

# REQUEST MODEL
class ProjectData(BaseModel):
    description: str

@app.get("/")
def home():
    return {"message": "Backend working"}

@app.post("/analyze")
async def analyze_project(data: ProjectData):

    try:

        prompt = f"""
        Analyze this software project.

        Project:
        {data.description}

        Return ONLY in this JSON format:

        {{
            "methodology": "",
            "risk_level": "",
            "recommended_team": "",
            "reason": ""
        }}
        """

        response = model.generate_content(prompt)
        import json

        clean_text = response.text.replace("```json", "").replace("```", "")

        parsed = json.loads(clean_text)

        return parsed
    
       

    except Exception as e:

        return {
            "error": str(e)
        }