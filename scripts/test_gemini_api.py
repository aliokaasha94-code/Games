import os
import json
import base64
import requests

API_KEY = "AIzaSyAmxiITvbiZA0ObuXMJnoZ1JmPIR_gFIfQ"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    resp = requests.get(url, timeout=10)
    print("Status:", resp.status_code)
    models = resp.json().get('models', [])
    print(f"Total available Gemini models: {len(models)}")
    for m in models:
        if 'flash' in m['name'].lower() or 'gemini' in m['name'].lower():
            print(" ", m['name'], m.get('supportedGenerationMethods'))
except Exception as e:
    print("Error:", e)
