import os
import json
from PIL import Image
import numpy as np

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"Auditing all {len(games)} processed game images in public/games/...")
print(f"{'ID':<26} {'FILE':<22} {'SIZE':<9} {'MODE':<5} {'FILL%':<6} {'STATUS'}")
print("-" * 80)

issues = []
for g in games:
    gid = g['id']
    rel_p = g['image'].lstrip('/')
    p = os.path.join('public', rel_p)
    if not os.path.exists(p):
        issues.append(f"MISSING: {p}")
        continue
        
    im = Image.open(p)
    w, h = im.size
    mode = im.mode
    
    if (w, h) != (800, 800):
        issues.append(f"{gid}: size is {w}x{h}, expected 800x800")
        
    # Check alpha or background
    if 'A' in mode:
        arr = np.array(im)
        mask = (arr[:, :, 3] > 10)
        coords = np.argwhere(mask)
        if len(coords):
            y0, x0 = coords.min(axis=0)
            y1, x1 = coords.max(axis=0)
            fill = (x1 - x0) * (y1 - y0) / (w * h) * 100
        else:
            fill = 0
        status = "TRANSPARENT_OK"
    else:
        # Full bleed photo
        arr = np.array(im.convert('RGB'))
        # Check border variance
        top = arr[0, :, :]
        bot = arr[-1, :, :]
        left = arr[:, 0, :]
        right = arr[:, -1, :]
        
        # Check if any border is pure solid letterbox
        tb_black = np.all(top < 20) and np.all(bot < 20) and not np.all(left < 20)
        lr_black = np.all(left < 20) and np.all(right < 20) and not np.all(top < 20)
        tb_white = np.all(top > 245) and np.all(bot > 245) and not np.all(left > 245)
        lr_white = np.all(left > 245) and np.all(right > 245) and not np.all(top > 245)
        
        fill = 100.0
        if tb_black or lr_black or tb_white or lr_white:
            status = "LETTERBOX_FOUND"
            issues.append(f"{gid}: has letterbox border")
        else:
            status = "FULL_BLEED_OK"
            
    print(f"{gid:<26} {os.path.basename(p):<22} {w}x{h:<5} {mode:<5} {fill:4.1f}%  {status}")

print("-" * 80)
if issues:
    print(f"Found {len(issues)} ISSUES:")
    for iss in issues:
        print("  -", iss)
else:
    print(f"PERFECT! All {len(games)} images pass 100% verification with ZERO issues!")
