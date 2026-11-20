from PIL import Image
import numpy as np

def crop_white_borders(im, tolerance=240):
    arr = np.array(im.convert('RGB'))
    h, w, _ = arr.shape
    
    # Check columns from left
    left = 0
    while left < w and np.all(arr[:, left, :] >= tolerance):
        left += 1
        
    right = w - 1
    while right >= 0 and np.all(arr[:, right, :] >= tolerance):
        right -= 1
        
    top = 0
    while top < h and np.all(arr[top, :, :] >= tolerance):
        top += 1
        
    bottom = h - 1
    while bottom >= 0 and np.all(arr[bottom, :, :] >= tolerance):
        bottom -= 1
        
    print(f"Original {w}x{h} -> Crop box: [{left}, {top}, {right+1}, {bottom+1}]")
    cropped = im.crop((left, top, right + 1, bottom + 1))
    return cropped

im_ana = Image.open('public/games/ana-mesh-arafny.webp')
cropped_ana = crop_white_borders(im_ana)
# Resize/center crop to 800x800 square with no bars!
# To make a square: crop or fit
# If aspect is close to square (e.g. 0.8), center crop height to make 1:1
cw, ch = cropped_ana.size
side = min(cw, ch)
x_off = (cw - side) // 2
y_off = (ch - side) // 2
square_ana = cropped_ana.crop((x_off, y_off, x_off + side, y_off + side)).resize((800, 800), Image.Resampling.LANCZOS)
square_ana.save('scratch/ana_mesh_arafny_square.webp', 'WEBP', quality=90)
print("Saved scratch/ana_mesh_arafny_square.webp")
