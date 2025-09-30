import requests

def fetch_html(url: str) -> str:
    """Fetch rew HTML content from a url"""
    response =  requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    return response.text
