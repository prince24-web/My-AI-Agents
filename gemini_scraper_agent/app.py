# app.py
import streamlit as st
import pandas as pd

from scraper.fetcher import fetch_html
from scraper.parser import clean_html
from scraper.gemini_agent import init_gemini, analyze_with_gemini

st.title("🌐 Gemini Web Scraper AI Agent")
st.caption("Scrape and analyze websites using Google Gemini + BeautifulSoup")

# User inputs
api_key = st.text_input("🔑 Enter your Gemini API key", type="password")
url = st.text_input("🌍 Enter website URL")
prompt = st.text_area("📝 What do you want to extract?", "Extract all headings and links")

if st.button("Scrape") and api_key and url and prompt:
    try:
        model = init_gemini(api_key)
        html = fetch_html(url)
        cleaned_html = clean_html(html)

        # Send to Gemini (for MVP we send everything at once)
        result = analyze_with_gemini(model, prompt, cleaned_html)

        st.subheader("✅ Extracted Data")
        st.write(result)

        # Save to file
        df = pd.DataFrame({"Result": [result]})
        df.to_csv("data/outputs/result.csv", index=False)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), "result.csv")

    except Exception as e:
        st.error(f"Error: {e}")
