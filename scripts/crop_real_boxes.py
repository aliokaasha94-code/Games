import cv2
from PIL import Image

im = cv2.imread("scratch/shelf_rz3_actual.jpg")
H, W, _ = im.shape
print("Actual size:", W, H)

# 1. Raz3 El Gomhoor
# x from 60 to 200, y from 30 to 215
rz3 = im[30:215, 60:200]
cv2.imwrite("scratch/rz3_clean.jpg", rz3)

# 2. 3arosty
# x from 115 to 255, y from 220 to 380
arosty = im[220:380, 115:255]
cv2.imwrite("scratch/3arosty_clean.jpg", arosty)

print("Saved rz3_clean.jpg and 3arosty_clean.jpg")
