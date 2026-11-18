keywords = ["2ool", "mostakhabby", "tala3", "eyad", "mougi", "est7ala", "ramadan", "madfa3", "raw", "hanbatel"]

try:
    with open("scripts/2oolameme_imgs.txt", "r", encoding="utf-16") as f:
        text = f.read()
except Exception:
    with open("scripts/2oolameme_imgs.txt", "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

for kw in keywords:
    matches = [line for line in text.splitlines() if kw.lower() in line.lower()]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:5]:
        print("  ", m)
