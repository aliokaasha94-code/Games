import urllib.request
import re

url = 'https://handagames.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', html)
        print('Total images:', len(imgs))
        for img in sorted(set(imgs))[:30]:
            print(' ', img)
except Exception as e:
    print('Error:', e)
