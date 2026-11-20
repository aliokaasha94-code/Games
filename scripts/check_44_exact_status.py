import json
import os
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

print(f"{'GAME ID':28} | {'SIZE':10} | {'MODE':5} | {'BG STATUS'}")
print("-" * 65)

for g in games:
    gid = g['id']
    p = os.path.join('public', g['image'].lstrip('/'))
    if not os.path.exists(p):
        print(f"{gid:28} | MISSING!")
        continue
    im = Image.open(p)
    if im.mode == 'RGBA':
        bbox = im.split()[-1].getbbox()
        print(f"{gid:28} | {str(im.size):10} | RGBA  | Clean Transparent (bbox={bbox})")
    else:
        tl = im.getpixel((0,0))
        br = im.getpixel((im.width-1, im.height-1))
        print(f"{gid:28} | {str(im.size):10} | RGB   | Solid TL={tl} BR={br}")
