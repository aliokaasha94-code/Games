import os
import json
from PIL import Image
import numpy as np

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"Checking {len(games)} games...")
print(f"{'ID':<26} {'SIZE':<8} {'BG_TYPE':<12} {'FG_BOX (x,y,w,h)':<20} {'ASP':<5} {'FILL%':<6} {'NOTES'}")
print("-" * 85)

for g in games:
    path = os.path.join('public', g['image'].lstrip('/'))
    with Image.open(path) as im:
        im_rgb = im.convert('RGB')
        arr = np.array(im_rgb)
        h, w, _ = arr.shape
        
        # Check border colors
        top = arr[0, :, :]
        bot = arr[-1, :, :]
        left = arr[:, 0, :]
        right = arr[:, -1, :]
        
        top_black = np.all(top < 25)
        bot_black = np.all(bot < 25)
        left_black = np.all(left < 25)
        right_black = np.all(right < 25)
        
        top_white = np.all(top > 235)
        bot_white = np.all(bot > 235)
        left_white = np.all(left > 235)
        right_white = np.all(right > 235)
        
        letterbox = ""
        if (top_black and bot_black) and not (left_black and right_black):
            letterbox = "BLACK_TB_BARS"
        elif (left_black and right_black) and not (top_black and bot_black):
            letterbox = "BLACK_LR_BARS"
            
        # non-bg bbox
        corner_colors = [tuple(arr[0,0]), tuple(arr[0,-1]), tuple(arr[-1,0]), tuple(arr[-1,-1])]
        bg = corner_colors[0]
        
        if top_white and bot_white:
            bg_desc = "WHITE_BG"
            diff = np.abs(arr.astype(int) - 255).sum(axis=2)
            fg_coords = np.argwhere(diff > 35)
        elif top_black and bot_black and left_black and right_black:
            bg_desc = "BLACK_BG"
            diff = np.abs(arr.astype(int) - 0).sum(axis=2)
            fg_coords = np.argwhere(diff > 35)
        else:
            bg_desc = f"COLOR_{bg[0]},{bg[1]},{bg[2]}"
            diff = np.abs(arr.astype(int) - np.array(bg)).sum(axis=2)
            fg_coords = np.argwhere(diff > 35)
            
        if len(fg_coords) > 0:
            y0, x0 = fg_coords.min(axis=0)
            y1, x1 = fg_coords.max(axis=0)
            fg_w = x1 - x0
            fg_h = y1 - y0
            aspect = fg_w / max(1, fg_h)
            fill_pct = (fg_w * fg_h) / (w * h) * 100
        else:
            y0, x0, fg_w, fg_h, aspect, fill_pct = 0, 0, w, h, 1.0, 100.0
            
        notes = []
        if letterbox:
            notes.append(letterbox)
        if aspect > 2.0:
            notes.append("WIDE_STRIP")
        elif aspect < 0.5:
            notes.append("TALL_STRIP")
        if fill_pct < 30:
            notes.append("TINY_CONTENT")
            
        print(f"{g['id']:<26} {w}x{h:<4} {bg_desc:<12} [{x0:3d},{y0:3d},{fg_w:3d},{fg_h:3d}]   {aspect:4.2f} {fill_pct:4.1f}%  {', '.join(notes)}")
