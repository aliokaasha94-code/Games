from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg")
W, H = im.size

# y from 0.48 to 0.75, x from 0.0 to 0.15
crop = im.crop((0, int(0.50 * H), int(0.15 * W), int(0.72 * H)))
crop.save("scratch/mawsoo3at_shelf.jpg")
print("Saved mawsoo3at_shelf.jpg:", crop.size)
