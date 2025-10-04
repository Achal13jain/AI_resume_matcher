# AI Resume & Job Description Matcher

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/Achal13jain/AI_resume_matcher/workflows/CI/badge.svg)

**Intelligent resume analysis powered by AI to help job seekers optimize their applications**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Development](#%E2%80%8D-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 🎯 Overview

**AI Resume & Job Description Matcher** is a sophisticated tool that leverages natural language processing (NLP) and large language models (LLMs) to analyze how well a resume aligns with a job description. It provides actionable insights including similarity scores, skill gap analysis, and personalized recommendations to help candidates optimize their job applications.

### Why This Tool?

- **Save Time**: Quickly identify which jobs match your skillset
- **Get Insights**: Understand exactly what skills you're missing
- **Improve Applications**: Tailor your resume to specific job requirements
- **Data-Driven**: Make informed decisions backed by AI analysis

---

## ✨ Features

### Core Functionality

- 📄 **Multi-Format Resume Support**: Upload resumes in PDF, DOCX, or TXT formats
- 📝 **Job Description Analysis**: Paste any job description for instant analysis
- 🤖 **Dual Analysis Modes**:
  - **Traditional NLP**: Rule-based skill extraction with sentence transformers
  - **LLM-Powered**: Advanced AI analysis using Llama 3.3 for accurate skill identification
- 📊 **Semantic Similarity Scoring**: Cosine similarity calculation using state-of-the-art embeddings
- 🎯 **Skill Gap Analysis**: 
  - Categorized skills (Technical, Tools, Soft Skills)
  - Missing skills identification
  - Ranked missing skills by importance
- 📈 **Visual Analytics**: Interactive charts and metrics for skill overlap
- 🔄 **Real-time Processing**: Instant feedback as you upload and analyze

### Advanced Features

- **Smart Skill Categorization**: Automatically groups skills into meaningful categories
- **Frequency Analysis**: Ranks missing skills based on how often they appear in the JD
- **Overlap Metrics**: Detailed statistics on skill matching between resume and JD
- **Clean UI/UX**: Intuitive Streamlit interface with expandable sections
- **API-First Design**: RESTful API for easy integration with other tools

---

## 🎬 Demo

### Web Interface

![AI Resume Matcher Demo](images/AI-resume%20matcher.png)

![AI Resume Matcher Demo](images/AI-resume%20matcher%201.png)

![AI Resume Matcher Demo](images/AI-resume%20matcher%202.png)
*Upload your resume and paste a job description to see instant analysis*

### Sample Output

```
Semantic Match Score: 78.5%

Skill Overlap:
├── Resume Skills: 24
├── JD Skills: 18
└── Matched: 15

Top Missing Skills:
1. Docker (3 mentions)
2. Kubernetes (2 mentions)
3. AWS (2 mentions)
```

---

## 🛠 Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Python 3.8+** - Core programming language

### Frontend
- **Streamlit** - Interactive web application framework

### AI/ML
- **Sentence Transformers** - State-of-the-art text embeddings (`all-MiniLM-L6-v2`)
- **spaCy** - Industrial-strength NLP library
- **OpenAI API** (via OpenRouter) - LLM integration for advanced skill extraction

### Document Processing
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX document parsing
- **pdfminer.six** - Advanced PDF text extraction

### DevOps
- **Docker** - Containerization (via devcontainer)
- **GitHub Actions** - CI/CD pipeline

---

## 🏗 Architecture

```
┌─────────────────┐
│   Streamlit UI  │
│   (Frontend)    │
└────────┬────────┘
         │ HTTP Requests
         ↓
┌─────────────────┐
│   FastAPI       │
│   (Backend)     │
├─────────────────┤
│ ├─ utils.py     │ ← Document parsing
│ ├─ nlp_utils.py │ ← Embeddings & similarity
│ ├─ skills.py    │ ← Skill extraction
│ └─ llm_utils.py │ ← LLM integration
└────────┬────────┘
         │
         ↓
┌─────────────────────────────┐
│  External Services          │
├─────────────────────────────┤
│ • HuggingFace Models        │
│ • OpenRouter API (LLM)      │
└─────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- OpenRouter API key (for LLM features)

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/Achal13jain/AI_resume_matcher.git
cd AI_resume_matcher
```

2. **Create a virtual environment**

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download spaCy language model**

```bash
python -m spacy download en_core_web_sm
```

5. **Set up environment variables**

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

To get an OpenRouter API key, visit: https://openrouter.ai/

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENROUTER_API_KEY` | API key for OpenRouter LLM service | Yes (for LLM features) | - |

### Model Configuration

The application uses the following models by default:

- **Embeddings**: `all-MiniLM-L6-v2` (Sentence Transformers)
- **LLM**: `meta-llama/llama-3.3-70b-instruct:free` (via OpenRouter)
- **NLP**: `en_core_web_sm` (spaCy)

These can be modified in the respective utility files (`nlp_utils.py`, `llm_utils.py`).

---

## 📖 Usage

### Starting the Application

You need to run both the backend and frontend servers.

#### 1. Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

The backend will be available at: http://127.0.0.1:8000

API documentation (Swagger UI): http://127.0.0.1:8000/docs

#### 2. Launch the Streamlit Frontend

In a new terminal window:

```bash
streamlit run frontend/app.py
```

The UI will open automatically in your browser at: http://localhost:8501

### Using the Web Interface

1. **Navigate to Resume Parser**: Use the sidebar to go to the "📄 Resume Parser" page

2. **Upload Resume**: Click "Upload resume" and select your PDF, DOCX, or TXT file

3. **Paste Job Description**: Copy and paste the job description in the text area

4. **Extract Skills**: Click "Extract JD & Skills" to see categorized skills from both documents

5. **Run Analysis**: 
   - Click "Match Now" for traditional NLP-based analysis
   - Click "Run LLM-based Match" for AI-powered analysis

6. **Review Results**: Examine the similarity score, skill gaps, and recommendations

### Using the API Directly

#### Upload Resume

```bash
curl -X POST "http://127.0.0.1:8000/upload_resume" \
  -F "file=@/path/to/resume.pdf"
```

#### Match Resume with JD

```bash
curl -X POST "http://127.0.0.1:8000/match" \
  -F "resume_text=Your resume text here" \
  -F "jd_text=Job description text here"
```

---

## 📚 API Documentation

### Endpoints

#### `GET /health`

Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

---

#### `POST /upload_resume`

Upload and parse a resume file.

**Parameters:**
- `file` (UploadFile): Resume file (PDF/DOCX/TXT)

**Response:**
```json
{
  "filename": "resume.pdf",
  "text_snippet": "First 500 characters...",
  "full_text": "Complete extracted text"
}
```

---

#### `POST /submit_jd`

Submit and clean job description text.

**Parameters:**
- `jd_text` (Form): Raw job description text

**Response:**
```json
{
  "jd_snippet": "First 500 characters...",
  "full_text": "Complete cleaned text"
}
```

---

#### `POST /extract_skills`

Extract categorized skills from text.

**Request Body:**
```json
{
  "text": "Your text here"
}
```

**Response:**
```json
{
  "technical": ["python", "sql", "machine learning"],
  "tools": ["git", "docker", "aws"],
  "soft_skills": ["communication", "teamwork"],
  "other_phrases": ["data analysis", "project management"]
}
```

---

#### `POST /match`

Perform comprehensive matching analysis.

**Parameters:**
- `resume_text` (Form): Resume text
- `jd_text` (Form): Job description text

**Response:**
```json
{
  "match_score": 78.5,
  "missing_skills": ["docker", "kubernetes"],
  "ranked_missing_skills": [
    {"skill": "docker", "count_in_jd": 3},
    {"skill": "kubernetes", "count_in_jd": 2}
  ],
  "resume_skills": {...},
  "jd_skills": {...},
  "overlap_count": 15,
  "resume_skill_count": 24,
  "jd_skill_count": 18
}
```

---

#### `POST /llm_extract_and_match`

LLM-powered skill extraction and matching.

**Parameters:**
- `resume_text` (Form): Resume text
- `jd_text` (Form): Job description text

**Response:**
```json
{
  "resume_skills": ["Python", "FastAPI", "SQL"],
  "jd_skills": ["Python", "Docker", "AWS"],
  "matched_skills": ["Python"],
  "missing_skills": ["Docker", "AWS"],
  "overlap_count": 1,
  "resume_skill_count": 3,
  "jd_skill_count": 3
}
```

---

## 📁 Project Structure

```
AI_resume_matcher/
├── .devcontainer/
│   └── devcontainer.json       # VS Code devcontainer configuration
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application & routes
│   ├── utils.py                # Document parsing utilities
│   ├── nlp_utils.py            # NLP & embeddings logic
│   ├── skills.py               # Skill extraction & categorization
│   └── llm_utils.py            # LLM integration
├── frontend/
│   └── app.py                  # Streamlit web interface
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

## 👨‍💻 Development

### Setting Up Development Environment

#### Using VS Code Dev Containers

This project includes a devcontainer configuration for a consistent development environment.

1. Install Docker Desktop
2. Install VS Code and the "Dev Containers" extension
3. Open the project in VS Code
4. Click "Reopen in Container" when prompted

#### Manual Setup

Follow the [Installation](#-installation) instructions above.

### Code Style

This project follows PEP 8 guidelines. Please ensure your code is formatted before submitting PRs.

```bash
# Install development tools
pip install black flake8 pylint

# Format code
black backend/ frontend/

# Lint code
flake8 backend/ frontend/
```

### Adding New Skills

To add new skills to the detection system, edit `backend/skills.py`:

```python
TECHNICAL = [
    # Add your technical skills here
    "your_new_skill",
]

TOOLS = [
    # Add your tools here
    "your_new_tool",
]
```

---

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=backend --cov-report=html
```

### Manual Testing

1. Start both servers (backend and frontend)
2. Upload a sample resume
3. Paste a sample job description
4. Verify all features work as expected

---

## 🚢 Deployment

### Docker Deployment (Coming Soon)

```bash
# Build Docker image
docker build -t ai-resume-matcher .

# Run container
docker run -p 8000:8000 -p 8501:8501 ai-resume-matcher
```

### Cloud Deployment

#### Heroku

```bash
heroku create your-app-name
git push heroku main
```

#### AWS / GCP / Azure

Refer to the respective platform documentation for deploying FastAPI and Streamlit applications.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [HuggingFace](https://huggingface.co/) for the sentence-transformers library
- [OpenRouter](https://openrouter.ai/) for LLM API access
- [spaCy](https://spacy.io/) for NLP capabilities
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Streamlit](https://streamlit.io/) for the intuitive UI framework

---

## 📧 Contact

**Achal Jain** - [@Achal13jain](https://github.com/Achal13jain)

Project Link: [https://github.com/Achal13jain/AI_resume_matcher](https://github.com/Achal13jain/AI_resume_matcher)

---

## Future Enhancements
- [ ] Add support for more resume formats (RTF, HTML)
- [ ] Implement resume optimization suggestions
- [ ] Add cover letter generation feature
- [ ] Create browser extension
- [ ] Add support for multiple languages
- [ ] Implement user accounts and history tracking
- [ ] Add ATS (Applicant Tracking System) optimization tips
- [ ] Create mobile application

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made  by [Achal Jain](https://github.com/Achal13jain)

</div>