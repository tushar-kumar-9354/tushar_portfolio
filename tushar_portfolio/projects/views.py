from django.shortcuts import render

def projects(request):
    projects = [
        {
            'name': 'AI Resume Optimizer',
            'desc': 'Analyzes your resume, finds missing skills, and generates coding challenges & project ideas using GenAI.',
            'url': 'https://github.com/tushar-kumar-9354/ai_resume_optimizer',
            'lang': 'Python, Django, Gemini API',
            'live': 'https://resume-ai.onrender.com'
        },
        {
            'name': 'AstroGPT – Space Simulator',
            'desc': 'Visualize orbits of planets, get Gemini-powered facts on hover, built with Three.js and Django.',
            'url': 'https://github.com/tushar-kumar-9354/astroGPT',
            'lang': 'Three.js, Django, Gemini API',
            'live': 'https://astro-gpt.onrender.com'
        },
        {
            'name': 'Tushar Portfolio',
            'desc': 'A modern personal portfolio showcasing skills, GitHub projects, animations, and contact form.',
            'url': 'https://github.com/tushar-kumar-9354/tushar_portfolio',
            'lang': 'HTML, TailwindCSS, Django',
            'live': ''
        },
        {
            'name': 'Auto-News Summarizer',
            'desc': 'Scrapes news, summarizes them using GenAI, tracks sentiment and generates a CSV report.',
            'url': 'https://github.com/tushar-kumar-9354/news_summarizer',
            'lang': 'Python, Selenium, Gemini API',
            'live': ''
        },
        {
            'name': 'AI Kisan Mitra (KrishiGPT)',
            'desc': 'Offline voice chatbot for farmers in Bhojpuri/Maithili using Django, Vosk & GenAI.',
            'url': 'https://github.com/tushar-kumar-9354/krishiGPT',
            'lang': 'Python, Django, Vosk, gTTS',
            'live': ''
        },
    ]
    return render(request, 'project.html', {'projects': projects})
