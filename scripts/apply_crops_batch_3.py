import os
from PIL import Image
from process_ecommerce_image import process_to_ecommerce_square

def crop_and_process(img_rel_path, box, out_rel_path):
    im = Image.open(img_rel_path)
    W, H = im.size
    ymin, xmin, ymax, xmax = box
    left = int(xmin * W / 1000)
    top = int(ymin * H / 1000)
    right = int(xmax * W / 1000)
    bottom = int(ymax * H / 1000)
    
    margin_x = int((right - left) * 0.05)
    margin_y = int((bottom - top) * 0.05)
    
    crop_box = (
        max(0, left - margin_x),
        max(0, top - margin_y),
        min(W, right + margin_x),
        min(H, bottom + margin_y)
    )
    cropped = im.crop(crop_box)
    temp_path = f"scratch/temp_{os.path.basename(out_rel_path)}.jpg"
    cropped.save(temp_path)
    process_to_ecommerce_square(temp_path, out_rel_path, target_size=800, bg_color=(255, 255, 255))
    print(f"Generated {out_rel_path} ({os.path.getsize(out_rel_path)} bytes)")

crops = [
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg", [338, 627, 494, 678], "public/games/raz3-el-gomhoor.webp"),
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg", [524, 0, 680, 97], "public/games/mawsoo3at.webp"),
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg", [511, 722, 677, 781], "public/games/3arosty.webp"),
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg", [524, 107, 677, 195], "public/games/tala3-el-mostakhabby.webp"),
]

for img_p, b, out_p in crops:
    crop_and_process(img_p, b, out_p)
