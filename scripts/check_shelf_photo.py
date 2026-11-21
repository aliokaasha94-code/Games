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

p = "WhatsApp Image 2026-11-17 at 12.35.02 AM (1).jpeg"
img_path = os.path.join("Image", p)
with open(img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

prompt = """
Examine this photo from Emad Afandi Cafe game shelf.
Identify all games, especially look for "طموحي" (Tomouhy), "تسالي", "طوبة ورقة مقص", or any other box.
Provide a JSON array with name_ar, box_2d [ymin, xmin, ymax, xmax], description.
"""
payload = {
    "contents": [{
        "parts": [
            {"text": prompt},
            {"inline_data": {"mime_type": "image/jpeg", "data": b64_data}}
        ]
    }],
    "generationConfig": {"response_mime_type": "application/json"}
}
try:
    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    print("Status:", resp.status_code)
    if resp.status_code == 200:
        parsed = json.loads(resp.json()['candidates'][0]['content']['parts'][0]['text'])
        print(f"Found {len(parsed)} items:")
        for item in parsed:
            print(f"  [{item.get('name_ar')}] box={item.get('box_2d')} | {item.get('description', '')[:50]}")
        with open(f"scripts/boxes_{p}.json", "w", encoding="utf-8") as f:
            json.dump(parsed, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error:", e)
