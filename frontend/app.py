import streamlit as st
import requests
import pandas as pd
from textwrap import shorten

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume–JD Matcher", layout="wide")

# Sidebar navigation (Home / Resume Parser)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📄 Resume Parser"])

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.title("Welcome to AI Resume–JD Matcher")
    st.markdown("""
    ### 🚀 What this app does
    - Upload your **resume** 📄  
    - Paste a **job description (JD)** 📝  
    - See **skill categorization** (Technical / Tools / Soft skills)  
    - Get **semantic matching scores** & missing skills 🔍  
    - Compare results with both **rule-based** and **LLM-based analysis** 🤖  

    ---
    ### 💡 Why use this tool?
    - Quickly tailor your resume for a job  
    - Identify missing skills  
    - Benchmark with AI-powered semantic matching  

    ---
    👉 Use the **sidebar** to navigate to the Resume Parser page.
    """)

# ---------------- RESUME PARSER PAGE ----------------
elif page == "📄 Resume Parser":
    st.title("AI Resume–JD Matcher")
    st.write("Upload resume, paste JD — see categorized skills and what’s missing.")

    # --- Upload Resume ---
    st.header("1) Upload Resume")
    uploaded_file = st.file_uploader("Upload resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    resume_text = ""
    if uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        resp = requests.post(f"{API_URL}/upload_resume", files={"file": uploaded_file})
        if resp.status_code == 200:
            resume_text = resp.json().get("full_text", "")
            st.success("Resume parsed.")
            st.expander("Preview extracted resume text", expanded=False).write(shorten(resume_text, width=1000, placeholder="..."))
            sk_resp = requests.post(f"{API_URL}/extract_skills", json={"text": resume_text})
            resume_skills = sk_resp.json() if sk_resp.status_code == 200 else {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}
        else:
            st.error("Failed to upload/parse resume.")
            resume_skills = {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}
    else:
        resume_skills = {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}

    # --- Paste JD ---
    st.header("2) Paste Job Description")
    jd_text = st.text_area("Paste JD here (or leave blank to test)", height=220)
    jd_clean = ""
    if st.button("Extract JD & Skills"):
        if not jd_text.strip():
            st.error("Paste a job description first.")
        else:
            jd_resp = requests.post(f"{API_URL}/submit_jd", data={"jd_text": jd_text})
            if jd_resp.status_code == 200:
                jd_clean = jd_resp.json().get("full_text", "")
                st.success("JD accepted.")
                st.expander("Preview cleaned JD text", expanded=False).write(shorten(jd_clean, width=1000, placeholder="..."))
                sk_resp = requests.post(f"{API_URL}/extract_skills", json={"text": jd_clean})
                jd_skills = sk_resp.json() if sk_resp.status_code == 200 else {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}
            else:
                st.error("Failed to submit JD.")
                jd_skills = {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}
    else:
        jd_skills = {"technical": [], "tools": [], "soft_skills": [], "other_phrases": []}

    # Show categorized skills
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Resume: Detected skills")
        with st.expander("Technical"):
            st.write(resume_skills.get("technical", []))
        with st.expander("Tools"):
            st.write(resume_skills.get("tools", []))
        with st.expander("Soft skills"):
            st.write(resume_skills.get("soft_skills", []))

    with col2:
        st.subheader("JD: Detected skills")
        with st.expander("Technical"):
            st.write(jd_skills.get("technical", []))
        with st.expander("Tools"):
            st.write(jd_skills.get("tools", []))
        with st.expander("Soft skills"):
            st.write(jd_skills.get("soft_skills", []))

    # --- Match and show overlap chart ---
    st.header("3) Match & Analyze")
    if st.button("Match Now"):
        if not resume_text:
            st.error("Please upload a resume first.")
        elif not jd_text.strip():
            st.error("Please paste a job description.")
        else:
            match_resp = requests.post(f"{API_URL}/match", data={"resume_text": resume_text, "jd_text": jd_text})
            if match_resp.status_code == 200:
                res = match_resp.json()
                score = res.get("match_score", 0)
                st.metric("Semantic match score (approx)", f"{score:.2f}")

                resume_count = res.get("resume_skill_count", 0)
                jd_count = res.get("jd_skill_count", 0)
                overlap = res.get("overlap_count", 0)

                st.subheader("Skill overlap (counts)")
                df = pd.DataFrame({
                    "Metric": ["Resume skills", "JD skills", "Matched (intersection)"],
                    "Count": [resume_count, jd_count, overlap]
                }).set_index("Metric")
                st.table(df)
                st.bar_chart(df)

                st.subheader("Top missing skills (from JD but not in resume)")
                ranked = res.get("ranked_missing_skills", [])
                if ranked:
                    st.table(pd.DataFrame(ranked).head(10))
                else:
                    st.write("No missing skills detected.")


                st.subheader("Raw missing_skills list")
                st.write(res.get("missing_skills", []))
            else:
                st.error("Matching failed. See backend logs.")

    # --- LLM-based extraction and match ---
    st.header("4) LLM-based Match & Analysis")
    if st.button("Run LLM-based Match"):
        if not resume_text:
            st.error("Please upload a resume first.")
        elif not jd_text.strip():
            st.error("Please paste a job description.")
        else:
            llm_resp = requests.post(f"{API_URL}/llm_extract_and_match", data={"resume_text": resume_text, "jd_text": jd_text})
            if llm_resp.status_code == 200:
                res = llm_resp.json()
                st.metric("LLM Overlap Count", res.get("overlap_count", 0))

                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Resume (LLM Skills)")
                    st.write(res.get("resume_skills", []))

                with col2:
                    st.subheader("JD (LLM Skills)")
                    st.write(res.get("jd_skills", []))

                st.subheader("Matched Skills ✅")
                st.write(res.get("matched_skills", []))

                st.subheader("Missing Skills ❌")
                st.write(res.get("missing_skills", []))
            else:
                st.error("LLM-based matching failed. See backend logs.")
