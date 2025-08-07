import requests
from collections import defaultdict
import matplotlib.pyplot as plt

username = "Wilfred430"
repos_url = f"https://api.github.com/users/{username}/repos"
response = requests.get(repos_url)
repos = response.json()

language_stats = defaultdict(int)
for repo in repos:
    lang_url = repo["languages_url"]
    lang_data = requests.get(lang_url).json()
    for lang, count in lang_data.items():
        language_stats[lang] += count

total = sum(language_stats.values())
language_percentages = {lang: (count / total) * 100 for lang, count in language_stats.items()}
sorted_langs = sorted(language_percentages.items(), key=lambda x: x[1], reverse=True)

langs = [lang for lang, _ in sorted_langs]
percents = [round(p, 2) for _, p in sorted_langs]

plt.figure(figsize=(10, 6))
bars = plt.barh(langs, percents, color='skyblue')
plt.xlabel("Usage Percentage")
plt.title("Most Used Languages by Wilfred430")
plt.gca().invert_yaxis()

for bar, pct in zip(bars, percents):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f"{pct}%", va='center')

plt.tight_layout()
plt.savefig("most_used_languages.png")
plt.show()
