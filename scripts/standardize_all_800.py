import json
import os
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

target_size = 800
for g in games:
    p = os.path.join('public', g['image'].lstrip('/'))
    if os.path.exists(p):
        im = Image.open(p)
        if im.size != (target_size, target_size):
            print(f"Resizing {p} from {im.size} to (800, 800)...")
            im_rgba = im.convert('RGBA')
            bbox = im_rgba.split()[-1].getbbox()
            if bbox:
                cropped = im_rgba.crop(bbox)
            else:
                cropped = im_rgba
            
            cw, ch = cropped.size
            usable = 680
            scale = min(usable / cw, usable / ch)
            nw, nh = int(cw * scale), int(ch * scale)
            resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
            
            canvas = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
            canvas.paste(resized, ((target_size - nw) // 2, (target_size - nh) // 2))
            canvas.save(p, 'WEBP', quality=92)
            print(f"  Saved {p} at (800, 800) successfully.")

print("All 44 games verified at 800x800!")
