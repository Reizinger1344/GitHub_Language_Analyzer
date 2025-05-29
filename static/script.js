(function() {
    const form = document.getElementById('githubForm');
    const resultsDiv = document.getElementById('results');
    const summaryPre = document.getElementById('languageSummary');
    const chartCtx = document.getElementById('languageChart').getContext('2d');
    let chartInstance = null;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        resultsDiv.hidden = true;
        summaryPre.textContent = '';
        if (chartInstance) {
            chartInstance.destroy();
            chartInstance = null;
        }

        const username = form.username.value.trim();
        const token = form.token.value.trim();
        if (!username) {
            alert('Please enter a GitHub username.');
            return;
        }

        const headers = {};
        if (token) {
            headers['Authorization'] = 'token ' + token;
        }

        try {
            form.querySelector('button').disabled = true;
            form.querySelector('button').textContent = 'Fetching...';

            // Fetch repos paginated
            let repos = [];
            let page = 1;
            while (true) {
                const repoResponse = await fetch(`https://api.github.com/users/${encodeURIComponent(username)}/repos?per_page=100&page=${page}`, { headers });
                if (repoResponse.status === 404) {
                    throw new Error(`User '${username}' not found.`);
                }
                if (!repoResponse.ok) {
                    const text = await repoResponse.text();
                    throw new Error(`Failed to fetch repos: ${repoResponse.status} ${text}`);
                }
                const data = await repoResponse.json();
                if (data.length === 0) break;
                repos = repos.concat(data);
                page++;
            }

            if (repos.length === 0) {
                summaryPre.textContent = 'User has no public repositories.';
                resultsDiv.hidden = false;
                return;
            }

            // Fetch languages for all repos
            let languageTotals = {};
            for (const repo of repos) {
                const langResponse = await fetch(`https://api.github.com/repos/${encodeURIComponent(username)}/${encodeURIComponent(repo.name)}/languages`, { headers });
                if (langResponse.status === 404) {
                    console.warn(`Repo '${repo.name}' not found or inaccessible.`);
                    continue;
                }
                if (!langResponse.ok) {
                    const text = await langResponse.text();
                    throw new Error(`Failed to fetch languages for repo '${repo.name}': ${langResponse.status} ${text}`);
                }
                const langs = await langResponse.json();
                for (const [lang, bytes] of Object.entries(langs)) {
                    languageTotals[lang] = (languageTotals[lang] || 0) + bytes;
                }
            }

            if (Object.keys(languageTotals).length === 0) {
                summaryPre.textContent = 'No language data found in user\'s repositories.';
                resultsDiv.hidden = false;
                return;
            }

            // Prepare text summary
            let totalBytes = 0;
            const sortedLangs = Object.entries(languageTotals).sort((a,b) => b[1] - a[1]);
            let textSummary = `Language usage for GitHub user: ${username}\n${'='.repeat(40)}\n`;
            for (const [lang, count] of sortedLangs) {
                textSummary += `${lang}: ${count.toLocaleString()} bytes\n`;
                totalBytes += count;
            }
            textSummary += `${'='.repeat(40)}\nTotal bytes: ${totalBytes.toLocaleString()}\n`;
            summaryPre.textContent = textSummary;

            // Create bar chart
            const labels = sortedLangs.map(x => x[0]);
            const data = sortedLangs.map(x => x[1]);

            chartInstance = new Chart(chartCtx, {
                type: 'bar',
                data: {
                    labels,
                    datasets: [{
                        label: 'Bytes of Code',
                        data,
                        backgroundColor: 'rgba(3, 102, 214, 0.7)',
                        borderColor: 'rgba(3, 102, 214, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return value.toLocaleString();
                                }
                            }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.parsed.y.toLocaleString() + ' bytes';
                                }
                            }
                        }
                    }
                }
            });

            resultsDiv.hidden = false;

        } catch (err) {
            alert('Error: ' + err.message);
        } finally {
            form.querySelector('button').disabled = false;
            form.querySelector('button').textContent = 'Fetch Language Stats';
        }
    });
})();
