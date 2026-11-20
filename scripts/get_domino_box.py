import urllib.request
import re

url = 'https://commons.wikimedia.org/wiki/File:A_box_of_playing_dominoes.jpg'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
imgs = re.findall(r'href=[\'"](https://upload\.wikimedia\.org/wikipedia/commons/[^\'"]+\.(?:jpg|png|webp))[\'"]', html)
print('Direct URLs:', imgs[:3])

if imgs:
    # download highest res or standard res
    img_url = imgs[0]
    print('Downloading:', img_url)
    req2 = urllib.request.Request(img_url, headers=headers)
    with urllib.request.urlopen(req2) as resp:
        with open('scratch/domino_box_wikimedia.jpg', 'wb') as f:
            f.write(resp.read())
    print('Saved scratch/domino_box_wikimedia.jpg')
