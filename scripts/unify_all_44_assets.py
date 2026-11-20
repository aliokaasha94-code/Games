import os
import shutil
import json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from collections import deque

def ensure_dirs():
    os.makedirs("public/games/backup", exist_ok=True)
    os.makedirs("scratch", exist_ok=True)

def remove_outer_flood(im_rgba, target_rgb, tolerance=22):
    arr = np.array(im_rgba.convert('RGBA'))
    h, w, _ = arr.shape
    target = np.array(target_rgb)
    
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

def isolate_and_center_transparent(img, target_size=800, padding_pct=0.10, is_white=True, tolerance=22):
    target_rgb = [255, 255, 255] if is_white else [0, 0, 0]
    trans = remove_outer_flood(img, target_rgb, tolerance=tolerance)
    
    # Find bounding box of non-transparent pixels
    arr = np.array(trans)
    mask = (arr[:, :, 3] > 10)
    coords = np.argwhere(mask)
    if len(coords) == 0:
        return img.resize((target_size, target_size), Image.Resampling.LANCZOS)
        
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    
    # Crop tightly to product
    cropped = trans.crop((x0, y0, x1 + 1, y1 + 1))
    cw, ch = cropped.size
    
    # Usable area
    usable_w = int(target_size * (1.0 - 2 * padding_pct))
    usable_h = int(target_size * (1.0 - 2 * padding_pct))
    
    scale = min(usable_w / cw, usable_h / ch)
    nw = max(1, int(cw * scale))
    nh = max(1, int(ch * scale))
    
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    canvas.paste(resized, ((target_size - nw) // 2, (target_size - nh) // 2), mask=resized)
    return canvas

def make_luxury_product_card(img, target_size=800, padding_pct=0.08, corner_radius=18, add_shadow=True):
    usable_w = int(target_size * (1 - 2 * padding_pct))
    usable_h = int(target_size * (1 - 2 * padding_pct))
    
    w, h = img.size
    scale = min(usable_w / w, usable_h / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS).convert('RGBA')
    
    mask = Image.new('L', (new_w, new_h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, new_w, new_h], radius=corner_radius, fill=255)
    
    box_with_corners = Image.new('RGBA', (new_w, new_h), (0, 0, 0, 0))
    box_with_corners.paste(resized, (0, 0), mask=mask)
    
    canvas = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    offset_x = (target_size - new_w) // 2
    offset_y = (target_size - new_h) // 2
    
    if add_shadow:
        shadow_mask = Image.new('L', (target_size, target_size), 0)
        sdraw = ImageDraw.Draw(shadow_mask)
        shadow_rect = [
            offset_x + int(new_w * 0.05),
            offset_y + new_h - 15,
            offset_x + new_w - int(new_w * 0.05),
            offset_y + new_h + 25
        ]
        sdraw.ellipse(shadow_rect, fill=160)
        shadow_blurred = shadow_mask.filter(ImageFilter.GaussianBlur(15))
        
        shadow_layer = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
        shadow_layer.putalpha(shadow_blurred)
        canvas = Image.alpha_composite(canvas, shadow_layer)
        
    canvas.paste(box_with_corners, (offset_x, offset_y), mask=box_with_corners)
    return canvas

def crop_letterbox_and_square(im, tolerance_white=240, tolerance_black=25, target_size=800):
    arr = np.array(im.convert('RGB'))
    h, w, _ = arr.shape
    
    # Strip white/black side bars
    left = 0
    while left < w and (np.all(arr[:, left, :] >= tolerance_white) or np.all(arr[:, left, :] <= tolerance_black)):
        left += 1
        
    right = w - 1
    while right >= 0 and (np.all(arr[:, right, :] >= tolerance_white) or np.all(arr[:, right, :] <= tolerance_black)):
        right -= 1
        
    top = 0
    while top < h and (np.all(arr[top, :, :] >= tolerance_white) or np.all(arr[top, :, :] <= tolerance_black)):
        top += 1
        
    bottom = h - 1
    while bottom >= 0 and (np.all(arr[bottom, :, :] >= tolerance_white) or np.all(arr[bottom, :, :] <= tolerance_black)):
        bottom -= 1
        
    if right <= left or bottom <= top:
        cropped = im
    else:
        cropped = im.crop((left, top, right + 1, bottom + 1))
        
    cw, ch = cropped.size
    # Center crop to 1:1 square
    side = min(cw, ch)
    x_off = (cw - side) // 2
    y_off = (ch - side) // 2
    square = cropped.crop((x_off, y_off, x_off + side, y_off + side))
    return square.resize((target_size, target_size), Image.Resampling.LANCZOS)

def main():
    ensure_dirs()
    with open('data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)['games']
        
    print(f"Starting master unification for {len(games)} games...")
    
    for i, g in enumerate(games, 1):
        gid = g['id']
        rel_p = g['image'].lstrip('/')
        out_p = os.path.join('public', rel_p)
        backup_p = os.path.join('public/games/backup', os.path.basename(out_p))
        
        # Backup if exists and not already backed up
        if os.path.exists(out_p) and not os.path.exists(backup_p):
            shutil.copy2(out_p, backup_p)
            
        print(f"[{i:02d}/44] Processing {gid} -> {out_p}")
        
        # 1. El Joker
        if gid == 'el-joker':
            joker_raw = Image.open('scratch/El-Joker01.jpg')
            card = make_luxury_product_card(joker_raw, target_size=800, padding_pct=0.08, corner_radius=16, add_shadow=True)
            card.save(out_p, 'WEBP', quality=92)
            
        # 2. Waraa El Gareema
        elif gid == 'waraa-el-gareema':
            # Unwarp fine
            warped = cv2.imread("scratch/waraa_unwarped_fine.jpg")
            cropped = warped[8:635, 8:448]
            cv2.imwrite("scratch/waraa_clean_crop.jpg", cropped)
            pil_crop = Image.open("scratch/waraa_clean_crop.jpg")
            card = make_luxury_product_card(pil_crop, target_size=800, padding_pct=0.08, corner_radius=16, add_shadow=True)
            card.save(out_p, 'WEBP', quality=92)
            
        # 3. Raz3 El Gomhoor
        elif gid == 'raz3-el-gomhoor':
            rz3_im = cv2.imread("scratch/rz3_clean.jpg")
            pts1_rz3 = np.float32([[24, 6], [130, 24], [36, 178], [136, 170]])
            out_w, out_h = 420, 600
            pts2 = np.float32([[0, 0], [out_w, 0], [0, out_h], [out_w, out_h]])
            mat_rz3 = cv2.getPerspectiveTransform(pts1_rz3, pts2)
            warped_rz3 = cv2.warpPerspective(rz3_im, mat_rz3, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
            gauss = cv2.GaussianBlur(warped_rz3, (0, 0), 1.5)
            sharp_rz3 = cv2.addWeighted(warped_rz3, 1.3, gauss, -0.3, 0)
            cv2.imwrite("scratch/rz3_unwarped.jpg", sharp_rz3)
            pil_rz3 = Image.open("scratch/rz3_unwarped.jpg")
            card = make_luxury_product_card(pil_rz3, target_size=800, padding_pct=0.08, corner_radius=18, add_shadow=True)
            card.save(out_p, 'WEBP', quality=92)
            
        # 4. 3arosty
        elif gid == '3arosty':
            arosty_im = cv2.imread("scratch/3arosty_clean.jpg")
            pts1_a = np.float32([[14, 10], [125, 12], [24, 160], [135, 158]])
            out_w, out_h = 420, 600
            pts2 = np.float32([[0, 0], [out_w, 0], [0, out_h], [out_w, out_h]])
            mat_a = cv2.getPerspectiveTransform(pts1_a, pts2)
            warped_a = cv2.warpPerspective(arosty_im, mat_a, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
            gauss_a = cv2.GaussianBlur(warped_a, (0, 0), 1.5)
            sharp_a = cv2.addWeighted(warped_a, 1.3, gauss_a, -0.3, 0)
            cv2.imwrite("scratch/3arosty_unwarped.jpg", sharp_a)
            pil_a = Image.open("scratch/3arosty_unwarped.jpg")
            card = make_luxury_product_card(pil_a, target_size=800, padding_pct=0.08, corner_radius=18, add_shadow=True)
            card.save(out_p, 'WEBP', quality=92)
            
        # 5. Mawsoo3at Al Ma3refa
        elif gid == 'mawsoo3at-al-ma3refa':
            im_m = cv2.imread("scratch/mawsoo3at_face.jpg")
            pts1 = np.float32([[45, 62], [142, 62], [12, 245], [122, 245]])
            out_w, out_h = 420, 600
            pts2 = np.float32([[0, 0], [out_w, 0], [0, out_h], [out_w, out_h]])
            mat = cv2.getPerspectiveTransform(pts1, pts2)
            warped = cv2.warpPerspective(im_m, mat, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
            gauss = cv2.GaussianBlur(warped, (0, 0), 1.5)
            sharp = cv2.addWeighted(warped, 1.3, gauss, -0.3, 0)
            cv2.imwrite("scratch/mawsoo3at_unwarped.jpg", sharp)
            pil_im = Image.open("scratch/mawsoo3at_unwarped.jpg")
            card = make_luxury_product_card(pil_im, target_size=800, padding_pct=0.08, corner_radius=18, add_shadow=True)
            card.save(out_p, 'WEBP', quality=92)
            
        # 6. Casino Al3ab Marwan Serry
        elif gid == 'casino-al3ab-marwan-serry':
            im_cas = Image.open(backup_p)
            W, H = im_cas.size
            front_box = im_cas.crop((0, 0, int(W * 0.52), H))
            card = isolate_and_center_transparent(front_box, target_size=800, padding_pct=0.10, is_white=True, tolerance=20)
            card.save(out_p, 'WEBP', quality=92)
            
        # 7. Starting Chess
        elif gid == 'starting-chess':
            im_chess = Image.open('downloads_official/chess_official.jpg')
            card = isolate_and_center_transparent(im_chess, target_size=800, padding_pct=0.08, is_white=True, tolerance=25)
            card.save(out_p, 'WEBP', quality=92)
            
        # 8. Original Domino
        elif gid == 'original-domino':
            im_dom = Image.open('scratch/domino_tight_crop.jpg')
            card = isolate_and_center_transparent(im_dom, target_size=800, padding_pct=0.10, is_white=True, tolerance=20)
            card.save(out_p, 'WEBP', quality=92)
            
        # 9. Black background 3D renders
        elif gid in ['tasali-aflam', 'tasali-kelma-fe-serrak', 'tasali-3andalib', 
                     'tasali-haqeeqa-khayal', 'tasali-system', 'tasali-kalam-fady', 'khufu']:
            im_item = Image.open(backup_p)
            card = isolate_and_center_transparent(im_item, target_size=800, padding_pct=0.10, is_white=False, tolerance=15)
            card.save(out_p, 'WEBP', quality=92)
            
        # 10. White background 3D renders
        elif gid in ['kadab', 'msh-hanbatel-nel3ab', 'est7ala', 'ew3a-weshak', 
                     'el-3awz', '2oolameme-2', 'sahseh', 'tomouhy', 'tasali-madfa3-ramadan']:
            im_item = Image.open(backup_p)
            card = isolate_and_center_transparent(im_item, target_size=800, padding_pct=0.09, is_white=True, tolerance=22)
            card.save(out_p, 'WEBP', quality=92)
            
        # 11. Met7awech (yellow solid bg)
        elif gid == 'met7awech':
            im_m = Image.open(backup_p)
            corner_m = im_m.getpixel((0, 0))[:3]
            trans_m = remove_outer_flood(im_m, corner_m, tolerance=25)
            # Find bbox
            arr = np.array(trans_m)
            coords = np.argwhere(arr[:, :, 3] > 10)
            y0, x0 = coords.min(axis=0)
            y1, x1 = coords.max(axis=0)
            cropped = trans_m.crop((x0, y0, x1 + 1, y1 + 1))
            # Scale to 800
            card = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
            usable = int(800 * 0.82)
            scale = min(usable / cropped.size[0], usable / cropped.size[1])
            nw = int(cropped.size[0] * scale)
            nh = int(cropped.size[1] * scale)
            resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
            card.paste(resized, ((800 - nw) // 2, (800 - nh) // 2), mask=resized)
            card.save(out_p, 'WEBP', quality=92)
            
        # 12. Full-bleed photos and cover art
        else:
            im_item = Image.open(backup_p)
            card = crop_letterbox_and_square(im_item, target_size=800)
            card.save(out_p, 'WEBP', quality=92)
            
        print(f"  -> Generated {out_p}: {os.path.getsize(out_p)//1024} KB")

    print("\nAll 44 images processed successfully!")

if __name__ == "__main__":
    main()
