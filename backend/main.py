# backend/main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from backend.utils import get_text_from_file, clean_text
from backend.nlp_utils import compute_similarity, get_missing_skills
from backend.skills import extract_skills_categorized, rank_missing_skills

app = FastAPI(title="AI Resume–JD Matcher")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = get_text_from_file(file.filename, content)
    if not text:
        return JSONResponse({"error": "Could not extract text"}, status_code=400)
    return {"filename": file.filename, "text_snippet": text[:500], "full_text": text}


@app.post("/submit_jd")
async def submit_jd(jd_text: str = Form(...)):
    text = clean_text(jd_text)
    if not text:
        return JSONResponse({"error": "Empty JD"}, status_code=400)
    return {"jd_snippet": text[:500], "full_text": text}


class TextIn(BaseModel):
    text: str


@app.post("/extract_skills")
async def extract_skills_endpoint(payload: TextIn):
    text = payload.text or ""
    if not text.strip():
        return JSONResponse({"error": "Empty text"}, status_code=400)
    categorized = extract_skills_categorized(text)
    return categorized


@app.post("/match")
async def match(resume_text: str = Form(...), jd_text: str = Form(...)):
    # existing similarity
    score = compute_similarity(resume_text, jd_text)
    missing = get_missing_skills(resume_text, jd_text)

    # new skill categorization and overlap metrics
    resume_sk = extract_skills_categorized(resume_text)
    jd_sk = extract_skills_categorized(jd_text)

    resume_set = set(resume_sk["technical"] + resume_sk["tools"] + resume_sk["soft_skills"])
    jd_set = set(jd_sk["technical"] + jd_sk["tools"] + jd_sk["soft_skills"])
    overlap = resume_set.intersection(jd_set)

    # ranked missing skills by frequency in JD
    ranked_missing = rank_missing_skills(resume_text, jd_text)

    return {
        "match_score": score,
        "missing_skills": missing,
        "ranked_missing_skills": ranked_missing,
        "resume_skills": resume_sk,
        "jd_skills": jd_sk,
        "overlap_count": len(overlap),
        "resume_skill_count": len(resume_set),
        "jd_skill_count": len(jd_set),
    }
