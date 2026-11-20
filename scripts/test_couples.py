from PIL import Image
from test_auto_crop_letterbox import crop_white_borders

im = Image.open('public/games/couples-walaken.webp')
cropped = crop_white_borders(im)
cw, ch = cropped.size
side = min(cw, ch)
x_off = (cw - side) // 2
y_off = (ch - side) // 2
square = cropped.crop((x_off, y_off, x_off + side, y_off + side)).resize((800, 800), Image.Resampling.LANCZOS)
square.save('scratch/couples_walaken_square.webp', 'WEBP', quality=90)
print("Saved scratch/couples_walaken_square.webp")
