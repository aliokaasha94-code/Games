import urllib.request
import json
import os
from PIL import Image

os.makedirs('public/games/official_raw', exist_ok=True)

# 1. 2oolameme mappings
two_url = "https://2oolameme.com/products.json?limit=250"
req = urllib.request.Request(two_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        products = json.loads(resp.read().decode('utf-8')).get('products', [])
        for p in products:
            handle = p['handle']
            if p.get('images'):
                img_url = p['images'][0]['src']
                out_path = f"public/games/official_raw/2ool_{handle}.png"
                try:
                    urllib.request.urlretrieve(img_url, out_path)
                    print(f"Downloaded 2ool: {handle} -> {out_path}")
                except Exception as e:
                    print(f"Failed {handle}: {e}")
except Exception as e:
    print("Error fetching 2oolameme:", e)

# 2. Meego mappings
meego_url = "https://meegostudios.com/products.json"
req = urllib.request.Request(meego_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        products = json.loads(resp.read().decode('utf-8')).get('products', [])
        for p in products:
            handle = p['handle']
            if p.get('images'):
                img_url = p['images'][0]['src']
                out_path = f"public/games/official_raw/meego_{handle}.png"
                try:
                    urllib.request.urlretrieve(img_url, out_path)
                    print(f"Downloaded meego: {handle} -> {out_path}")
                except Exception as e:
                    print(f"Failed {handle}: {e}")
except Exception as e:
    print("Error fetching meego:", e)

print("Finished downloading official raw products.")
