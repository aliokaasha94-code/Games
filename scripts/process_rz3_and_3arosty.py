import cv2
import numpy as np
from PIL import Image
from test_luxury_joker import make_luxury_product_card

# 1. Process Raz3 El Gomhoor
# Source: scratch/rz3_clean.jpg
# Box quad in rz3_clean.jpg:
# Top-Left: (22, 5)
# Top-Right: (132, 28)
# Bottom-Left: (36, 180)
# Bottom-Right: (138, 175)
rz3_im = cv2.imread("scratch/rz3_clean.jpg")
h, w, _ = rz3_im.shape
pts1_rz3 = np.float32([
    [24, 6],
    [130, 24],
    [36, 178],
    [136, 170]
])
out_w, out_h = 420, 600
pts2 = np.float32([[0, 0], [out_w, 0], [0, out_h], [out_w, out_h]])
mat_rz3 = cv2.getPerspectiveTransform(pts1_rz3, pts2)
warped_rz3 = cv2.warpPerspective(rz3_im, mat_rz3, (out_w, out_h), flags=cv2.INTER_LANCZOS4)

# Enhance sharpness
gauss = cv2.GaussianBlur(warped_rz3, (0, 0), 1.5)
sharp_rz3 = cv2.addWeighted(warped_rz3, 1.3, gauss, -0.3, 0)
cv2.imwrite("scratch/rz3_unwarped.jpg", sharp_rz3)

pil_rz3 = Image.open("scratch/rz3_unwarped.jpg")
card_rz3 = make_luxury_product_card(pil_rz3, target_size=800, padding_pct=0.08, corner_radius=18)
card_rz3.save("scratch/raz3_card_test.webp", "WEBP", quality=90)
print("Saved scratch/raz3_card_test.webp")

# 2. Process 3arosty
# In 3arosty_clean.jpg:
# Top-Left: (12, 10)
# Top-Right: (125, 12)
# Bottom-Left: (24, 162)
# Bottom-Right: (136, 160)
arosty_im = cv2.imread("scratch/3arosty_clean.jpg")
h_a, w_a, _ = arosty_im.shape
pts1_a = np.float32([
    [14, 10],
    [125, 12],
    [24, 160],
    [135, 158]
])
mat_a = cv2.getPerspectiveTransform(pts1_a, pts2)
warped_a = cv2.warpPerspective(arosty_im, mat_a, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
gauss_a = cv2.GaussianBlur(warped_a, (0, 0), 1.5)
sharp_a = cv2.addWeighted(warped_a, 1.3, gauss_a, -0.3, 0)
cv2.imwrite("scratch/3arosty_unwarped.jpg", sharp_a)

pil_a = Image.open("scratch/3arosty_unwarped.jpg")
card_a = make_luxury_product_card(pil_a, target_size=800, padding_pct=0.08, corner_radius=18)
card_a.save("scratch/3arosty_card_test.webp", "WEBP", quality=90)
print("Saved scratch/3arosty_card_test.webp")
