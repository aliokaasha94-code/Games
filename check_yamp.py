import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://sllr.co/yampstore'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
    html = r.read().decode('utf-8', errors='ignore')
    imgs = set(re.findall(r'(https?://[^\s"\'<>]+\.(?:webp|jpg|jpeg|png))', html))
    for img in sorted(imgs):
        print("IMG:", img)
