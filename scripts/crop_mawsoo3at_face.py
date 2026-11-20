from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg")
W, H = im.size

# Crop lower down: y from 0.55 to 0.85, x from 0.0 to 0.18
crop = im.crop((0, int(0.55 * H), int(0.18 * W), int(0.85 * H)))
crop.save("scratch/mawsoo3at_face.jpg")
print("Saved mawsoo3at_face.jpg:", crop.size)
