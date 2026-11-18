import urllib.request
import json
import ssl

urls = {
    '2oolameme': 'https://2oolameme.com/products.json?limit=250',
    'jokeyjoy': 'https://jokeyjoy.com/products.json?limit=250',
    'saleeny': 'https://saleenyeg.com/products.json?limit=250',
    'casinoal3ab': 'https://casinoal3ab.com/products.json?limit=250',
    'rebaat': 'https://rebaat-eg.com/products.json?limit=250'
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

store_data = {}

for store, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            data = json.loads(r.read().decode('utf-8'))
            items = []
            for p in data.get('products', []):
                title = p.get('title', '')
                handle = p.get('handle', '')
                images = [img.get('src') for img in p.get('images', [])]
                items.append({'title': title, 'handle': handle, 'images': images})
            store_data[store] = items
            print(f"[SUCCESS] {store}: {len(items)} products fetched.")
    except Exception as e:
        print(f"[ERROR] {store}: {e}")

with open('shopify_products.json', 'w', encoding='utf-8') as f:
    json.dump(store_data, f, ensure_ascii=False, indent=2)

print("\nSaved all products to shopify_products.json")
