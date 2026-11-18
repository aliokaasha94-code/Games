import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request("https://handagames.com", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    # find all links on page
    links = re.findall(r'href=["\'](https://handagames\.com/[^"\']+)["\']', html)
    print(f"Links on homepage: {len(links)}")
    for l in set(links):
        print(" ", l)
