import os
from PIL import Image
import numpy as np

solid_games = [
    'public/games/shake-me.webp',
    'public/games/tala3-el-mostakhabby.webp',
    'public/games/kataflam.webp',
    'public/games/couples-walaken.webp',
    'public/games/mawada-w-rahma.webp',
    'public/games/qabl-el-hewar.webp',
    'public/games/pick-a-date.webp',
    'public/games/girls-walaken.webp',
    'public/games/waraa-el-gareema.webp',
    'public/games/mansa.webp',
    'public/games/skrew.webp'
]

def remove_solid_bg(img_path, tolerance=35):
    im = Image.open(img_path).convert('RGBA')
    w, h = im.size
    
    # Get corner colors
    corners = [
        im.getpixel((0, 0)),
        im.getpixel((w - 1, 0)),
        im.getpixel((0, h - 1)),
        im.getpixel((w - 1, h - 1))
    ]
    # Average corner color (RGB)
    avg_r = sum(c[0] for c in corners) // 4
    avg_g = sum(c[1] for c in corners) // 4
    avg_b = sum(c[2] for c in corners) // 4
    
    data = np.array(im)
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Distance to corner color
    dist = np.sqrt((r.astype(float) - avg_r)**2 + (g.astype(float) - avg_g)**2 + (b.astype(float) - avg_b)**2)
    
    # Mask where distance < tolerance
    mask = dist < tolerance
    
    # Flood-fill from borders to only remove connected background
    # (keeps any similar colors inside the box art safe)
    import cv2
    cv_mask = mask.astype(np.uint8) * 255
    h_cv, w_cv = cv_mask.shape
    flood_mask = np.zeros((h_cv + 2, w_cv + 2), np.uint8)
    
    # Flood fill from each corner
    bg_connected = np.zeros((h_cv, w_cv), np.uint8)
    for seed in [(0, 0), (w_cv - 1, 0), (0, h_cv - 1), (w_cv - 1, h_cv - 1)]:
        if cv_mask[seed[1], seed[0]] == 255:
            cv2.floodFill(cv_mask, flood_mask, seed, 128)
    
    bg_connected = (cv_mask == 128)
    data[:, :, 3][bg_connected] = 0
    
    result = Image.fromarray(data, 'RGBA')
    bbox = result.split()[-1].getbbox()
    if bbox:
        cropped = result.crop(bbox)
        # Pad to square 800x800
        target = 800
        usable = 680
        cw, ch = cropped.size
        scale = min(usable / cw, usable / ch)
        nw, nh = int(cw * scale), int(ch * scale)
        resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas = Image.new('RGBA', (target, target), (0, 0, 0, 0))
        canvas.paste(resized, ((target - nw) // 2, (target - nh) // 2))
        canvas.save(img_path, 'WEBP', quality=92)
        print(f"Isolated {img_path}: new bbox={canvas.split()[-1].getbbox()}")
    else:
        print(f"Could not find bbox for {img_path}")

for p in solid_games:
    if os.path.exists(p):
        remove_solid_bg(p)
