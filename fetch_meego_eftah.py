import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

sites = [
    'https://meegostudios.com/products.json?limit=250',
    'https://eftahtopic.net/products.json?limit=250'
]

for s in sites:
    try:
        req = urllib.request.Request(s, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            data = json.loads(r.read().decode('utf-8'))
            print(f"=== {s} ({len(data.get('products', []))} products) ===")
            for p in data.get('products', []):
                img = p['images'][0]['src'] if p.get('images') else 'NO_IMG'
                print(f"  - {p['title']} -> {img}")
    except Exception as e:
        print(f"ERROR {s}: {e}")
