import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request("https://handagames.com", headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Successfully reached handagames.com")
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        print(f"Found {len(imgs)} images on homepage:")
        for im in imgs[:10]:
            print(" ", im)
except Exception as e:
    print(f"Error handagames: {e}")
