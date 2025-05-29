# 🔍 GitHub Language Statistics Viewer

A dual-interface tool (Python + Web) to explore and visualize the programming languages used in any public GitHub user's repositories. View usage breakdowns, analyze code size, and generate visual summaries with ease.

---

## 📦 Project Overview

This project offers **two usage modes**:

| Mode          | Description                                                   |
|---------------|---------------------------------------------------------------|
| 🖥️ Web App   | Fully client-side web interface to view GitHub language stats |
| 🐍 Python CLI | Command-line tool for fetching, saving, and plotting data     |

---

## 📖 Documentation

* 📄 [**PAT Guide**](docs/PAT.md)
  Learn what a GitHub Personal Access Token is, why it's needed, and how to generate one securely.

* 🐍 [**Python Script Usage**](docs/Python.md)
  Documentation for using the command-line tool, including token handling, saving results, and visual output.

* 🌐 [**Web Version Guide**](docs/Web.md)
  Instructions and features of the browser-based version — including UI, security notice, and visual charts.

---

## 🚀 Quickstart

### ▶️ Try the Web Version

Simply open `index.html` in your browser or serve it locally,

No install required — just input a GitHub username (optionally add your PAT for increased API limits).

### ▶️ Try the Python Version

After downloading the script, and installing dependencies, run:

```bash
python3 github_lang_analyzer.py
```

You’ll be prompted for a GitHub username and optionally a PAT if you haven't set it up as a global variable.

More details [here »](docs/Python.md)

---

## 🔐 Security Notice

This tool **does not store** your GitHub token. In the web version, it stays in-browser only.
However, it is visible to the page environment and any extensions you have — so use with caution.

More info [here »](docs/PAT.md)

---

## 🧾 License

MIT License — fork, use, modify, contribute.

---
