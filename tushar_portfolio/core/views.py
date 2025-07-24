import os
import json
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
from .utils import extract_resume_text 
print("THIS IS MY ASK_ASSISTANT.PY 00")

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
from .utils import extract_resume_text, read_personality

@csrf_exempt
def ask_assistant(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user_input = body.get("message", "")

        resume_text = extract_resume_text()  # ✅ NO ARGUMENTS
        read_personality_text = read_personality()  # ✅ NO ARGUMENTS

        # Build prompt
        prompt = f"""
You are Tushar’s personal AI assistant, embedded in his portfolio.

Here’s the context:
Resume:
\"\"\"
{resume_text}
\"\"\"

Personality:
\"\"\"
{read_personality_text}
\"\"\"

Now respond helpfully to this user message:
"{user_input}"

If the question is about his resume (skills, experience, education), answer from the resume.
If the question is about his personality (behavior, nature, mindset), use the personality info.
If the question is general or technical, respond using your own knowledge.
"""

        try:
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})
