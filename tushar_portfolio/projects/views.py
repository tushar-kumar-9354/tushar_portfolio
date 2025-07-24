import requests
from django.shortcuts import render

def projects_view(request):
    try:
        resp = requests.get(
            "https://api.github.com/users/tushar-kumar-9354/repos",
            params={"per_page": 12, "sort": "pushed"},
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=5  # Optional: to avoid hanging
        )
        if resp.status_code == 200:
            repos = resp.json()
        else:
            repos = []
    except Exception as e:
        print(f"Error fetching GitHub projects: {e}")
        repos = []

    # Filter and transform
    projects = [
        {
            "name": r.get("name", ""),
            "desc": r.get("description", ""),
            "url": r.get("html_url", "#"),
            "live": r.get("homepage", ""),
            "lang": r.get("language", ""),
        }
        for r in repos
        if not r.get("fork", False)
    ]

    # Optional: Fallback project if empty (helps in production)
    if not projects:
        projects = [{
            "name": "Demo Project",
            "desc": "Fallback demo project in case GitHub API fails.",
            "url": "https://github.com/tushar-kumar-9354",
            "live": "",
            "lang": "Python"
        }]

    return render(request, "projects.html", {"projects": projects})
