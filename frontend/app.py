import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume–JD Matcher", layout="wide")
st.title("AI Resume–JD Matcher")

# --- Upload Resume ---
st.header("Step 1: Upload Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

resume_text = ""
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    resume_resp = requests.post(f"{API_URL}/upload_resume", files={"file": uploaded_file})
    if resume_resp.status_code == 200:
        resume_json = resume_resp.json()
        resume_text = resume_json.get("full_text", "")
        st.success("Resume uploaded successfully!")
        st.text_area("Extracted Resume Text", resume_text[:1000], height=200)
    else:
        st.error("Error uploading resume.")

# --- Submit Job Description ---
st.header("Step 2: Paste Job Description")
jd_text = st.text_area("Paste the JD here")

jd_cleaned_text = ""
if st.button("Submit JD"):
    jd_resp = requests.post(f"{API_URL}/submit_jd", data={"jd_text": jd_text})
    if jd_resp.status_code == 200:
        jd_json = jd_resp.json()
        jd_cleaned_text = jd_json.get("full_text", "")
        st.success("Job description submitted successfully!")
        st.text_area("Cleaned JD Text", jd_cleaned_text[:1000], height=200)
    else:
        st.error("Error submitting JD.")

# --- Match Resume & JD ---
st.header("Step 3: Match Resume and JD")
if st.button("Match Now"):
    if not resume_text or not jd_text:
        st.error("Please upload resume and submit JD first.")
    else:
        match_resp = requests.post(
            f"{API_URL}/match",
            data={"resume_text": resume_text, "jd_text": jd_text}
        )
        if match_resp.status_code == 200:
            match_json = match_resp.json()
            score = match_json.get("match_score", 0)
            missing_skills = match_json.get("missing_skills", [])
            st.metric("Match Score", f"{score:.2f}")
            st.subheader("Missing Skills")
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.write("No major missing skills found!")
        else:
            st.error("Error matching resume and JD.")
