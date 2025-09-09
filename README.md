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

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* `pip` and `venv`

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Achal13jain/AI_resume_matcher.git]
    cd ai-resume-matcher
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

You'll need to run the backend and frontend in separate terminal windows.

1.  **Start the FastAPI Backend:**
    ```bash
    uvicorn backend.main:app --reload
    ```
    The backend API will be available at `http://127.0.0.1:8000`. You can see the auto-generated documentation at `http://127.0.0.1:8000/docs`.

2.  **Launch the Streamlit Frontend:**
    ```bash
    streamlit run frontend/app.py
    ```
    The user interface will be accessible in your browser at `http://localhost:8501`.

---

## 📋 API Endpoints

The FastAPI backend provides the following endpoints, which are defined in `backend/main.py`:

* `POST /upload_resume`: Accepts a resume file (`.pdf` or `.docx`), extracts the text, and returns it.
* `POST /submit_jd`: Accepts raw job description text, cleans it, and returns the cleaned text.
* `POST /extract_skills`: Accepts raw text and returns a categorized list of skills found within it.
* `POST /match`: The core endpoint that performs the analysis between a resume and a job description.

You can test these endpoints using tools like Postman or the built-in Swagger UI at `/docs`.

---

## 💡 How It Works

1.  **Parsing**: The `backend/utils.py` module extracts raw text from the uploaded resume (PDF/DOCX) and the pasted job description.
2.  **Skill Extraction**: The `backend/skills.py` module uses NLP techniques to identify and categorize skills into `technical`, `tools`, and `soft_skills` from both texts.
3.  **Embedding**: In `backend/nlp_utils.py`, the `all-MiniLM-L6-v2` model converts both the resume and JD text into high-dimensional numerical vectors (embeddings) that capture semantic meaning.
4.  **Similarity Score**: The **cosine similarity** is calculated between the two vectors to produce a score representing how well they match. A higher score means a better match.
    The formula for Cosine Similarity is:
    
    score=cos(θ)= ∥A∥∥B∥/
                    A⋅B
    
    Where:  
    A and B are the vector representations (embeddings) of the two texts.
    A · B is the dot product of the vectors.
    ||A|| and ||B|| are the magnitudes (or norms) of the vectors.
6.  **Gap Analysis**: The extracted skill sets are compared to generate a list of missing skills, which are then ranked based on their frequency in the job description to determine importance. The final payload provides a comprehensive analysis of the match.
