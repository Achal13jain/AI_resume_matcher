#  AI Resume & Job Description Matcher

A powerful tool built with FastAPI and Streamlit to analyze how well a resume matches a job description. It calculates a similarity score and identifies key skills missing from the resume.
---

## ✨ Features

* **Resume Upload**: Supports both PDF and DOCX file formats for easy resume submission.
* **Job Description Input**: A simple text area to paste the job description you're interested in.
* **AI-Powered Matching**: Uses `sentence-transformers` to compute a cosine similarity score between the resume and the JD.
* **Skill Gap Analysis**: Identifies and lists the crucial skills mentioned in the job description that are missing from the resume.
* **Interactive UI**: A clean and user-friendly interface built with Streamlit for a seamless experience.

---

## 🛠️ Tech Stack & Tools

* **Backend**: FastAPI, Uvicorn
* **Frontend**: Streamlit
* **NLP / Embeddings**: HuggingFace `sentence-transformers` (`all-MiniLM-L6-v2` model)
* **File Parsing**: `PyPDF2`, `python-docx`
* **Core**: Python 3.x

---

## 📂 Project Structure
    ├── .github/
    ├── .venv/
    ├── backend/
    │   ├── pycache/
    │   ├── init.py
    │   ├── main.py
    │   ├── nlp_utils.py
    │   ├── skills.py
    │   └── utils.py
    ├── frontend/
    │   └── app.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt
