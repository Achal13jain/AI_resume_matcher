# backend/utils.py
import io
import re
from typing import Optional
from docx import Document
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text as pdfminer_extract


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Try pdfminer first, fall back to PyPDF2."""
    text = ""
    try:
        text = pdfminer_extract(io.BytesIO(file_bytes))
    except Exception:
        pass

    if not text.strip():
        try:
            reader = PdfReader(io.BytesIO(file_bytes))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception:
            text = ""
    return text


def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join(p.text for p in doc.paragraphs)


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def get_text_from_file(filename: str, file_bytes: bytes) -> str:
    fname = filename.lower()
    if fname.endswith(".pdf"):
        return clean_text(extract_text_from_pdf(file_bytes))
    if fname.endswith(".docx") or fname.endswith(".doc"):
        return clean_text(extract_text_from_docx(file_bytes))
    # plain text fallback
    try:
        return clean_text(file_bytes.decode("utf-8"))
    except Exception:
        return ""
