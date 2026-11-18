import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://handagames.com/'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
    html = r.read().decode('utf-8', errors='ignore')
    links = set(re.findall(r'href=[\'"]([^\'"]+)[\'"]', html))
    for l in sorted(links):
        if 'product' in l or 'category' in l or 'p-' in l or 'item' in l or 'handa' in l or l.startswith('/'):
            print("LINK:", l)
