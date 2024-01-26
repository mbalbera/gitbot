# GitBot - Random Daily Commits
GitBot is a simple bot designed to generate a random number of commits to a specified GitHub repository or file on a daily basis. This can be a fun way to add activity to your repositories or test workflows that involve frequent commits.

## How to Use
To run GitBot, follow these simple steps:

1. Fork the Repo: Start by forking this repository to your GitHub account.

2. Create .env file: Create a .env file in the root of your project with the following variables: (Make sure to replace the placeholder values with your actual GitHub username, personal access token, and repository details.)

```env
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_personal_access_token
REPO_OWNER=owner_of_the_repository
REPO_NAME=name_of_the_repository
```


3. Edit File Path: Open thecommit_generator.py and edit the file path variable (lines 29 and 40) to point to the file you want changed daily. This is the file in which the random commits will be made.
   
5. Host and Run: Host the GitBot script on a server or use a scheduled job (e.g., cron) to run the script daily. The script will generate a random number of commits and push them to the specified repository or file.

## Security Note
Make sure to keep your GitHub personal access token (GITHUB_TOKEN) secure and do not share it publicly. It is recommended to use a bot account with the necessary repository access rather than your personal account.

# Disclaimer
This is a joke project! GitBot is designed for educational and entertainment purposes. Excessive commits may be considered spammy behavior on GitHub, so use it responsibly.

Feel free to customize the GitBot script to suit your needs or contribute improvements to the project. Happy coding!





