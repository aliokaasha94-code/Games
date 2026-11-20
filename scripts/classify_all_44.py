import json
import os
from PIL import Image
import numpy as np

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"Total games: {len(games)}")

for i, g in enumerate(games, 1):
    gid = g['id']
    rel_p = g['image'].lstrip('/')
    p = os.path.join('public', rel_p)
    im = Image.open(p)
    w, h = im.size
    arr = np.array(im.convert('RGB'))
    
    # Corner sample
    tl = arr[0, 0]
    tr = arr[0, -1]
    bl = arr[-1, 0]
    br = arr[-1, -1]
    
    is_white = all(np.all(c > 240) for c in [tl, tr, bl, br])
    is_black = all(np.all(c < 25) for c in [tl, tr, bl, br])
    
    # Check if edges are uniform
    edge_std = np.std(np.concatenate([arr[0, :, :], arr[-1, :, :], arr[:, 0, :], arr[:, -1, :]]))
    
    # Find content bounding box
    if is_white:
        mask = (arr < 240).any(axis=2)
    elif is_black:
        mask = (arr > 30).any(axis=2)
    else:
        # Diff from corner
        diff = np.abs(arr.astype(int) - tl).max(axis=2)
        mask = (diff > 30)
        
    coords = np.argwhere(mask)
    if len(coords):
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0)
        cw, ch = (x1 - x0), (y1 - y0)
        fill = (cw * ch) / (w * h) * 100
        asp = cw / max(1, ch)
    else:
        cw, ch, fill, asp = w, h, 100.0, 1.0
        
    bg_kind = "WHITE" if is_white else ("BLACK" if is_black else "COLOR/PHOTO")
    print(f"{i:2d}. {gid:<25} {w}x{h} {bg_kind:<11} box=[{cw:3d}x{ch:3d}] fill={fill:4.1f}% asp={asp:.2f} edge_std={edge_std:4.1f}")
