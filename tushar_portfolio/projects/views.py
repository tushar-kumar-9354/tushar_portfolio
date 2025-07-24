import requests
from django.shortcuts import render
import requests
from django.http import JsonResponse

def projects_view(request):
    try:
        print("📡 Fetching GitHub repos...")

        resp = requests.get(
            "https://api.github.com/users/tushar-kumar-9354/repos",
            params={"per_page": 12, "sort": "pushed"},
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=5
        )

        print(f"📦 Response Status Code: {resp.status_code}")

        if resp.status_code == 200:
            repos = resp.json()
            print(f"✅ Total repos fetched: {len(repos)}")
        else:
            print("⚠️ GitHub API returned a non-200 response")
            repos = []

    except Exception as e:
        print(f"❌ Error fetching GitHub projects: {e}")
        repos = []

    # Filter out forks and transform into simplified project data
    projects = []
    for r in repos:
        if not r.get("fork", False):
            project_data = {
                "name": r.get("name", ""),
                "desc": r.get("description", ""),
                "url": r.get("html_url", "#"),
                "live": r.get("homepage", ""),
                "lang": r.get("language", ""),
            }
            print(f"🔍 Processed project: {project_data['name']}")
            projects.append(project_data)

    print(f"🎯 Final projects to show: {len(projects)}")

    return JsonResponse({"projects": projects})


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
