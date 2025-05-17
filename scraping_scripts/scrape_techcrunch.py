import requests
from bs4 import BeautifulSoup
import json

base_url = "https://techcrunch.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

results = []

articles = soup.select("a.loop-card__title-link")[:5]

for article in articles:
    url = article['href']
    title = article.get_text(strip=True)

    post_response = requests.get(url)
    post_soup = BeautifulSoup(post_response.text, 'html.parser')

    try:
        summary = post_soup.find("meta", {"name": "description"})['content']
    except:
        summary = ""

    try:
        content_div = post_soup.find(
            "div",
            class_="entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained"
        )
        paragraphs = content_div.find_all("p", class_="wp-block-paragraph")
        full_content = " ".join([p.get_text(strip=True) for p in paragraphs])
    except:
        full_content = ""

    try:
        date = post_soup.find("time")['datetime']
    except:
        date = ""

    results.append({
        "title": title,
        "summary": summary,
        "content": full_content,
        "date_published": date,
        "source_url": url
    })

with open("techcrunch_blogs.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
