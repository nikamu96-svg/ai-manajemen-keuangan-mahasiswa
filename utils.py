import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GROK_API_KEY")
API_URL = "https://api.x.ai/v1/chat/completions"

def ask_grok(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    body = {
        "model": "grok-beta",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, json=body, headers=headers)
    result = response.json()
    return result["choices"][0]["message"]["content"]
