from PIL import Image
import numpy as np

im = Image.open('downloads_official/domino_raw.jpg')
W, H = im.size
print("Domino raw size:", W, H)

# Find non-white pixels
arr = np.array(im.convert('RGB'))
# The background is white (r,g,b > 245)
mask = (arr < 240).any(axis=2)
coords = np.argwhere(mask)
if len(coords):
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    print(f"Content bbox: x={x0}..{x1} (w={x1-x0}), y={y0}..{y1} (h={y1-y0})")
    
    # Crop tightly with small margin (10%)
    margin = int((x1 - x0) * 0.1)
    crop_x0 = max(0, x0 - margin)
    crop_y0 = max(0, y0 - margin)
    crop_x1 = min(W, x1 + margin)
    crop_y1 = min(H, y1 + margin)
    
    cropped = im.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    cropped.save('scratch/domino_tight_crop.jpg')
    print("Saved scratch/domino_tight_crop.jpg:", cropped.size)
