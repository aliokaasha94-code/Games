import json

data = json.load(open('shopify_products.json', encoding='utf-8'))
for store, prods in data.items():
    print(f"\n=== {store} ({len(prods)} products) ===")
    for p in prods:
        print(f"  - {p['title']} ({len(p['images'])} images)")
