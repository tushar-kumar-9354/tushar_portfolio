from django.contrib.staticfiles.storage import staticfiles_storage
import fitz  # PyMuPDF

def extract_resume_text():
    try:

        resume_path = staticfiles_storage.path("resume/TUSHAR_KUMAR_SOFTWARE_DEVELOPER_RESUME.pdf")

        text = ""
        print("this is actucal path",resume_path)
        doc = fitz.open(resume_path)
        for page in doc:
            text += page.get_text()
        print(text)
        return text

    except Exception as e:
        return f"Error loading resume: {e}"
print(extract_resume_text)

def read_personality():
    try:
        personality_path = staticfiles_storage.path("personality/personality.txt")
        with open(personality_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Tushar is a backend developer with a great personality. [DEBUG: {e}]"
