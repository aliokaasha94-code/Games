import urllib.request
import re

url = "https://www.games2egypt.com/ar/Product/40392/%D8%AF%D9%88%D9%85%D9%8A%D9%86%D8%A7-%D8%B3%D9%8A%D8%B1%D8%A7%D9%85%D9%8A%D9%83-%D9%85%D8%B9-%D8%B5%D9%86%D8%AF%D9%88%D9%82-%D8%AD%D9%81%D8%B8-%D9%85%D8%B9%D8%AF%D9%86%D9%8A-%D8%A3%D9%86%D9%8A%D9%82"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print("All img tags:", len(imgs))
    for im in imgs:
        if 'product' in im.lower() or 'upload' in im.lower():
            print("Product img:", im)
