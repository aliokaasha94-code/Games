import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def search_nilco(keyword):
    url = f"https://nilco-int.com/?s={urllib.parse.quote(keyword)}&post_type=product"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # find product images and titles
            matches = re.findall(r'<img[^>]+src=["\'](https://nilco-int\.com/wp-content/uploads/[^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
            print(f"Results for '{keyword}': {len(matches)}")
            for src, alt in matches:
                print(f"  {alt}: {src}")
    except Exception as e:
        print(f"Error {url}: {e}")

search_nilco("kadab")
search_nilco("كداب")
search_nilco("العوز")
