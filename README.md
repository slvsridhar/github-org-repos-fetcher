<<<<<<< HEAD
# github-org-repos-fetcher
A simple Python script to fetch and save the list of repositories for any public GitHub organization using the GitHub REST API.
=======
# github-org-repo-fetcher

A simple Python script to fetch and save the list of repositories for any public GitHub organization using the GitHub REST API.

## Features
- Fetches all repositories for a specified GitHub organization
- Saves the repository list to a JSON file named after the organization
- Command-line input for organization name (defaults to `microsoft`)

## Requirements
- Python 3.x
- requests library

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/<your-username>/github-org-repo-fetcher.git
   cd github-org-repo-fetcher
   ```
2. (Recommended) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
Run the script and enter the organization name when prompted:

```sh
python OrganizationRepositories.py
```

- Press Enter to use the default organization (`microsoft`).
- The script will print the repositories and save them to `<org>_repositories.json`.

## Example Output
```
Repositories in 'microsoft':
repo1
repo2
...
Repository list saved to microsoft_repositories.json
```

## License
MIT
>>>>>>> 2bd6b27 (Add README with project description and usage instructions)
