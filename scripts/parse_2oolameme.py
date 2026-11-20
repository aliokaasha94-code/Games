with open('scripts/2oolameme_imgs.txt', 'r', encoding='utf-16') as f:
    text = f.read()

lines = text.splitlines()
current_game = ""
games_dict = {}
for l in lines:
    if l.startswith("=== "):
        current_game = l.strip()
        games_dict[current_game] = []
    elif l.strip().startswith("http") and current_game:
        games_dict[current_game].append(l.strip())

print(f"Total games in 2oolameme: {len(games_dict)}")
for g, imgs in games_dict.items():
    print(f"{g}: {len(imgs)} images")
    if imgs:
        print(f"   First: {imgs[0]}")
