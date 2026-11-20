import os
from PIL import Image

im = Image.open('scratch/El-Joker01.jpg')
print("El-Joker01 size:", im.size)

# Let's inspect what El-Joker01 is
# Let's save a resized version to scratch for analysis
small = im.resize((400, int(400 * im.size[1] / im.size[0])))
small.save('scratch/el_joker_preview.jpg')
print("Saved el_joker_preview.jpg:", small.size)

# Also check El-Joker02
im2 = Image.open('scratch/El-Joker02.jpg')
small2 = im2.resize((400, int(400 * im2.size[1] / im2.size[0])))
small2.save('scratch/el_joker_02_preview.jpg')
print("Saved el_joker_02_preview.jpg:", small2.size)
