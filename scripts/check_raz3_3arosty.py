import json

with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)['games']

for g in games:
    if g['id'] in ['raz3-el-gomhoor', '3arosty', 'mawsoo3at-al-ma3refa']:
        print(f"ID: {g['id']}")
        print(f"  Name: {g['name']}")
        print(f"  Publisher: {g.get('publisher')}")
        print(f"  Tagline: {g.get('tagline')}")
        print(f"  Image: {g.get('image')}")
