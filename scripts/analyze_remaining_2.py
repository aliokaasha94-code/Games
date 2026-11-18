import os
import json
import base64
import requests

API_KEY = "AIzaSyAmxiITvbiZA0ObuXMJnoZ1JmPIR_gFIfQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

for p in ["WhatsApp Image 2026-11-17 at 12.35.02 AM (1).jpeg", "WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg"]:
    img_path = os.path.join("Image", p)
    print(f"Analyzing {p}...")
    with open(img_path, "rb") as f:
        b64_data = base64.b64encode(f.read()).decode('utf-8')
    prompt = """
Examine this photo from Emad Afandi Cafe game collection.
Identify EVERY board game, card game, puzzle, or novelty box visible.
Look especially for:
- "عروستي" (3arosty)
- "رزع الجمهور" (Raz3 El Gomhoor)
- "طموحي" (Tomouhy)
- "الجوكر" (El Joker)
- "سلسلة بطاقات المعرفة" (Mawsoo3at Al Ma3refa)
- "دومينو" (Domino)
- "تسالي" (Tasali)
For each item provide:
- "name_ar": Exact Arabic name on the box
- "name_en": English name or transliteration
- "box_2d": [ymin, xmin, ymax, xmax] normalized 0-1000
- "description": Brief visual features
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
        resp = requests.post(url, json=payload, timeout=45)
        print("Status:", resp.status_code)
        if resp.status_code == 200:
            parsed = json.loads(resp.json()['candidates'][0]['content']['parts'][0]['text'])
            print(f"Found {len(parsed)} items in {p}:")
            for item in parsed:
                print(f"  [{item.get('name_ar')}] box={item.get('box_2d')} | {item.get('description', '')[:50]}")
            with open(f"scripts/boxes_{p}.json", "w", encoding="utf-8") as f:
                json.dump(parsed, f, ensure_ascii=False, indent=2)
        else:
            print("Error:", resp.text)
    except Exception as e:
        print("Exception:", e)
