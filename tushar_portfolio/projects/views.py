import os
import requests
from django.http import JsonResponse

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def projects_view(request):
    try:
        print("📡 Fetching GitHub repos...")

        headers = {
            "Accept": "application/vnd.github.v3+json"
        }

        # Add Authorization only if token exists
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"

        resp = requests.get(
            "https://api.github.com/users/tushar-kumar-9354/repos",
            params={"per_page": 12, "sort": "pushed"},
            headers=headers,
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

    # Transform
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

    print(f"🎯 Final projects to show: {len(projects)}")
    return JsonResponse({"projects": projects})
