import re

with open('scratch/handa_home.html', 'r', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'https?://[^\s"\'<>]+', text)
for u in set(urls):
    if any(k in u.lower() for k in ['salla', 'handa', 'product', 'item']):
        print(u)
