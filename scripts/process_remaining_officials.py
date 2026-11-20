import os
from PIL import Image

def process_packshot(src_path, out_path):
    im = Image.open(src_path)
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
    canvas = Image.new('RGBA', (target, target), (0, 0, 0, 0))
    if resized.mode == 'RGBA':
        canvas.paste(resized, ((target - nw) // 2, (target - nh) // 2), resized)
    else:
        canvas.paste(resized.convert('RGBA'), ((target - nw) // 2, (target - nh) // 2))
    canvas.save(out_path, 'WEBP', quality=92)
    print(f"Processed {out_path} from {src_path}")

targets = [
    ('downloads_official/chess_official.jpg', 'public/games/starting-chess.webp'),
    ('downloads_official/domino_raw.jpg', 'public/games/original-domino.webp'),
    ('downloads_official/kadab_official.jpg', 'public/games/kadab.webp'),
    ('downloads_official/sahseh_official.jpg', 'public/games/sahseh.webp'),
    ('downloads_official/el_3awz_official.png', 'public/games/el-3awz.webp'),
    ('downloads_official/ew3a_weshak_official.jpg', 'public/games/ew3a-weshak.webp'),
]

for src, out in targets:
    if os.path.exists(src):
        process_packshot(src, out)
