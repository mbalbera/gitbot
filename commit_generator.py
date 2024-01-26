import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import base64
import subprocess


def commit_generator(num):
    # Load environment variables from .env file
    load_dotenv()

    # GitHub credentials
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')

    # Repository information
    repo_owner = os.getenv('REPO_OWNER')
    repo_name = os.getenv('REPO_NAME')

    # API endpoint
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs/heads/main'

    # Get the latest commit SHA
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    response_json = response.json()
    latest_commit_sha = response_json['object']['sha']

    with open('alterable_file.py', 'r') as file:
        file_content = file.read()

    # Encode the content of the file
    base64_encoded_content = base64.b64encode(file_content.encode()).decode()

    # Create a new tree
    tree_data = {
        "base_tree": latest_commit_sha,
        "tree": [
            {
                "path": "alterable_file.py",
                "mode": "100644",
                "type": "blob",
                "content": base64_encoded_content
            }
        ]
    }

    tree_response = requests.post(f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees',
                                  json=tree_data, auth=HTTPBasicAuth(username, token))

    tree_response.raise_for_status()  # Raise an HTTPError for bad responses
    tree_sha = tree_response.json()['sha']

    # Create a new commit
    commit_data = {
        "message": f'Commit message # of the day {num}',
        "tree": tree_sha,
        "parents": [latest_commit_sha]
    }

    commit_response = requests.post(f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits',
                                    json=commit_data, auth=HTTPBasicAuth(username, token))

    commit_response.raise_for_status()  # Raise an HTTPError for bad responses
    new_commit_sha = commit_response.json()['sha']

    # Update the branch reference
    update_data = {
        "sha": new_commit_sha,
        "force": True
    }

    response = requests.patch(url, json=update_data,
                              auth=HTTPBasicAuth(username, token))

    if response.status_code == 200:
        print("Commit pushed successfully!")
    else:
        print(
            f"Failed to push commit. Status code: {response.status_code}, Message: {response.text}")

    # Local commit and push
    subprocess.run(['git', 'add', 'alterable_file.py'])
    subprocess.run(
        ['git', 'commit', '-m', f'Commit message # of the day {num}'])
