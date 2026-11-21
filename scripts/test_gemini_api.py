import os
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

url = "https://generativelanguage.googleapis.com/v1beta/models"
headers = {
    "x-goog-api-key": API_KEY
}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    models = resp.json().get('models', [])
    print(f"Total available Gemini models: {len(models)}")
    for m in models:
        if 'flash' in m['name'].lower() or 'gemini' in m['name'].lower():
            print(" ", m['name'], m.get('supportedGenerationMethods'))
except Exception as e:
    print("Error:", e)
