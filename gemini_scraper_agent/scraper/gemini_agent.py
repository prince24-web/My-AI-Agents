# scraper/gemini_agent.py
import google.generativeai as genai

def init_gemini(api_key: str, model: str = "gemini-2.0-flash"):
    """Initialize Gemini API client."""
    genai.configure(api_key=api_key)
    return model

def analyze_with_gemini(model: str, prompt: str, html_chunk: str):
    """Send HTML chunk + user instruction to Gemini and return response."""
    response = genai.GenerativeModel(model).generate_content(
        f"{prompt}\n\nHere is the HTML content:\n{html_chunk}"
    )
    return response.text
