import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_page(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode('utf-8', errors='ignore')

# Let's search nilco-int.com for products
for page in range(1, 15):
    try:
        url = f"https://nilco-int.com/ar/products?page={page}"
        html = get_page(url)
        products = re.findall(r'<a href="(https://nilco-int\.com/ar/products/\d+-[^"]+)"[^>]*>.*?<img[^>]+src="([^"]+)".*?alt="([^"]*)"', html, re.DOTALL)
        if not products:
            # try alternative regex
            links = re.findall(r'https://nilco-int\.com/ar/products/\d+-[^\s"\'<>]+', html)
            imgs = re.findall(r'https://nilco-int\.com/storage/[^\s"\'<>]+\.jpg', html)
            print(f"Page {page}: found {len(links)} links, {len(imgs)} imgs")
        else:
            print(f"Page {page}: found {len(products)} products")
            for link, img, alt in products:
                print(f"  {alt} | {link} | {img}")
    except Exception as e:
        print(f"Page {page} error: {e}")
        break
