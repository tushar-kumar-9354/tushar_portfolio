import requests
from django.http import JsonResponse
#last check


def projects_view(request):
    try:
        print("📡 Fetching GitHub repos...")

        # No Authorization header (using public access)
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }

        resp = requests.get(
            "https://api.github.com/users/tushar-kumar-9354/repos",
            params={"per_page": 12, "sort": "pushed"},
            headers=headers,
            timeout=5
        )

        print(f"📦 Response Status Code: {resp.status_code}")

        # Handle rate limiting (403 without token)
        if resp.status_code == 403:
            print("❌ Hit GitHub rate limit (403) — unauthenticated API requests are limited to 60/hour.")
            return JsonResponse({"error": "GitHub rate limit exceeded (unauthenticated)"}, status=429)

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
