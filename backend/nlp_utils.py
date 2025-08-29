# backend/nlp_utils.py
from sentence_transformers import SentenceTransformer, util
import spacy
import re

# Load model once
embedder = SentenceTransformer("all-MiniLM-L6-v2")
nlp = spacy.load("en_core_web_sm")

def get_embedding(text: str):
    return embedder.encode(text, convert_to_tensor=True)

def compute_similarity(resume_text: str, jd_text: str) -> float:
    emb_resume = get_embedding(resume_text)
    emb_jd = get_embedding(jd_text)
    score = util.cos_sim(emb_resume, emb_jd).item()
    return round(score * 100, 2)  # percentage

def extract_skills(text: str):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if token.is_alpha]
    common_skills = [
        "python", "java", "c++", "html", "css", "javascript",
        "fastapi", "react", "sql", "postgresql", "mysql",
        "machine learning", "deep learning", "nlp", "data science",
        "git", "github", "docker", "aws", "streamlit"
    ]
    found = []
    for skill in common_skills:
        pattern = re.compile(r"\b" + re.escape(skill) + r"\b", re.IGNORECASE)
        if pattern.search(text):
            found.append(skill)
    return list(set(found))

def get_missing_skills(resume_text: str, jd_text: str):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    return list(jd_skills - resume_skills)
