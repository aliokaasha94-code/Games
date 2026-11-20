import os
import json
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

for i, g in enumerate(games, 1):
    path = os.path.join('public', g['image'].lstrip('/'))
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    im = Image.open(path) if exists else None
    dims = f"{im.size[0]}x{im.size[1]}" if im else "N/A"
    mode = im.mode if im else "N/A"
    print(f"{i:2d}. {g['id']:<26} {dims:<10} {mode:<5} {size//1024:3d}KB {g['image']}")
