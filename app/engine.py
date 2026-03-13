import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_verdict(claim, evidence):
    """
    Analyzes a claim against provided evidence using Llama 3 via Groq.
    """
    prompt = f"""
    SYSTEM: You are a professional fact-checker. You must be objective and rely ONLY on the provided evidence.
    
    CLAIM: {claim}
    
    EVIDENCE:
    {evidence}
    
    INSTRUCTIONS:
    1. Compare the CLAIM against the EVIDENCE.
    2. Decide if the claim is SUPPORTED, REFUTED, or if there is NOT ENOUGH INFORMATION.
    3. Provide a concise, one-sentence reasoning.
    4. List the SPECIFIC SOURCES from the evidence that helped you decide.
    
    OUTPUT FORMAT (JSON):
    {{
        "verdict": "SUPPORTED | REFUTED | NOT ENOUGH INFORMATION",
        "reasoning": "Your explanation here."
        "sources_used": ["Source 1", "Source 2"]
    }}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant", # Extremely fast and free
        response_format={"type": "json_object"}
    )
    
    return chat_completion.choices[0].message.content