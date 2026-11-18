import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in ["https://handagames.com/sitemap.xml", "https://handagames.com/api/v1/products", "https://handagames.com/products"]:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            print(f"URL: {url} -> {len(data)} chars")
            links = re.findall(r'<loc>(https?://[^<]+)</loc>', data)
            if links:
                print(f"  Sitemap links: {len(links)}")
                for l in links[:15]:
                    print("   ", l)
            else:
                imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:webp|jpg|png)', data)
                print(f"  Images: {len(imgs)}")
                for im in imgs[:5]:
                    print("   ", im)
    except Exception as e:
        print(f"Error {url}: {e}")
