import requests
import urllib3
import os
from dotenv import load_dotenv

# Desactivar warnings SSL
urllib3.disable_warnings()

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
print(API_KEY)
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {
            "role": "user",
            "content": "Say hello in Spanish"
        }
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=data,
    verify=False
)

print(response.status_code)
print(response.text)