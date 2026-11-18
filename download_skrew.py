import urllib.request
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://storage.googleapis.com/bosta-files/products_images/MjUxMDAwX18yMDI1LTAxLTA2VDE0OjM0OjE1LjQ1Mlpf2LPZg9ix2Ygg2YbZitmIINmE2YjZgy5wbmc=.png'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    data = r.read()

im = Image.open(io.BytesIO(data)).convert("RGBA")
w, h = im.size
dim = max(w, h)
sq = Image.new("RGBA", (dim, dim), (255, 255, 255, 255))
sq.paste(im, ((dim - w) // 2, (dim - h) // 2), im)
sq.resize((600, 600), Image.Resampling.LANCZOS).convert("RGB").save('public/games/skrew.webp', 'WEBP', quality=88)
print("Saved official Skrew 1:1 WebP!")
