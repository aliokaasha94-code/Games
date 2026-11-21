import urllib.request
import re
import json

req = urllib.request.Request('https://3dicons.co/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https://bvconuycpdvgzbvbkijl\.supabase\.co/storage/v1/object/public/sizes/([^/]+)/dynamic/200/([^.]+)\.webp', html)
        print("Total 3dicons entries found:", len(matches))
        for m in sorted(set(matches)):
            print(f"Slug: {m[0]} | Style: {m[1]}")
except Exception as e:
    print("Error:", e)
