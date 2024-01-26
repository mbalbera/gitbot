import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
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

    # Create a new commit
    commit_data = {
        "message": f'Commit message # of the day {num}',
        "content": "bXkgbmV3IGZpbGUgY29udGVudHM=",  # Base64-encoded file content
        "sha": latest_commit_sha
    }

    response = requests.post(f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits',
                            json=commit_data, auth=HTTPBasicAuth(username, token))

    new_commit_sha = response.json()['sha']

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
