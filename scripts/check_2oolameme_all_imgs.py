import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request("https://2oolameme.com/products.json?limit=250", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for p in data['products']:
    print(f"=== {p['title']} ({p['handle']}) ===")
    for img in p.get('images', []):
        print(f"   {img['src']}")
