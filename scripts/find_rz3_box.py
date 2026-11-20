from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg")
W, H = im.size

# Let's crop lower down on the shelf where the boxes sit:
# y from 0.40 to 0.75, x from 0.68 to 0.85
crop = im.crop((int(0.68 * W), int(0.38 * H), int(0.85 * W), int(0.70 * H)))
crop.save("scratch/shelf_rz3_actual.jpg")
print("Saved shelf_rz3_actual.jpg:", crop.size)
