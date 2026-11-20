import os
import glob
from PIL import Image

def analyze_images():
    for p in sorted(glob.glob('public/games/*.webp')):
        im = Image.open(p)
        name = os.path.basename(p)
        if im.mode == 'RGBA':
            # Count transparent pixels
            alpha = im.split()[-1]
            hist = alpha.histogram()
            trans_pct = (hist[0] / (im.width * im.height)) * 100
            print(f"{name:30} | RGBA | transparent: {trans_pct:.1f}%")
        else:
            print(f"{name:30} | RGB  | corners: TL={im.getpixel((0,0))} BR={im.getpixel((im.width-1,im.height-1))}")

if __name__ == '__main__':
    analyze_images()
