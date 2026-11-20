import re
import json

with open('scripts/nilco_catalog.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

titles = re.findall(r'"title":\s*"([^"]+)"', text)
print(f"Total Nilco titles: {len(titles)}")
for t in set(titles):
    if any(k in t for k in ['كذاب', 'كداب', 'شطرنج', 'عروستي', 'مستخبي', 'إوعى', 'دومينو', 'تحدي', 'مستور']):
        print('Nilco match:', t)
