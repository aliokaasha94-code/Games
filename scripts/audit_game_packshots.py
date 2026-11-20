import json
import os
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"Auditing {len(games)} games for Amazon-grade presentation:")
for g in games:
    gid = g['id']
    img_path = os.path.join('public', g['image'].lstrip('/'))
    if not os.path.exists(img_path):
        print(f"MISSING: {gid} at {img_path}")
        continue
    im = Image.open(img_path)
    is_rgba = im.mode == 'RGBA'
    print(f"{gid:25} | {g['name']:20} | {im.size} | {im.mode} | is_rgba={is_rgba}")
