import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def check_shopify(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Success fetching {url}: {len(data.get('products', []))} products found!")
            for p in data.get('products', []):
                title = p.get('title')
                handle = p.get('handle')
                images = [img['src'] for img in p.get('images', [])]
                print(f" - {title} ({handle}): {len(images)} images")
                if images:
                    print(f"   First image: {images[0]}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

check_shopify("https://2oolameme.com/products.json?limit=250")
