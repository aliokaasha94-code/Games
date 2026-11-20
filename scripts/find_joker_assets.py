import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

html = fetch('https://luciddreaminggames.com')
print(f"Home length: {len(html)}")
urls = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
joker_urls = [u for u in set(urls) if 'joker' in u.lower()]
print("Joker URLs:", joker_urls)

for ju in joker_urls:
    print(f"\nFetching {ju}...")
    j_html = fetch(ju)
    print(f"Page length: {len(j_html)}")
    j_imgs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', j_html)
    for img in set(j_imgs):
        if any(ext in img.lower() for ext in ['.jpg', '.png', '.webp']):
            print("  Image on Joker page:", img)

