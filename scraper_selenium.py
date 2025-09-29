# scraper_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://biggest.great-site.net"

def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def fetch_html(url):
    driver = create_driver(headless=False)  # set to False so you see the browser
    driver.get(url)
    time.sleep(8)  # wait for JS redirect and loading
    html = driver.page_source
    driver.quit()
    return html

def parse_and_save(html):
    soup = BeautifulSoup(html, "html.parser")
    data = []

    # Collect links
    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"]
        data.append({"type": "link", "text": text if text else "(no text)", "value": href})

    # Collect headings
    for h in soup.find_all(["h1", "h2", "h3"]):
        text = h.get_text(strip=True)
        if text:
            data.append({"type": "heading", "text": text, "value": ""})

    # Collect images
    for img in soup.find_all("img", src=True):
        alt = img.get("alt", "")
        src = img["src"]
        data.append({"type": "image", "text": alt if alt else "(no alt)", "value": src})

    if data:
        df = pd.DataFrame(data)
        df.to_csv("website_data.csv", index=False)
        print(f"✅ Scraping complete! {len(df)} records saved to website_data.csv")
    else:
        print("⚠️ No data found")

if __name__ == "__main__":
    html = fetch_html(URL)
    parse_and_save(html)
