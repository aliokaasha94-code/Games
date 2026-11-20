from PIL import Image

im = Image.open(r"Image\WhatsApp Image 2026-11-17 at 12.53.11 AM.jpeg")
W, H = im.size
print("Shelf photo size:", W, H)

# The earlier box in test_crop.py was:
# ymin, xmin, ymax, xmax = 517, 34, 762, 269
# Let's crop a slightly tighter box around the actual front of the box, avoiding the table and adjacent box
# In test_crop.py, left was 34 * W / 1000 = 54, right was 269 * W / 1000 = 430
# top was 517 * H / 1000 = 620, bottom was 762 * H / 1000 = 915
# Notice on the right there was another box ("RAW") overlapping at x > ~220!
# And at the left x < 45 was black shadow/table!

# Let's inspect the coordinates in detail
crop1 = im.crop((int(0.04 * W), int(0.50 * H), int(0.25 * W), int(0.77 * H)))
crop1.save("scratch/waraa_tight_1.jpg")

crop2 = im.crop((int(0.05 * W), int(0.51 * H), int(0.23 * W), int(0.76 * H)))
crop2.save("scratch/waraa_tight_2.jpg")

print("Saved scratch/waraa_tight_1.jpg:", crop1.size)
print("Saved scratch/waraa_tight_2.jpg:", crop2.size)
