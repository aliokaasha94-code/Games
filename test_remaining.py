import urllib.request
import ssl
import json
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            return res.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

# 1. JokeyJoy
print("Testing JokeyJoy...")
content = fetch_url('https://jokeyjoy.com/collections/all')
if not content.startswith("Error"):
    # extract product links/titles
    titles = re.findall(r'class="[^"]*product-item__title[^"]*">([^<]+)<', content)
    if not titles:
        titles = re.findall(r'href="/products/([^"?]+)"', content)
    print(f"JokeyJoy found: {len(set(titles))} titles: {list(set(titles))[:15]}")
else:
    print(f"JokeyJoy error: {content}")

# 2. Saleeny
print("\nTesting Saleeny...")
content = fetch_url('https://saleenyeg.com/')
if not content.startswith("Error"):
    links = re.findall(r'href="([^"]*(?:product|shop)[^"]*)"', content)
    print(f"Saleeny links found: {len(links)}: {links[:10]}")
    # try title matches
    titles = re.findall(r'<h[234][^>]*>(.*?)</h[234]>', content)
    clean = [re.sub(r'<[^>]+>', '', t).strip() for t in titles if len(t.strip()) > 2]
    print(f"Saleeny headings: {clean[:15]}")
else:
    print(f"Saleeny error: {content}")

# 3. W2P Games
print("\nTesting W2P Games...")
content = fetch_url('https://w2pgames.com/ar/shop/')
if not content.startswith("Error"):
    titles = re.findall(r'<h2 class="woocommerce-loop-product__title">([^<]+)</h2>', content)
    if not titles:
        titles = re.findall(r'class="[^"]*product-title[^"]*"><a[^>]*>([^<]+)</a>', content)
    print(f"W2P Games found: {len(titles)} titles: {titles[:15]}")
else:
    print(f"W2P Games error: {content}")

# 4. Nilco
print("\nTesting Nilco...")
content = fetch_url('https://nilco-int.com/ar/products')
if not content.startswith("Error"):
    titles = re.findall(r'<h[2345][^>]*>(.*?)</h[2345]>', content)
    clean = [re.sub(r'<[^>]+>', '', t).strip() for t in titles if len(t.strip()) > 2]
    print(f"Nilco products headings: {clean[:20]}")
else:
    content = fetch_url('https://nilco-int.com/ar')
    titles = re.findall(r'<h[2345][^>]*>(.*?)</h[2345]>', content)
    clean = [re.sub(r'<[^>]+>', '', t).strip() for t in titles if len(t.strip()) > 2]
    print(f"Nilco home headings: {clean[:20]}")
