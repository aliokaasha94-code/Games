import json
from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg")
W, H = im.size
print("Shelf photo 12.53.12 AM size:", W, H)

# Let's see what detections are in boxes_WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg.json
# or cafe_boxes_detected.json
try:
    with open(r"scripts\boxes_WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg.json", "r", encoding="utf-8") as f:
        boxes = json.load(f)
    print(f"Found {len(boxes)} detected boxes in this image:")
    for b in boxes:
        print(f"  {b.get('name_ar')} / {b.get('name_en')}: {b.get('box_2d')}")
except Exception as e:
    print("Error reading json:", e)
