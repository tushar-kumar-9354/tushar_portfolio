import requests
from bs4 import BeautifulSoup

def fetch_github_repos_brute(username):
    url = f"https://github.com/{username}?tab=repositories"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    repos = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        repo_list = soup.find_all('li', {'itemprop': 'owns'})

        for repo in repo_list:
            name = repo.find('a', itemprop='name codeRepository')
            description = repo.find('p', itemprop='description')
            lang = repo.find('span', itemprop='programmingLanguage')

            repo_info = {
                'name': name.text.strip() if name else None,
                'url': f"https://github.com{name['href']}" if name else None,
                'description': description.text.strip() if description else "No description",
                'language': lang.text.strip() if lang else "Unknown"
            }
            repos.append(repo_info)

        return repos

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching GitHub repos:", e)
        return []

# Example usage:
username = "tushar-kumar-9354"
projects = fetch_github_repos_brute(username)

for p in projects:
    print(f"🔹 {p['name']} ({p['language']})\n   {p['description']}\n   {p['url']}\n")
