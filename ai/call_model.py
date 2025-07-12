# ai/call_model.py

import requests

def call_model(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",   # Use the model you pulled with `ollama pull mistral`
            "prompt": prompt,
            "stream": False       # Set to True if you want streaming (we use False for simple integration)
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama API Error: {response.status_code} - {response.text}")

    return response.json().get("response", "").strip()
