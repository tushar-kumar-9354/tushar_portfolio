import requests
from django.shortcuts import render
print("THIS IS MY PROJECTS.VIEWS.PY 00")
def projects_view(request):
    resp = requests.get(
        "https://api.github.com/users/tushar-kumar-9354/repos",
        params={"per_page": 12, "sort": "pushed"},
        headers={"Accept": "application/vnd.github.v3+json"}
    )
    repos = resp.json() if resp.status_code == 200 else []
    # Filter and transform
    projects = [
        {
            "name": r["name"],
            "desc": r["description"] or "",
            "url": r["html_url"],
            "live": r["homepage"] or "",
            "lang": r["language"] or "",
        }
        for r in repos
        if not r["fork"]
    ]
    return render(request, "projects.html", {"projects": projects})
