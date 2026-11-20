import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
req = urllib.request.Request('https://handagames.com', headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Search for salla product urls or cdn images
salla_imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp|jpeg)', html)
print('Salla images in html:', len(salla_imgs))
for simg in set(salla_imgs):
    if 'product' in simg or 'salla' in simg:
        print(' ', simg)

# Also check for product links
links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
for l in set(links):
    if any(k in l for k in ['product', 'p-', 'case', 'crime', 'gareema']):
        print(' Product link:', l)
