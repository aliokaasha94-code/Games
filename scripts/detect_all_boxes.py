import os
import json
import base64
import time
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

image_dir = 'Image'
photos = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

all_detections = {}

for p in photos:
    img_path = os.path.join(image_dir, p)
    print(f"Analyzing {p}...")
    with open(img_path, "rb") as f:
        b64_data = base64.b64encode(f.read()).decode('utf-8')

    prompt = """
Examine this photo from Emad Afandi Cafe game collection.
Identify EVERY board game, card game, puzzle, or novelty box visible.
For each item provide:
- "name_ar": Exact Arabic name on the box
- "name_en": English name or transliteration
- "box_2d": [ymin, xmin, ymax, xmax] normalized 0-1000
- "description": Brief visual features (colors, characters, logos)
Return a valid JSON array of objects.
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
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code == 200:
            data = resp.json()['candidates'][0]['content']['parts'][0]['text']
            parsed = json.loads(data)
            all_detections[p] = parsed
            print(f"  -> Found {len(parsed)} items in {p}")
        else:
            print(f"  -> Error {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"  -> Exception: {e}")
    time.sleep(1)

with open("scripts/cafe_boxes_detected.json", "w", encoding="utf-8") as f:
    json.dump(all_detections, f, ensure_ascii=False, indent=2)

print("Saved all detections to scripts/cafe_boxes_detected.json!")
