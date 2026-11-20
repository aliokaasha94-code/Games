import urllib.request
import re

url = "https://handagames.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Handagames HTML: {len(html)} chars")
        # Find images
        links = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp|jpeg)', html)
        print("Total image links:", len(links))
        for l in sorted(set(links)):
            print("IMG:", l)
except Exception as e:
    print("Error:", e)
