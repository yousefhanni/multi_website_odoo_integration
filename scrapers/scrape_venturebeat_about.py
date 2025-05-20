import requests
from bs4 import BeautifulSoup
import json

url = "https://venturebeat.com/about/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.get_text(strip=True) if soup.title else "No Title"

content_div = soup.find("div", class_="entry-content")
page_content = ""

if content_div:
    elements = content_div.find_all(["h2", "p", "li"])
    for el in elements:
        text = el.get_text(strip=True)
        if text:
            page_content += text + "\n"

data = {
    "page_title": title,
    "page_content": page_content.strip(),
    "source_url": url
}

with open("venturebeat_about.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Static page content saved to venturebeat_about.json")
