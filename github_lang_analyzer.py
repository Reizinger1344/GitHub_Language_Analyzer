import requests
import matplotlib.pyplot as plt
import sys
import os
import colorlog

GITHUB_API_URL = "https://api.github.com"


def setup_logger():
    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s[%(levelname)s]%(reset)s %(message)s",
        log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "red,bg_white",
        }
    )
    handler.setFormatter(formatter)
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(colorlog.INFO)
    return logger


def get_github_token(logger):
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        logger.debug("Using GitHub token from environment variable.")
        return token

    logger.warning("GitHub token not found in environment variable 'GITHUB_TOKEN'.")
    token = input("Enter your GitHub personal access token (press Enter to continue unauthenticated): ").strip()
    if not token:
        logger.warning("Running unauthenticated. Limited to 60 API requests per hour.")
    else:
        logger.debug("Using GitHub token from user input.")
    return token


def get_repos(session, username):
    repos = []
    page = 1
    while True:
        url = f"{GITHUB_API_URL}/users/{username}/repos"
        params = {"per_page": 100, "page": page}
        response = session.get(url, params=params)
        if response.status_code == 404:
            raise Exception(f"User '{username}' not found.")
        elif response.status_code != 200:
            raise Exception(f"Failed to fetch repos: {response.status_code} {response.text}")

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1
    return repos


def get_languages(session, owner, repo_name, logger):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/languages"
    response = session.get(url)
    if response.status_code == 404:
        logger.warning(f"Repo '{repo_name}' not found or inaccessible.")
        return {}
    elif response.status_code != 200:
        raise Exception(f"Failed to fetch languages for repo '{repo_name}': {response.status_code} {response.text}")
    return response.json()


def save_language_data_to_file(language_totals, username, logger):
    filename = f"{username}_languages.txt"
    try:
        total_bytes = sum(language_totals.values())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Language usage for GitHub user: {username}\n")
            f.write("=" * 40 + "\n")
            for lang, count in sorted(language_totals.items(), key=lambda x: x[1], reverse=True):
                f.write(f"{lang}: {count} bytes\n")
            f.write("=" * 40 + "\n")
            f.write(f"Total bytes: {total_bytes}\n")
        logger.info(f"Language data saved to '{filename}'.")
    except Exception as e:
        logger.error(f"Failed to write language data to file: {e}")


def plot_language_usage(language_totals, username):
    if not language_totals:
        return

    sorted_langs = sorted(language_totals.items(), key=lambda x: x[1], reverse=True)
    langs, counts = zip(*sorted_langs)

    plt.figure(figsize=(10, 6))
    plt.bar(langs, counts, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Bytes of Code')
    plt.title(f'Languages used by GitHub user: {username}')
    plt.tight_layout()
    plt.show()


def main():
    logger = setup_logger()

    token = get_github_token(logger)
    headers = {"Authorization": f"token {token}"} if token else {}
    session = requests.Session()
    session.headers.update(headers)

    username = input("Enter GitHub username: ").strip()
    if not username:
        logger.error("Username cannot be empty.")
        sys.exit(1)

    try:
        logger.info(f"Fetching repositories for user '{username}'...")
        repos = get_repos(session, username)
        logger.info(f"Found {len(repos)} repositories.")

        if not repos:
            logger.info("User has no public repositories.")
            return

        language_totals = {}

        for repo in repos:
            repo_name = repo['name']
            logger.info(f"Fetching languages for repo: {repo_name}...")
            langs = get_languages(session, username, repo_name, logger)
            for lang, bytes_count in langs.items():
                language_totals[lang] = language_totals.get(lang, 0) + bytes_count

        if not language_totals:
            logger.info("No language data found in user's repositories.")
            return

        save_language_data_to_file(language_totals, username, logger)
        plot_language_usage(language_totals, username)

    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
