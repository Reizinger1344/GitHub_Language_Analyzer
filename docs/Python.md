# GitHub Language Analyzer

A Python script that analyzes the programming languages used across a GitHub user's public repositories, with optional authentication, logging, and data visualization.

![GitHub Language Chart Example](https://img.shields.io/badge/matplotlib-enabled-blue)
![Colorlog Support](https://img.shields.io/badge/colorlog-enabled-green)

## 📌 Features

* Retrieves all public repositories of a GitHub user
* Fetches language statistics for each repository
* Aggregates total language usage
* Displays a bar chart of language usage
* Saves language data to a text file
* Optional GitHub token support for higher API limits
* Colored log output for better readability

---

## 🛠 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Set GitHub Token (Optional)

To avoid API rate limits (60 requests/hr unauthenticated), export a personal GitHub token:

```bash
export GITHUB_TOKEN=your_token_here
```

If omitted, the script will prompt you to enter one or continue unauthenticated.

> More info about [PAT here](PAT.md)!


### 2. Run the Script

```bash
python github_lang_analyzer.py
```

You will be prompted to enter the GitHub username to analyze.

---

## 📈 Output

* A color-coded bar chart showing bytes of code per language.
* A text file named `{username}_languages.txt` containing the language breakdown and total byte count.

Example output file:

```
Language usage for GitHub user: octocat
========================================
Python: 15000 bytes
JavaScript: 8000 bytes
HTML: 3000 bytes
========================================
Total bytes: 26000
```

---

## 🧠 Logging

The script uses `colorlog` to provide clean, colorized output for better visibility of info, warnings, and errors.

Example log:

```
[INFO] Fetching repositories for user 'octocat'...
[INFO] Found 7 repositories.
[INFO] Fetching languages for repo: hello-world...
[WARNING] GitHub token not found in environment variable 'GITHUB_TOKEN'.
```

---

## ❗ Troubleshooting

* **404 errors:** Ensure the username is correct and repositories are public.
* **Rate limiting:** Use a GitHub token to increase the request limit.
* **No language data:** Some repositories may be empty or not include detectable source files.
