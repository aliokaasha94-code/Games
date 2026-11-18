import urllib.request
import re
import ssl
import json

targets = [
    ('meego', 'https://meegostudios.com/'),
    ('handa', 'https://handagames.com/'),
    ('kataflam', 'https://kataflam.com/'),
    ('eftahtopic', 'https://eftahtopic.net/'),
    ('nilco_kadab', 'https://nilco-int.com/ar/product/kadab/'),
    ('nilco_3awz', 'https://nilco-int.com/ar/product/el-3awz/'),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in targets:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extract images
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE)
            valid_imgs = [img for img in imgs if not img.endswith('.svg') and ('product' in img or 'game' in img or 'cdn' in img or 'upload' in img)]
            print(f"[{name}] {url} -> found {len(valid_imgs)} candidate product images")
            for vi in valid_imgs[:4]:
                print(f"    {vi}")
    except Exception as e:
        print(f"[{name}] ERROR: {e}")
