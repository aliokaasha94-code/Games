import urllib.request
import re

url = 'https://commons.wikimedia.org/wiki/File:A_box_of_playing_dominoes.jpg'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
imgs = re.findall(r'https://upload\.wikimedia\.org/wikipedia/commons/[^\s"\'<>]+', html)
print('Found links:', len(imgs))
for l in set(imgs):
    if any(ext in l.lower() for ext in ['.jpg', '.png', '.webp']):
        print('Image link:', l)
        req2 = urllib.request.Request(l, headers=headers)
        with urllib.request.urlopen(req2) as resp:
            with open('scratch/domino_box.jpg', 'wb') as f:
                f.write(resp.read())
        print('Saved scratch/domino_box.jpg')
        break
