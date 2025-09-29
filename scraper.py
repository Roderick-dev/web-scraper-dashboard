import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://biggest.great-site.net"
data = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# Collect all links
for link in soup.find_all("a", href=True):
    title = link.get_text(strip=True)
    href = link["href"]
    data.append({
        "title": title if title else "(no text)",
        "link": href
    })

# Save to CSV only if data exists
if data:
    df = pd.DataFrame(data)
    df.to_csv("website_data.csv", index=False)
    print(f"✅ Scraping complete! {len(data)} records saved to website_data.csv")
else:
    print(response.text[:1000])  # shows first 1000 characters of HTML

