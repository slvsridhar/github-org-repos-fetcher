import requests
import json

def get_github_repos(org):
    url = f"https://api.github.com/orgs/{org}/repos"
    repos = []
    page = 1
    while True:
        response = requests.get(url, params={'per_page': 100, 'page': page})
        if response.status_code != 200:
            print(f"Failed to fetch repositories: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        repos.extend([repo['name'] for repo in data])
        page += 1
    return repos

if __name__ == "__main__":
    org = input("Enter the GitHub organization name (default: microsoft): ") or "microsoft"
    repos = get_github_repos(org)
    print(f"Repositories in '{org}':")
    for repo in repos:
        print(repo)
    print(len(repos))
    # Save to JSON file
    output = {org: repos}
    filename = f"{org}_repositories.json"
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Repository list saved to {filename}")
