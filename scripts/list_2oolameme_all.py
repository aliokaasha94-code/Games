import urllib.request
import json

req = urllib.request.Request('https://2oolameme.com/products.json?limit=250', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        products = data.get('products', [])
        print("Total 2oolameme products:", len(products))
        for p in products:
            print(f"{p['title']} | {p['handle']} | {p['images'][0]['src'] if p['images'] else ''}")
except Exception as e:
    print("Error:", e)
