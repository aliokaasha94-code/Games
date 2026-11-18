import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://diwanegypt.com/product/screw-card-game-second-edition/'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'src=["\']([^"\']+\.(?:webp|jpg|jpeg|png))["\']', html)
        print("Diwan Screw images:")
        for img in imgs:
            if 'product' in img or 'upload' in img:
                print("  ", img)
except Exception as e:
    print("Error Diwan:", e)
