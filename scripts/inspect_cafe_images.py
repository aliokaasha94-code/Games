import os
from PIL import Image

image_dir = 'Image'
for fname in os.listdir(image_dir):
    fpath = os.path.join(image_dir, fname)
    if os.path.isfile(fpath) and fname.lower().endswith(('.jpeg', '.jpg', '.png')):
        im = Image.open(fpath)
        print(f"{fname}: size={im.size}, mode={im.mode}, filesize={os.path.getsize(fpath)} bytes")
