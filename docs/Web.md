# 🧠 GitHub Language Statistics Viewer

A browser-based tool to visualize the programming languages used across any public GitHub user's repositories. No backend required — all API requests are made client-side in your browser.

---

## ⚙️ Features

* 📊 Generates a visual language usage chart with [Chart.js](https://www.chartjs.org/)
* 📄 Outputs a text summary of total byte usage per language
* 🔐 Optional GitHub **Personal Access Token (PAT)** input for higher API rate limits
* 🌐 Fully client-side: No data is stored or sent to any server
* 🧪 Works with any public GitHub account

---

## 🖼 Interface

**Fields:**

* `GitHub Username`: The username to analyze.
* `GitHub Personal Access Token`: *(Optional)* Increases API rate limits to 5,000 requests per hour.

**Outputs:**

* **Language Summary**: A text breakdown of total bytes per language.
* **Usage Chart**: A bar chart of language usage by byte count.

---

## 🛡 Security Notice

> Your GitHub Personal Access Token (PAT) is **only used in your browser** and **never sent to any server**. However:
>
> * It may be accessible to browser extensions or other JavaScript executing in the page.
> * Do **not** use this tool on untrusted networks or browsers with unknown extensions.
> * Prefer generating **read-only tokens** with **minimal scopes**.
> 
> More info about [PAT here](PAT.md)!

---

## 🧱 Project Structure

```
/
├── index.html         # Main HTML interface
├── static/
│   ├── styles.css     # UI styling
│   ├── script.js      # Main logic & GitHub API integration
│   └── favicon.svg    # Page icon
```

---

## 📦 Dependencies

* [Chart.js](https://www.chartjs.org/) (via CDN)

---

## ❓ FAQ

**Q: What are the rate limits?**

* Without authentication: 60 requests/hour
* With a PAT: 5,000 requests/hour

**Q: What if a repo has no language data?**
It’s skipped. Empty repos or those with only non-source content may not have language stats.

**Q: Is this mobile-friendly?**
Yes — thanks to responsive styling and `<meta viewport>` usage.
