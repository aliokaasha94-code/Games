from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg")
W, H = im.size

# Context around rz3 el gomhoor:
# box: [338, 627, 494, 678] -> y is 338..494, x is 627..678
# Let's crop wider: y from 0.30 to 0.52, x from 0.58 to 0.75
crop_rz3 = im.crop((int(0.58 * W), int(0.30 * H), int(0.75 * W), int(0.52 * H)))
crop_rz3.save("scratch/shelf_rz3_wide.jpg")

# Context around 3arosty:
# box: [511, 722, 677, 781]
# Let's crop wider: y from 0.48 to 0.70, x from 0.68 to 0.82
crop_3arosty = im.crop((int(0.68 * W), int(0.48 * H), int(0.82 * W), int(0.70 * H)))
crop_3arosty.save("scratch/shelf_3arosty_wide.jpg")

print("Saved shelf_rz3_wide.jpg:", crop_rz3.size)
print("Saved shelf_3arosty_wide.jpg:", crop_3arosty.size)
