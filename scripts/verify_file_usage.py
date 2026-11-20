import json
import os

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

images_used = set()
for g in games:
    p = g['image'].lstrip('/')
    images_used.add(p)

print(f"Total unique images referenced by games: {len(images_used)}")
all_files = [f"games/{f}" for f in os.listdir("public/games")]
print(f"Total files in public/games: {len(all_files)}")

extra = set(all_files) - images_used
print("Extra unreferenced files:", extra)
missing = images_used - set(all_files)
print("Missing files:", missing)
