import os
import json
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
from .utils import extract_resume_text 
print("THIS IS MY ASK_ASSISTANT.PY 00")

load_dotenv()

print("--"*50)
genai.configure(api_key="AIzaSyD5QuAAmVq-Dt-LF06bV_8cK1GIJj7d2-M")

print("THIS IS MY ASK_ASSISTANT.PY 01")
from .utils import extract_resume_text, read_personality

@csrf_exempt
def ask_assistant(request):
    print("ask assistant")
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
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            print( "-"*50)
            print("THIS IS MY ASK_ASSISTANT.PY response", response)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})
