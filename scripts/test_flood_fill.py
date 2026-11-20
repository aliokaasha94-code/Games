from PIL import Image
import numpy as np
from collections import deque

def remove_outer_bg(img, bg_is_white=True, tolerance=25):
    # Convert to RGBA
    im_rgba = img.convert('RGBA')
    arr = np.array(im_rgba)
    h, w, _ = arr.shape
    
    # Target color: 255, 255, 255 if white, 0, 0, 0 if black
    target = np.array([255, 255, 255] if bg_is_white else [0, 0, 0])
    
    # Compute color distance from target for all pixels
    diff = np.abs(arr[:, :, :3].astype(int) - target).max(axis=2)
    match_mask = (diff <= tolerance)
    
    # BFS flood fill from all 4 borders
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()
    
    # Add border pixels that match target
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
                    
    # Now visited contains the contiguous outer background
    # Set alpha of visited to 0
    arr[visited, 3] = 0
    return Image.fromarray(arr)

# Test on kadab
im_kadab = Image.open('public/games/kadab.webp')
transparent_kadab = remove_outer_bg(im_kadab, bg_is_white=True, tolerance=20)
transparent_kadab.save('scratch/kadab_transparent.png')
print("Saved scratch/kadab_transparent.png")

# Test on tasali-cinema
im_cinema = Image.open('public/games/tasali-cinema.webp')
transparent_cinema = remove_outer_bg(im_cinema, bg_is_white=False, tolerance=15)
transparent_cinema.save('scratch/cinema_transparent.png')
print("Saved scratch/cinema_transparent.png")
