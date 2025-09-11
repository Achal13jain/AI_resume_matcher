import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # from .env
)

def extract_skills_with_llm(text: str, model: str = "meta-llama/llama-3.3-70b-instruct:free"):
    prompt = f"""
    Extract all relevant skills, tools, and technologies from the following text. 
    Respond ONLY in strict JSON format with a key called "skills", like this:
    {{"skills": ["Python", "SQL", "FastAPI"]}}

    Text: {text}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()
    
    try:
        data = json.loads(raw)
        return data
    except:
        skills = [s.strip() for s in raw.replace("\n", ",").split(",") if s.strip()]
        return {"skills": skills}
