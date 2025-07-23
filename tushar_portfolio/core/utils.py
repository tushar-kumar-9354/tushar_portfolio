# core/utils.py
import fitz  # PyMuPDF
import os

def extract_resume_text(resume_path):
    resume_path = os.path.join("static", "resume", "TUSHAR KUMAR_SOFTWARE_DEVELOPER_RESUME.pdf")
    if not os.path.exists(resume_path):
        return "Resume not found."
    text = ""
    doc = fitz.open(resume_path)
    for page in doc:
        text += page.get_text()
    return text

from django.conf import settings

def read_personality(personality_path):
    personality_path = os.path.join("static", "personality", "personality.txt")
    try:
        with open(personality_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Tushar is a backend developer with a great personality."

