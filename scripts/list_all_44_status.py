import json

with open('data/games.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total games: {len(d['games'])}")
for g in d['games']:
    print(f"{g['id']:25} | {g['name']:25} | {g['publisher']:22} | {g['image']}")
