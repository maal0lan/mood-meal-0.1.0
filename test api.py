import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {
    "Authorization": f"Bearer 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",
    "Content-Type": "application/json"
}
payload = {
    "inputs": "Say hello to MoodMeal."
}

r = requests.post(API_URL, headers=headers, json=payload)
print(r.status_code)
print(r.text)
