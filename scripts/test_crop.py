from PIL import Image
import os
from process_ecommerce_image import process_to_ecommerce_square

img_path = r"Image\WhatsApp Image 2026-11-17 at 12.53.11 AM.jpeg"
im = Image.open(img_path)
W, H = im.size

# Box: [517, 34, 762, 269] -> ymin, xmin, ymax, xmax (normalized 0-1000)
ymin, xmin, ymax, xmax = 517, 34, 762, 269
left = int(xmin * W / 1000)
top = int(ymin * H / 1000)
right = int(xmax * W / 1000)
bottom = int(ymax * H / 1000)

# Add small margin
margin_x = int((right - left) * 0.05)
margin_y = int((bottom - top) * 0.05)
crop_box = (
    max(0, left - margin_x),
    max(0, top - margin_y),
    min(W, right + margin_x),
    min(H, bottom + margin_y)
)

cropped = im.crop(crop_box)
os.makedirs("scratch", exist_ok=True)
cropped.save("scratch/crop_waraa_gareema.jpg")
print(f"Cropped waraa_gareema: size={cropped.size}")

# Process to e-commerce square
out_path = "public/games/waraa-el-gareema.webp"
process_to_ecommerce_square("scratch/crop_waraa_gareema.jpg", out_path, target_size=800, bg_color=(255, 255, 255))
print(f"Generated {out_path}: {os.path.getsize(out_path)} bytes")
