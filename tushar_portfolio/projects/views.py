from django.shortcuts import render

def projects_view(request):
    projects = [
        {
            'name': 'Tushar Portfolio',
            'desc': 'My personal portfolio website showcasing my projects, skills, and experience.',
            'url': 'https://github.com/tushar-kumar-9354/tushar_portfolio',
            'lang': 'HTML, CSS, JavaScript, Django',
            'live': 'https://tushar-portfolio-1.onrender.com/'
        },
        {
            'name': 'ASTRO-GPT',
            'desc': 'Interactive space exploration tool with AI-generated information about celestial bodies.',
            'url': 'https://github.com/tushar-kumar-9354/ASTRO-GPT',
            'lang': 'Python, Three.js, Django, Gemini API',
            'live': 'https://astro-gpt-2.onrender.com/'
        },
        {
            'name': 'Resume Optimizer',
            'desc': 'AI-powered tool that analyzes and optimizes resumes for better job prospects.',
            'url': 'https://github.com/tushar-kumar-9354/resume_optimizer',
            'lang': 'Python, Django, Gemini API',
            'live': 'https://resume-optimizer-fcod.onrender.com/'
        },
        {
            'name': 'Complaint Registration System',
            'desc': 'Web application for registering and tracking complaints or service requests.',
            'url': 'https://github.com/tushar-kumar-9354/complaint_registration',
            'lang': 'Python, Django, PostgreSQL',
            'live': ''
        },
        {
            'name': 'PYTHON MASTERY',
            'desc': 'Collection of Python scripts and projects demonstrating advanced Python concepts.',
            'url': 'https://github.com/tushar-kumar-9354/...PYTHON_MASTERY...',
            'lang': 'Python',
            'live': 'https://python-mastery.onrender.com/'
        },
        {
            'name': 'AI Agent Workspace',
            'desc': 'Platform for building and testing AI agents with various capabilities.',
            'url': 'https://github.com/tushar-kumar-9354/ai-agent-workspace',
            'lang': 'Python, LangChain, OpenAI API',
            'live': ''
        },
        
        {
            'name': 'Auto News Summarizer',
            'desc': 'Automated system that collects and summarizes news articles using AI.',
            'url': 'https://github.com/tushar-kumar-9354/auto_news_summarizer',
            'lang': 'Python, BeautifulSoup, NLP',
            'live': ''
        },
        {
            'name': 'PDF to Quiz Generator',
            'desc': 'Converts educational PDF content into interactive quizzes automatically.',
            'url': 'https://github.com/tushar-kumar-9354/pdf_to_quiz',
            'lang': 'Python, PyPDF2, Gemini API',
            'live': ''
        },
        {
            'name': 'GEN AI HUB',
            'desc': 'Centralized platform for various generative AI tools and applications.',
            'url': 'https://github.com/tushar-kumar-9354/GEN_AI_HUB',
            'lang': 'Python, Django, Various AI APIs',
            'live': ''
        },
        {
            'name': 'Voice Assistant',
            'desc': 'Customizable voice-controlled assistant for desktop automation.',
            'url': 'https://github.com/tushar-kumar-9354/Voice_assistant',
            'lang': 'Python, SpeechRecognition, pyttsx3',
            'live': ''
        },
        {
            'name': 'Chat Zone',
            'desc': 'Real-time chat application with multiple rooms and user authentication.',
            'url': 'https://github.com/tushar-kumar-9354/chat-zone',
            'lang': 'JavaScript, Node.js, Socket.io',
            'live': ''
        }
    ]
    return render(request, 'projects.html', {'projects': projects})