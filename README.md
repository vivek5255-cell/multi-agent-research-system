# 🔬 Multi-Agent AI Research System

An AI-powered research assistant built using LangChain, Gemini, Tavily Search, BeautifulSoup, and Streamlit.

## Features

- Multi-Agent Architecture
- Web Search Agent
- Web Scraping Agent
- Research Report Generator
- Research Critic
- Streamlit UI
- Gemini API
- Tavily Search API

## Tech Stack

- Python
- Streamlit
- LangChain
- Gemini API
- Tavily
- BeautifulSoup

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multi-agent-research-system.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GOOGLE_API_KEY=YOUR_KEY
TAVILY_API_KEY=YOUR_KEY
```

Run

```bash
streamlit run app.py
```

## Project Structure

```
app.py
agents.py
tools.py
requirements.txt
.env.example
README.md
```