import urllib.request
import json
import re

query = 'وراء الجريمة فندق الدم'
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # find links
        links = re.findall(r'<a[^>]+class="result__url"[^>]*href="([^"]+)"', html)
        print("Found links:", len(links))
        for l in links[:10]:
            print(" ", l.strip())
except Exception as e:
    print("Error:", e)
