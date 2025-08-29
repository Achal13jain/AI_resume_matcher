# AI Resume–JD Matcher (Day 1 Starter)

Minimal scaffold for the project. Follow these steps locally:

## 1) Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Run the backend (FastAPI)
```bash
uvicorn backend.main:app --reload --port 8000
```
Open http://127.0.0.1:8000/health — you should see: `{"status":"ok"}`.

## 4) Run the frontend (Streamlit)
In a new terminal (with the same venv activated):
```bash
streamlit run frontend/app.py
```

## 5) Initialize Git and push (optional)
```bash
git init
git add .
git commit -m "chore: day1 setup scaffold"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```

You're ready for Day 2 (parsing).