import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://luciddreaminggames.com', headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

urls = set(re.findall(r'href=[\'"]([^\'"]+)[\'"]', html))
for u in sorted(urls):
    if any(k in u.lower() for k in ['game', 'product', 'shop', 'el-', 'fuga']):
        print("Link:", u)
