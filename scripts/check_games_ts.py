import re

with open('src/data/games.ts', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'image:\s*[\'"]([^\'"]+)[\'"]', text)
print(f"Total images in src/data/games.ts: {len(imgs)}")
