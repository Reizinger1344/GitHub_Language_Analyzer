# 🛡️ GitHub Personal Access Token (PAT) Guide

This project can optionally use a **GitHub Personal Access Token (PAT)** to increase your API rate limit when fetching data. This guide explains what a PAT is, why it matters, and how to safely create and use one.

---

## 🔍 What Is a GitHub PAT?

A Personal Access Token is like a password specifically for GitHub API access. It lets tools and scripts authenticate as *you* when making requests to GitHub — without needing your actual password.

**In this project, the PAT is used only to read public information** (like repository metadata and language stats). No scopes or write permissions are required.

---

## ⚠️ Why Do You Need One?

Without a PAT, GitHub limits your API usage to:

* ✅ **60 requests per hour (unauthenticated)**

With a PAT:

* 🚀 **Up to 5000 requests per hour**

That matters because:

* Listing repos = 1 request per 100 repos
* Fetching languages = 1 request per repo

So if you're querying someone with many repositories, you’ll hit the limit fast unless authenticated.

---

## 🧭 How to Generate a Personal Access Token

1. **Log in to GitHub**
   → [https://github.com](https://github.com)

2. **Navigate to Developer Settings**
   → Click your profile pic (top-right) → **Settings**
   → Scroll down the left menu → **Developer settings**

3. **Create Token**
   → Select **Personal access tokens** → **Tokens (classic)**
   → Click **Generate new token**

4. **Configure Your Token**

   * **Note:** Use a name like `GitHubLangStatsTool`
   * **Expiration:** Choose your preferred duration (30 days, 90 days, or no expiration)
   * **Scopes:** ✅ Leave **everything unchecked**

     > This tool only reads public data — no scopes required.

5. **Generate and Copy**

   * Click **Generate token**
   * GitHub will show it **once only** — copy and save it immediately
   * Lost it? Just regenerate a new one.

---

## 🧪 How to Use the PAT with the Script

### ➤ Option 1: Use an Environment Variable (Recommended)

Set the token in your terminal session before running the Python script:

* **Linux/macOS:**

  ```bash
  export GITHUB_TOKEN=your_token_here
  python github_lang_stats.py
  ```

* **Windows (CMD):**

  ```cmd
  set GITHUB_TOKEN=your_token_here
  python github_lang_stats.py
  ```

* **Windows (PowerShell):**

  ```powershell
  $env:GITHUB_TOKEN="your_token_here"
  python github_lang_stats.py
  ```

---

## 🌐 How to Use the PAT in the Web Version

If you're using the browser-based version:

1. Open the web app (e.g., `index.html`)
2. Paste your PAT into the **optional** input field
3. The app will use it for increased rate limits

> **Note:** Your token never leaves your browser — but it can be accessed by browser extensions. Use caution if you have untrusted extensions installed.

---

## 🧼 How to Revoke or Rotate a Token

* Go to [Your Developer Settings](https://github.com/settings/tokens)
* Click the **Delete** button next to the token you want to remove
* Generate a new one any time you need

---

## ✅ Best Practices

| ✔️ Do                           | ❌ Don’t                        |
|---------------------------------|--------------------------------|
| Store token in env vars         | Hard-code token in scripts     |
| Keep your token private         | Paste it in public chats/repos |
| Use no scopes for read-only use | Add unnecessary scopes         |
| Regenerate expired tokens       | Reuse old/insecure tokens      |

---

## 📎 Summary

| Question                    | Answer                                                  |
|-----------------------------|---------------------------------------------------------|
| Do I *have* to use a token? | No — but it greatly improves rate limits                |
| Is it secure?               | Yes, if you don’t expose it or grant extra scopes       |
| What scopes are needed?     | The minimal, Read-only to public repo's                 |
| Where do I use it?          | Environment variable (Python) or browser field (Web UI) |

---

🔒 **Use it smartly, use it safely.**
If in doubt — delete and regenerate.

---
