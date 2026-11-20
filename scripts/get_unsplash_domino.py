import urllib.request
import re

url = "https://unsplash.com/photos/a-close-up-of-a-game-of-dominos-on-a-table-K9r9T9Ww-w4"
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    imgs = re.findall(r'https://images\.unsplash\.com/[^\s"\'<>]+', html)
    print("Found images:", len(imgs))
    for im in set(imgs):
        if 'photo-' in im:
            print("Direct photo:", im[:120])
            # download
            req2 = urllib.request.Request(im.split('?')[0] + '?w=1000&auto=format&fit=crop&q=85', headers=headers)
            with urllib.request.urlopen(req2) as resp:
                with open('scratch/domino_unsplash.jpg', 'wb') as f:
                    f.write(resp.read())
            print("Saved scratch/domino_unsplash.jpg")
            break
except Exception as e:
    print("Error:", e)
