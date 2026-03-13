import json
from app.collector import fetch_evidence
from app.engine import get_verdict
from app.database import init_db, save_fact_check

def run_fact_checker():
    # Ensure tables exist
    init_db()

    print("--- AI Fact-Checking POC ---")
    claim = input("Enter the claim you want to verify: ")
    
    print("\n[1/2] Searching the web for evidence...")
    evidence = fetch_evidence(claim)
    
    print("[2/2] Analyzing evidence with Llama 3 (Groq)...")
    # The get_verdict function returns a JSON string
    raw_result = get_verdict(claim, evidence)
    
    # Parse the JSON for a clean output
    result = json.loads(raw_result)
    print("[3/3] Saving result to PostgreSQL...")
    save_fact_check(
        claim=claim,
        verdict=result.get("verdict"),
        reasoning=result.get("reasoning"),
        evidence=evidence
    )

    # --- NEW: Display the Evidence ---
    print("\n" + "="*50)
    print("FOUND EVIDENCE:")
    print(evidence) 
    print("="*50)
    
    
    print(f"VERDICT: {result.get('verdict')}")
    print(f"REASONING: {result.get('reasoning')}")
    print("="*30)

if __name__ == "__main__":
    run_fact_checker()