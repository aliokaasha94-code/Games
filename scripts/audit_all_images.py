import json
import os
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

games = data['games']
print(f"Total games in data/games.json: {len(games)}")

results = []
for g in games:
    gid = g['id']
    name = g['name']
    img_rel = g.get('image', '').lstrip('/')
    full_path = os.path.join('public', img_rel)
    
    if not os.path.exists(full_path):
        print(f"MISSING: {gid} -> {full_path}")
        continue
        
    with Image.open(full_path) as im:
        w, h = im.size
        mode = im.mode
        aspect = w / h
        
        # Check border colors (top, bottom, left, right)
        # Convert to RGB to analyze pixels
        rgb_im = im.convert('RGB')
        pixels = rgb_im.load()
        
        # Sample border pixels
        corners = [pixels[0, 0], pixels[w-1, 0], pixels[0, h-1], pixels[w-1, h-1]]
        top_edge = [pixels[x, 0] for x in range(0, w, max(1, w//10))]
        bottom_edge = [pixels[x, h-1] for x in range(0, w, max(1, w//10))]
        left_edge = [pixels[0, y] for y in range(0, h, max(1, h//10))]
        right_edge = [pixels[w-1, y] for y in range(0, h, max(1, h//10))]
        
        # Check if borders are pure black or near black (letterbox)
        def is_dark(rgb, threshold=30):
            return all(c < threshold for c in rgb)
            
        def is_white(rgb, threshold=240):
            return all(c > threshold for c in rgb)

        dark_borders = all(is_dark(c) for c in corners)
        white_borders = all(is_white(c) for c in corners)
        
        top_dark = all(is_dark(c) for c in top_edge)
        bottom_dark = all(is_dark(c) for c in bottom_edge)
        
        has_alpha = ('A' in mode)
        
        status = "OK"
        if aspect > 1.8 or aspect < 0.5:
            status = "STRANGE_ASPECT"
        elif top_dark and bottom_dark and not (is_dark(left_edge[0]) and is_dark(right_edge[0]) and all(is_dark(c) for c in left_edge)):
            status = "LETTERBOX_TB"
        elif is_dark(corners[0]) and not has_alpha:
            status = "DARK_BG"
        elif is_white(corners[0]):
            status = "WHITE_BG"
            
        results.append({
            "id": gid,
            "name": name,
            "file": img_rel,
            "size": f"{w}x{h}",
            "aspect": round(aspect, 2),
            "mode": mode,
            "corners": corners[0],
            "status": status,
            "top_dark": top_dark,
            "bottom_dark": bottom_dark,
            "has_alpha": has_alpha
        })

print(f"{'ID':<28} {'SIZE':<10} {'ASPECT':<6} {'MODE':<5} {'ALPHA':<5} {'CORNER_RGB':<15} {'STATUS'}")
print("-" * 85)
for r in results:
    print(f"{r['id']:<28} {r['size']:<10} {r['aspect']:<6} {r['mode']:<5} {str(r['has_alpha']):<5} {str(r['corners']):<15} {r['status']}")

print("\n--- Summary of potential problematic images ---")
for r in results:
    if r['status'] in ['STRANGE_ASPECT', 'LETTERBOX_TB'] or 'joker' in r['id'] or 'waraa' in r['id'] or r['aspect'] > 1.4 or r['aspect'] < 0.7:
        print(f"Problem: {r['id']} ({r['file']}) -> size={r['size']}, aspect={r['aspect']}, status={r['status']}")
