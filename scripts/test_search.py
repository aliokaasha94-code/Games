import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            links = re.findall(r'href="(https?://[^"&]+)"', html)
            print(f"Results for '{query}': {len(links)} links found")
            return [l for l in links if 'duckduckgo' not in l][:10]
    except Exception as e:
        print(f"Error DDG: {e}")
        return []

print(search_ddg("لعبة كداب نيلكو site:games2egypt.com OR site:shop-ourkids.com OR site:nilco-int.com"))
