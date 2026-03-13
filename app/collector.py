import os
import requests
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def fetch_evidence(claim):
    """
    Searches the web for evidence related to the claim using Tavily.
    """
    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": f"fact check: {claim}",
        "search_depth": "advanced", # More thorough for fact-checking
        "max_results": 5,
        "include_answer": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        results = response.json().get("results", [])
        
        # Format the results into a clean string for the LLM
        evidence_text = ""
        for i, res in enumerate(results, 1):
            evidence_text += f"Source {i}: {res['title']}\n"
            evidence_text += f"Content: {res['content']}\n"
            evidence_text += f"URL: {res['url']}\n\n"
            
        return evidence_text if evidence_text else "No relevant evidence found."
    
    except Exception as e:
        return f"Error fetching evidence: {str(e)}"