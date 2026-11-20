from PIL import Image
import numpy as np
from collections import deque

def remove_outer_color_bg(img, target_color, tolerance=25):
    im_rgba = img.convert('RGBA')
    arr = np.array(im_rgba)
    h, w, _ = arr.shape
    
    target = np.array(target_color)
    diff = np.abs(arr[:, :, :3].astype(int) - target).max(axis=2)
    match_mask = (diff <= tolerance)
    
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()
    
    for x in range(w):
        if match_mask[0, x]:
            queue.append((0, x))
            visited[0, x] = True
        if match_mask[h-1, x]:
            queue.append((h-1, x))
            visited[h-1, x] = True
            
    for y in range(h):
        if match_mask[y, 0] and not visited[y, 0]:
            queue.append((y, 0))
            visited[y, 0] = True
        if match_mask[y, w-1] and not visited[y, w-1]:
            queue.append((y, w-1))
            visited[y, w-1] = True
            
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny, nx] and match_mask[ny, nx]:
                    visited[ny, nx] = True
                    queue.append((ny, nx))
                    
    arr[visited, 3] = 0
    return Image.fromarray(arr)

# Test met7awech
im_m = Image.open('public/games/met7awech.webp')
corner_m = im_m.getpixel((0, 0))[:3]
trans_m = remove_outer_color_bg(im_m, corner_m, tolerance=25)
trans_m.save('scratch/met7awech_trans.png')
print("Saved scratch/met7awech_trans.png")

# Test hareedy
im_h = Image.open('public/games/hareedy.webp')
corner_h = im_h.getpixel((0, 0))[:3]
trans_h = remove_outer_color_bg(im_h, corner_h, tolerance=20)
trans_h.save('scratch/hareedy_trans.png')
print("Saved scratch/hareedy_trans.png")
