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
    
    margin_x = int((right - left) * 0.04)
    margin_y = int((bottom - top) * 0.04)
    
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
    (r"Image\WhatsApp Image 2026-11-17 at 12.35.02 AM.jpeg", [243, 127, 418, 706], "public/games/el-joker.webp"),
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.11 AM.jpeg", [492, 265, 762, 427], "public/games/msh-hanbatel.webp"),
    (r"Image\WhatsApp Image 2026-11-17 at 12.53.11 AM.jpeg", [390, 613, 560, 796], "public/games/est7ala.webp"),
]

for img_p, b, out_p in crops:
    crop_and_process(img_p, b, out_p)
