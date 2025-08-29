# backend/skills.py
import re
from typing import Dict, List
import spacy

nlp = spacy.load("en_core_web_sm")

# a compact vocabulary to start — extend as you like
TECHNICAL = [
    "python","java","c++","c#","javascript","typescript","sql","nosql",
    "machine learning","deep learning","nlp","computer vision","pandas","numpy",
    "scikit-learn","pytorch","tensorflow","fastapi","flask","django"
]

TOOLS = [
    "git","github","gitlab","docker","kubernetes","aws","gcp","azure",
    "postgresql","mysql","mongodb","redis","streamlit","postman","jira"
]

SOFT = [
    "communication","teamwork","leadership","problem solving","adaptability",
    "time management","collaboration","presentation"
]


def _normalize_text(text: str) -> str:
    # lowercase and keep alphanumerics and common symbols
    return re.sub(r"[^a-z0-9\+\#\-\s]", " ", text.lower())


def _find_terms(text: str, terms: List[str]) -> List[str]:
    t = _normalize_text(text)
    found = []
    for term in terms:
        # normalize term for matching
        term_norm = re.sub(r"[^a-z0-9\+\#\-\s]", " ", term.lower()).strip()
        if not term_norm:
            continue
        # use word-boundary-like matching by surrounding spaces
        if (" " + term_norm + " ") in (" " + t + " "):
            found.append(term)
        else:
            # fallback: check phrase tokens present
            tokens = term_norm.split()
            if all(tok in t.split() for tok in tokens):
                found.append(term)
    return sorted(set(found))


def extract_skills_categorized(text: str) -> Dict[str, List[str]]:
    """
    Returns dict: {"technical": [...], "tools":[...], "soft":[...], "other_phrases":[...]}
    """
    technical = _find_terms(text, TECHNICAL)
    tools = _find_terms(text, TOOLS)
    soft = _find_terms(text, SOFT)

    # try to extract other candidate phrases (noun-chunks) for additional skills
    doc = nlp(text)
    phrases = set()
    for nc in doc.noun_chunks:
        candidate = nc.text.strip().lower()
        # keep short useful phrases
        if 2 <= len(candidate.split()) <= 4 and len(candidate) < 40:
            phrases.add(candidate)

    # remove ones already recognized
    others = [p for p in sorted(phrases) if p not in technical and p not in tools and p not in soft]

    return {
        "technical": technical,
        "tools": tools,
        "soft_skills": soft,
        "other_phrases": others[:40]  # limit returned count
    }


def rank_missing_skills(resume_text: str, jd_text: str):
    """
    Returns a list of dicts: [{"skill": "Docker", "count_in_jd": 3}, ...]
    Ordered by frequency in JD (desc).
    """
    resume = extract_skills_categorized(resume_text)
    jd = extract_skills_categorized(jd_text)

    resume_set = set(resume["technical"] + resume["tools"] + resume["soft_skills"])
    jd_set = set(jd["technical"] + jd["tools"] + jd["soft_skills"])

    missing = jd_set - resume_set

    counts = []
    text_norm = _normalize_text(jd_text)
    for m in missing:
        m_norm = re.sub(r"[^a-z0-9\+\#\-\s]", " ", m.lower()).strip()
        # count occurrences (simple)
        cnt = len(re.findall(r"\b" + re.escape(m_norm) + r"\b", text_norm))
        counts.append({"skill": m, "count_in_jd": cnt})

    # sort by frequency desc then alphabetically
    counts_sorted = sorted(counts, key=lambda x: (-x["count_in_jd"], x["skill"]))
    return counts_sorted
