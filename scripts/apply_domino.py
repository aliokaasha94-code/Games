import urllib.request
import os
from PIL import Image
from process_ecommerce_image import process_to_ecommerce_square

headers = {'User-Agent': 'EmadAfandiGamesHub/1.0 (contact: aliokasha@gmail.com)'}
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Domino_Piece_isolated_on_White_Background.jpg/800px-Domino_Piece_isolated_on_White_Background.jpg"
out_raw = "downloads_official/domino_raw.jpg"

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp, open(out_raw, 'wb') as f:
    f.write(resp.read())

print("Downloaded Domino raw:", os.path.getsize(out_raw), "bytes")
out_webp = "public/games/original-domino.webp"
process_to_ecommerce_square(out_raw, out_webp, target_size=800, bg_color=(255, 255, 255))
print(f"Generated {out_webp} ({os.path.getsize(out_webp)} bytes)")
