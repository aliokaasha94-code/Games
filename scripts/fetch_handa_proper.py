import urllib.request
import re

url = "https://handagames.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Handagames home fetched: {len(html)} chars")
        # Find images and product links
        imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|webp|jpeg))["\']', html)
        print("Images found:", len(imgs))
        for img in imgs[:15]:
            print(" ", img)
except Exception as e:
    print("Error:", e)
