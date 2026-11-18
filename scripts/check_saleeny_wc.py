import urllib.request
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in ["https://saleenyeg.com/wp-json/wc/store/products", "https://saleenyeg.com/shop/"]:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            if 'wp-json' in url:
                products = json.loads(data)
                print(f"WooCommerce API returned {len(products)} products:")
                for p in products:
                    name = p.get('name')
                    images = [im.get('src') for im in p.get('images', [])]
                    print(f"  {name}: {images}")
            else:
                imgs = re.findall(r'<img[^>]+src="([^"]+wp-content/uploads/[^"]+)"[^>]*alt="([^"]*)"', data)
                print(f"Shop page returned {len(imgs)} images:")
                for src, alt in imgs:
                    print(f"  {alt}: {src}")
    except Exception as e:
        print(f"Error {url}: {e}")
