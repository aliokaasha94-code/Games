from PIL import Image
import numpy as np
import sys
sys.path.append('scripts')
from test_flood_fill import remove_outer_bg

im = Image.open('public/games/casino-al3ab.webp')
W, H = im.size
# Left box is roughly x=0 to x=int(W*0.52)
front_box = im.crop((0, 0, int(W * 0.52), H))
front_box.save('scratch/casino_front.png')

trans = remove_outer_bg(front_box, bg_is_white=True, tolerance=20)
# Find non-transparent bbox
arr = np.array(trans)
mask = (arr[:, :, 3] > 0)
coords = np.argwhere(mask)
y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0)
cropped = trans.crop((x0, y0, x1, y1))

# Center in 800x800 with 10% padding
canvas = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
usable = int(800 * 0.82)
scale = min(usable / cropped.size[0], usable / cropped.size[1])
nw = int(cropped.size[0] * scale)
nh = int(cropped.size[1] * scale)
resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
canvas.paste(resized, ((800 - nw) // 2, (800 - nh) // 2), mask=resized)
canvas.save('scratch/casino_card_test.webp', 'WEBP', quality=90)
print("Saved scratch/casino_card_test.webp")
