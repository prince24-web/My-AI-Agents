# Gemini Web Scraper Agent

An AI-powered web scraper built with **BeautifulSoup** and **Google Gemini API**.  
It fetches content from a website, parses the text, and sends it to Gemini for summarization, Q&A, or any prompt you provide.

---

## 🚀 Features
- Scrape webpages using `requests + BeautifulSoup`.
- Extract meaningful text from HTML.
- Send extracted text to **Gemini API** for AI-powered analysis.
- Save results automatically into `data/outputs/`.
- Interactive **Streamlit UI**.

---

## 📂 Project Structure
gemini_scraper_agent/
│── app.py # Streamlit entry point
│── requirements.txt # Dependencies
│── README.md # Project guide
│
├── scraper/
│ ├── init.py
│ ├── fetcher.py # Fetches HTML
│ ├── parser.py # Extracts text
│ ├── gemini_agent.py # Gemini API interaction
│ └── utils.py # Helpers
│
├── data/
│ ├── outputs/ # AI outputs
│ └── cache/ # Optional caching


---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/prince24-web/My-AI-Agents.git
   cd gemini-scraper-agent

 **Create a virtual environment (recommended)**
```bash
 python -m venv venv
```
# On Windows
```bash
.\venv\Scripts\activate
```
# On macOS/Linux
```bash
source venv/bin/activate
```
## Install dependencies
``` bash
pip install -r requirements.txt
```
## Running the App
``` bash
streamlit run app.py
```
** Example Prompts **
- Summarize this article in 5 bullet points
- Extract all names of people mentioned
- Rewrite this news post as a Twitter thread
- Generate 3 quiz questions based on this page
- Highlight only the AI-related news from this site


##  Example Websites to Test
Website 	                URL	Example                                                                 Prompt
Tech News	            https://techcrunch.com	                                         "Summarize the latest headlines in 3 bullet points"
Hacker News         	https://news.ycombinator.com	                                   "Summarize the top 5 posts and explain why they are trending"
Wikipedia               https://en.wikipedia.org/wiki/Artificial_intelligence	            "Summarize this article in 5 sentences, focusing on AI applications"            
BBC News	             https://www.bbc.com/news	                                        "What are the top 3 global stories today?"
Quotes for Testing	     https://quotes.toscrape.com	                                    "Extract 5 quotes and rewrite them as motivational tweets"


