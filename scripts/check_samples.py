import os
import json
from PIL import Image

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

# Let's inspect some sample games:
sample_ids = [
    '2ool-aw-e3mel',
    'couples-walaken',
    'kadab',
    '2oolameme-2',
    'kataflam',
    'shake-me',
    'tasali-aflam',
    'khufu',
    'starting-chess',
    'original-domino'
]

for gid in sample_ids:
    g = next(x for x in games if x['id'] == gid)
    p = os.path.join('public', g['image'].lstrip('/'))
    im = Image.open(p)
    print(f"{gid:<25} size={im.size} mode={im.mode}")
