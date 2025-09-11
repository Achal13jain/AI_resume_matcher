# AI Resume & Job Description Matcher

A powerful tool built with **FastAPI** and **Streamlit** to analyze how well a resume matches a job description.  
It calculates a similarity score, identifies missing skills, and now also leverages **LLMs** (Large Language Models) for more accurate skill extraction and overlap analysis.  

---

## ✨ Features

- **Resume Upload**: Supports both **PDF** and **DOCX** file formats for easy resume submission.  
- **Job Description Input**: A simple text area to paste the job description you're interested in.  
- **AI-Powered Matching (Embeddings)**: Uses **sentence-transformers** to compute a cosine similarity score between the resume and the JD.  
- **LLM-Powered Skill Extraction**: Uses a connected LLM (via API) to extract **clean, domain-specific skills** from both resumes and JDs.  
- **Skill Gap Analysis**: Identifies and lists the crucial skills mentioned in the job description that are missing from the resume.  
- **Overlap Analysis**: Combines LLM and traditional methods to highlight **matched skills, missing skills, and overlap counts**.  
- **Interactive UI**: A clean and user-friendly interface built with Streamlit for a seamless experience.  

---

## 🛠️ Tech Stack & Tools

- **Backend**: FastAPI, Uvicorn  
- **Frontend**: Streamlit  
- **NLP / Embeddings**: HuggingFace **sentence-transformers** (`all-MiniLM-L6-v2` model)  
- **LLM Integration**: Free OpenAI API from OpenRouter.ai (configurable via `.env`)  
- **File Parsing**: PyPDF2, python-docx  
- **Core**: Python 3.x  

---

## 📂 Project Structure

```
├── .github/
├── .venv/
├── backend/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── main.py
│   ├── nlp_utils.py
│   ├── skills.py
│   └── utils.py
├── frontend/
│   └── app.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+  
- pip and venv  
- An OpenAI API key (for LLM skill extraction)  

### Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Achal13jain/AI_resume_matcher.git
cd ai-resume-matcher
```

2. **Create and activate a Python virtual environment:**

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Setup environment variables (`.env` file):**

Create a `.env` file in the root directory with:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### Running the Application

You'll need to run the backend and frontend in separate terminal windows.

1. **Start the FastAPI Backend:**

```bash
uvicorn backend.main:app --reload
```

The backend API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).  
You can explore API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).  

2. **Launch the Streamlit Frontend:**

```bash
streamlit run frontend/app.py
```

The UI will be accessible in your browser at [http://localhost:8501](http://localhost:8501).  

---

## 📋 API Endpoints

The FastAPI backend provides the following endpoints:

- `POST /upload_resume`: Accepts a resume file (.pdf or .docx), extracts the text, and returns it.  
- `POST /submit_jd`: Accepts raw job description text, cleans it, and returns the cleaned text.  
- `POST /extract_skills`: Extracts skills using traditional NLP methods.   
* `POST /match`: The core endpoint that performs the analysis between a resume and a job description.
- `POST /llm_extract_and_match`: Combines LLM skill extraction with overlap analysis (matched, missing, and counts).  

---

## 💡 How It Works

1. **Parsing**  
   - `utils.py` extracts raw text from uploaded resumes (PDF/DOCX) and JDs.  

2. **Traditional Skill Extraction**  
   - `skills.py` uses NLP + regex lists to identify technical, tool-based, and soft skills.  

3. **LLM Skill Extraction**  
   - `extract_skills_with_llm()` sends text to an LLM (via API) and returns a **clean, comma-separated skill list**.  

4. **Embedding-based Similarity**  
   - `nlp_utils.py` uses `all-MiniLM-L6-v2` to generate embeddings for both texts.  
   - Cosine similarity is computed:  

    score=cos(θ)= ∥A∥∥B∥/
                    A⋅B 

   where **A** and **B** are embeddings of resume and JD.  

5. **Overlap & Gap Analysis**  
   - The system compares **resume skills vs JD skills**.  
   - Results include:  
     - ✅ Matched skills  
     - ⚠️ Missing skills  
     - 📊 Overlap counts (resume, JD, match)  

