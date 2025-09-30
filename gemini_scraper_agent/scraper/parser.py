# scraper/parser.py
from bs4 import BeautifulSoup

def clean_html(html: str) -> str:
    """Remove scripts/styles and return clean text HTML."""
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    return soup.get_text(separator="\n", strip=True)
