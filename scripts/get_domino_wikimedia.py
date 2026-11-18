import urllib.request
import re

url = "https://commons.wikimedia.org/wiki/File:Domino_Piece_isolated_on_White_Background.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        imgs = re.findall(r'href="(https://upload\.wikimedia\.org/wikipedia/commons/[^"]+)"', html)
        print("Upload URLs:", imgs[:3])
except Exception as e:
    print("Error:", e)
