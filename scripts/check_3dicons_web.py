import urllib.request
import re

req = urllib.request.Request('https://3dicons.co/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Fetched 3dicons.co length:", len(html))
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:png|webp)', html)
        print("Found images:", len(imgs))
        for img in sorted(set(imgs))[:25]:
            print(" ", img)
except Exception as e:
    print("Error:", e)
