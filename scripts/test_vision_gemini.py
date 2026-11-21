import os
import json
import base64
from pathlib import Path
import requests

# Load GEMINI_API_KEY from repo root .env if not already set in environment
env_file = Path(__file__).resolve().parent.parent / '.env'
if env_file.exists():
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
if not API_KEY:
    print("[ERROR] GEMINI_API_KEY is missing. Please create a local .env file with GEMINI_API_KEY=your_key")
    exit(1)

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

img_path = r"Image\WhatsApp Image 2026-11-17 at 12.34.25 AM.jpeg"
if not os.path.exists(img_path):
    print(f"[ERROR] Image not found at {img_path}")
    exit(1)

with open(img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

prompt = """
Examine this photo from Emad Afandi Cafe game collection.
Identify every board game or card game box you see.
For each game box, provide:
1. The exact title written on the box (Arabic and English).
2. The bounding box [ymin, xmin, ymax, xmax] normalized from 0 to 1000.
3. The visual appearance (color, logo, characters).
Return as a clean JSON list.
"""

payload = {
    "contents": [{
        "parts": [
            {"text": prompt},
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": b64_data
                }
            }
        ]
    }],
    "generationConfig": {
        "response_mime_type": "application/json"
    }
}

resp = requests.post(url, headers=headers, json=payload, timeout=30)
print("Status:", resp.status_code)
if resp.status_code == 200:
    print(resp.json()['candidates'][0]['content']['parts'][0]['text'])
else:
    print(resp.text)
