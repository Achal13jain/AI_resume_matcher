# backend/main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from backend.utils import get_text_from_file, clean_text
from backend.nlp_utils import compute_similarity, get_missing_skills
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


@app.post("/match")
async def match(resume_text: str = Form(...), jd_text: str = Form(...)):
    score = compute_similarity(resume_text, jd_text)
    missing = get_missing_skills(resume_text, jd_text)
    return {
        "match_score": score,
        "missing_skills": missing
    }