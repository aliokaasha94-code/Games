import urllib.request
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for endpoint in ["https://saleenyeg.com/products.json?limit=250", "https://saleenyeg.com/"]:
    try:
        req = urllib.request.Request(endpoint, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            if endpoint.endswith('.json'):
                js = json.loads(data)
                print(f"Saleeny JSON: {len(js.get('products', []))} products")
                for p in js.get('products', []):
                    imgs = [im['src'] for im in p.get('images', [])]
                    print(f"  {p['title']} ({p['handle']}): {imgs[:2]}")
            else:
                print("Fetched Saleeny homepage")
                imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:png|jpg|webp)', data)
                print(f"Homepage images: {len(imgs)}")
                for im in set(imgs[:10]):
                    print("  ", im)
    except Exception as e:
        print(f"Error {endpoint}: {e}")
