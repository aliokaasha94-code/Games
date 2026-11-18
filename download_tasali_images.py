import os
import ssl
import urllib.request
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

tasali_map = {
    "tasali-3andalib": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/3ANDALIB.png?v=1778575716",
    "tasali-cinema": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/CINEMA2Y.png?v=1778575716",
    "tasali-haqeeqa": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/ha2e2awlakhaialmockup_25202fd2-53f2-4047-b339-f1b23889ced9.png?v=1747754890",
    "tasali-system": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/System_box.png?v=1747755096",
    "tasali-dehk": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/kalamfadymockup_8e4bf4a1-974d-409e-b66d-48e0b0d63507.png?v=1747754890",
    "tasali-kelma-khatar": "https://cdn.shopify.com/s/files/1/0721/9822/6214/files/KELMAKHATAR.png?v=1778575716",
}

def make_square_webp(img: Image.Image, target_size=600) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    max_dim = max(w, h)
    
    # Check corner transparency or color
    corners = [img.getpixel((0, 0)), img.getpixel((w-1, 0)), img.getpixel((0, h-1)), img.getpixel((w-1, h-1))]
    if corners[0][3] < 50:
        bg_color = (0, 0, 0, 0)
    else:
        bg_color = (255, 255, 255, 255)
        
    sq = Image.new("RGBA", (max_dim, max_dim), bg_color)
    paste_x = (max_dim - w) // 2
    paste_y = (max_dim - h) // 2
    sq.paste(img, (paste_x, paste_y), img if img.mode == 'RGBA' else None)
    return sq.resize((target_size, target_size), Image.Resampling.LANCZOS)

for slug, url in tasali_map.items():
    try:
        print(f"Downloading {slug}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            raw = r.read()
        im = Image.open(io.BytesIO(raw))
        sq = make_square_webp(im, 600)
        out_path = f"public/games/{slug}.webp"
        sq.convert("RGB").save(out_path, "WEBP", quality=88)
        print(f"Saved {out_path} ({os.path.getsize(out_path)} bytes)")
    except Exception as e:
        print(f"Error {slug}: {e}")

print("All Tasali games downloaded and converted!")
