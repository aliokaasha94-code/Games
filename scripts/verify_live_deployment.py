import urllib.request

urls = [
    "https://emad-afandi-games-hub.pages.dev",
    "https://emad-afandi-games-hub.pages.dev/games/mansa.webp",
    "https://emad-afandi-games-hub.pages.dev/games/kadab.webp",
    "https://emad-afandi-games-hub.pages.dev/games/sahseh.webp",
    "https://emad-afandi-games-hub.pages.dev/games/skrew.webp",
    "https://emad-afandi-games-hub.pages.dev/manifest.json",
    "https://emad-afandi-games-hub.pages.dev/sw.js",
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content_type = resp.headers.get('Content-Type')
            content_len = len(resp.read())
            print(f"[{resp.status}] {u} -> type={content_type}, size={content_len} bytes")
    except Exception as e:
        print(f"Error {u}: {e}")
