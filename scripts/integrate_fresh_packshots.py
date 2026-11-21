import cv2
import numpy as np
from PIL import Image
import os

items = [
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/raz3_el_gomhoor_packshot_1795234558441.jpg',
        'public/games/raz3-el-gomhoor.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/arosty_game_box_packshot_1795234585623.jpg',
        'public/games/3arosty.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/el_joker_card_game_box_1795234609917.jpg',
        'public/games/el-joker.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/egyptian_trivia_box_packshot_1795234633817.jpg',
        'public/games/mawsoo3at.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/tomouhy_card_game_packshot_1795234657422.jpg',
        'public/games/tomouhy.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/tala3_el_mostakhabby_packshot_1795234686799.jpg',
        'public/games/tala3-el-mostakhabby.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/egyptian_party_game_box_packshot_1795234722137.jpg',
        'public/games/msh-hanbatel.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/est7ala_card_game_packshot_1795234747424.jpg',
        'public/games/est7ala.webp'
    ),
    (
        r'C:/Users/user/.gemini/antigravity/brain/0e585059-d206-4832-98ff-eb24e7296108/ramadan_game_packshot_1795234769266.jpg',
        'public/games/tasali-ramadan.webp'
    ),
]

for src, out in items:
    if not os.path.exists(src):
        print(f"Skipping missing {src}")
        continue
    
    img = cv2.imread(src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Corners are light studio background (> 180)
    # Box is the main subject
    mask = (gray < 200).astype(np.uint8) * 255
    
    # Find largest component
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
    if num_labels > 1:
        largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        clean_mask = (labels == largest_label).astype(np.uint8) * 255
    else:
        clean_mask = mask
        
    # Fill holes inside the box
    contours, _ = cv2.findContours(clean_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_mask = np.zeros_like(clean_mask)
    cv2.drawContours(filled_mask, contours, -1, 255, -1)
    
    # Soft edge feather
    filled_mask = cv2.GaussianBlur(filled_mask, (5, 5), 0)
    
    rgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    rgba[:, :, 3] = filled_mask
    
    pil_im = Image.fromarray(rgba)
    bbox = pil_im.getbbox()
    if bbox:
        cropped = pil_im.crop(bbox)
    else:
        cropped = pil_im
        
    target = 800
    usable = 680
    w, h = cropped.size
    scale = min(usable / w, usable / h)
    nw, nh = int(w * scale), int(h * scale)
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (target, target), (0, 0, 0, 0))
    canvas.paste(resized, ((target - nw) // 2, (target - nh) // 2), resized)
    canvas.save(out, 'WEBP', quality=95)
    print(f"Successfully processed {out} -> (800x800 RGBA, bbox={canvas.getbbox()})")

print("All fresh 3D Amazon-grade packshots integrated!")
