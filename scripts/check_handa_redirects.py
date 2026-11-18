import urllib.request
import re

urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBjLb-YegJlCpjxF8VCKt_fQDDoQ-7eR6XLog3jOjlMQShbOI9elRmfNmEdVTJvjq_8FUN6f5eOowmc88v_io7StiAA8a_36hMSmv-tQ==",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqPHpceotAWW_eEXVZ8FPmMerBDGjWWYuenpnZx4ShIYbqwQ-ix53nQyN-YXIZjqMmk168q548mYkxAjOT9VaNisHMdxdsFcGmJ8ETiOmKbX4=="
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            print("Redirects to:", resp.geturl())
            data = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:webp|jpg|png)', data)
            print("Found images:", imgs[:5])
    except Exception as e:
        print("Error:", e)
