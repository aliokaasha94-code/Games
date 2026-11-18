import urllib.request
import json
import ssl
import re

urls = [
    ('2oolameme', 'https://2oolameme.com/products.json?limit=250'),
    ('jokeyjoy', 'https://jokeyjoy.com/products.json?limit=250'),
    ('rebaat', 'https://rebaat-eg.com/products.json?limit=250'),
    ('saleeny', 'https://saleenyeg.com/products.json?limit=250'),
    ('masra7gareema', 'https://masra7gareema.com/products.json?limit=250'),
    ('casinoal3ab', 'https://casinoal3ab.com/products.json?limit=250'),
    ('zag', 'https://www.zag.games/products.json?limit=250'),
    ('w2pgames', 'https://w2pgames.com/wp-json/wc/store/v1/products?per_page=100'),
    ('nilco', 'https://nilco-int.com/ar'),
    ('yampstore', 'https://sllr.co/yampstore')
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

results = {}

for name, url in urls:
    print(f"Checking {name} -> {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as res:
            content = res.read().decode('utf-8', errors='ignore')
            if 'products.json' in url or 'wp-json' in url:
                try:
                    data = json.loads(content)
                    if isinstance(data, dict) and 'products' in data:
                        prods = [p['title'] for p in data['products']]
                        results[name] = prods
                        print(f"  [SUCCESS] {name} has {len(prods)} products (Shopify)")
                    elif isinstance(data, list):
                        prods = [p.get('name', p.get('title', '')) for p in data]
                        results[name] = prods
                        print(f"  [SUCCESS] {name} has {len(prods)} products (WooCommerce/List)")
                except Exception as e:
                    print(f"  [JSON ERROR] {name}: {e}")
            else:
                # Basic html scrape
                titles = re.findall(r'<h[234][^>]*>(.*?)</h[234]>', content, re.IGNORECASE)
                clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in titles if len(t.strip()) > 2]
                results[name] = clean_titles[:30]
                print(f"  [HTML SUCCESS] {name}: extracted {len(clean_titles)} headings")
    except Exception as e:
        print(f"  [FETCH ERROR] {name}: {e}")

with open('catalog_dump.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDumped to catalog_dump.json")
