# AI Fact-Checker

A modular Python application that verifies claims using Real-Time Web Search and LLM reasoning.

## 🚀 Features
- **Evidence Collection:** Uses Tavily AI to scrape high-quality web data.
- **Reasoning Engine:** Powered by Llama 3.1 via Groq for ultra-fast inference.
- **Persistence:** All checks are logged in a PostgreSQL database using SQLAlchemy.
- **Zero-Shot Logic:** Uses RAG (Retrieval-Augmented Generation) principles.

## 🛠️ Setup
1. Clone the repo.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it and install: `pip install -r requirements.txt`.
4. Create a `.env` file with `GROQ_API_KEY`, `TAVILY_API_KEY`, and `DATABASE_URL`.
5. Run the app: `python -m app.main`.
