import urllib.request
import json

req = urllib.request.Request('https://meegostudios.com/products.json', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        products = data.get('products', [])
        print("Meego products found:", len(products))
        for p in products:
            print("Title:", p['title'], "Handle:", p['handle'])
            for img in p['images']:
                print("  IMG:", img['src'])
except Exception as e:
    print("Error:", e)
