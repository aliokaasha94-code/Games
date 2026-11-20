import re

with open('scripts/nilco_catalog.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

keywords = ['kadab', '3awz', 'chess', 'domino', 'كذاب', 'شطرنج', 'دومينو', 'العوز']
for kw in keywords:
    matches = re.findall(rf'.{{0,50}}{kw}.{{0,100}}', text, re.IGNORECASE)
    print(f"Keyword '{kw}' matches: {len(matches)}")
    for m in matches[:3]:
        print("  ", m.strip())
