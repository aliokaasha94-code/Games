import json
import os

with open('data/games.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

games = data.get('games', [])
print(f"Total games: {len(games)}")
real_count = 0
placeholder_count = 0
placeholders = []

for g in games:
    img = g.get('image', '')
    img_path = os.path.join('public', img.lstrip('/'))
    exists = os.path.exists(img_path)
    size = os.path.getsize(img_path) if exists else 0
    is_real = size > 9000
    if is_real:
        real_count += 1
    else:
        placeholder_count += 1
        placeholders.append((g['id'], g['name'], g.get('publisher'), img, size))
    status = "REAL" if is_real else "NEED_REAL"
    print(f"[{status:9s}] {g['id']:25s} | {g['name']:30s} | {size:6d} B | {g.get('publisher')}")

print("\n" + "="*50)
print(f"REAL IMAGES: {real_count}/{len(games)}")
print(f"NEEDS REAL IMAGE: {placeholder_count}/{len(games)}")
print("="*50)
for p in placeholders:
    print(f"Target: id={p[0]}, name={p[1]}, pub={p[2]}, current_img={p[3]}")
