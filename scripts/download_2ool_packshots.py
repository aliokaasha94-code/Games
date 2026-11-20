import requests
from PIL import Image
import os

os.makedirs('public/games/official_raw', exist_ok=True)

targets = {
    'mesh-mertahlak': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/files/1_afe3f82a-04fa-41f4-92b6-badc636853cf.png?v=1775228371',
    'kelmet-el-ser-mostathmer': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/files/Artboard.1.png?v=1741707357',
    'el-le3ba-el-qadya': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/files/Main.png?v=1728053163',
    'wala3a': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/products/wala3agame.png?v=1716284290',
    '2ool-aw-e3mel': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/products/2oolawe3melegypt.webp?v=1716284222',
    'ana-mesh-arafny': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/products/anamsh3arefni2oolameme.jpg?v=1716284172',
    'autobeez': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/files/Untitleddesign.png?v=1768310352',
    'byegy-menno': 'https://cdn.shopify.com/s/files/1/0721/9822/6214/files/IMG_5092.jpg?v=1716284480'
}

for gid, url in targets.items():
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if r.status_code == 200:
            raw_path = f"public/games/official_raw/{gid}.raw"
            with open(raw_path, 'wb') as f:
                f.write(r.content)
            
            im = Image.open(raw_path)
            print(f"Downloaded {gid}: {im.size}, mode={im.mode}")
            
            # Process to Amazon e-commerce square
            # If RGBA, crop bbox
            if im.mode == 'RGBA':
                bbox = im.split()[-1].getbbox()
                if bbox:
                    im = im.crop(bbox)
            
            w, h = im.size
            target = 800
            usable = 680
            scale = min(usable / w, usable / h)
            nw, nh = int(w * scale), int(h * scale)
            resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
            
            # Place on transparent canvas
            canvas = Image.new('RGBA', (target, target), (0, 0, 0, 0))
            if resized.mode == 'RGBA':
                canvas.paste(resized, ((target - nw) // 2, (target - nh) // 2), resized)
            else:
                canvas.paste(resized.convert('RGBA'), ((target - nw) // 2, (target - nh) // 2))
            
            out_webp = f"public/games/{gid}.webp"
            canvas.save(out_webp, 'WEBP', quality=92)
            print(f"Updated {out_webp} to official studio packshot!")
    except Exception as e:
        print(f"Error {gid}: {e}")
