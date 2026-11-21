import os
import json
from PIL import Image
import numpy as np

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"{'ID':28} | {'SIZE':10} | {'MODE':5} | {'TRANS %':7} | {'BBOX':25} | {'STYLE'}")
print("-" * 90)

for g in games:
    gid = g['id']
    p = os.path.join('public', g['image'].lstrip('/'))
    if not os.path.exists(p):
        print(f"MISSING: {p}")
        continue
    im = Image.open(p)
    arr = np.array(im)
    if im.mode == 'RGBA':
        alpha = arr[:, :, 3]
        trans_pct = np.mean(alpha < 10) * 100
        mask = alpha > 10
        coords = np.argwhere(mask)
        if len(coords) > 0:
            y0, x0 = coords.min(axis=0)
            y1, x1 = coords.max(axis=0)
            bbox_str = f"({x0},{y0})-({x1},{y1})"
        else:
            bbox_str = "empty"
    else:
        trans_pct = 0
        bbox_str = "full"
        
    style = "Isolated Packshot (Transparent)" if trans_pct > 15 else "Full Cover / Bled"
    print(f"{gid:28} | {str(im.size):10} | {im.mode:5} | {trans_pct:6.1f}% | {bbox_str:25} | {style}")
