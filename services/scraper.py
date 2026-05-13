import requests
from bs4 import BeautifulSoup

def scrape_company(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except:
        return "Could not scrape company website." 