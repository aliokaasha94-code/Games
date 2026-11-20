with open('scripts/nilco_catalog.txt', 'r', encoding='utf-16', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
print(f"Total lines in nilco_catalog.txt: {len(lines)}")
for l in lines:
    if any(k in l for k in ['chess', 'domino', 'kadab', 'ew3a', 'sahseh', 'شطرنج', 'كذاب', 'كداب', 'عروستي', 'إوعى']):
        print(l[:150])
