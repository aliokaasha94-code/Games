import cv2
import numpy as np
from PIL import Image
from test_luxury_joker import make_luxury_product_card

im = cv2.imread("scratch/mawsoo3at_face.jpg")
pts1 = np.float32([
    [45, 62],
    [142, 62],
    [12, 245],
    [122, 245]
])
out_w, out_h = 420, 600
pts2 = np.float32([[0, 0], [out_w, 0], [0, out_h], [out_w, out_h]])
mat = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(im, mat, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
gauss = cv2.GaussianBlur(warped, (0, 0), 1.5)
sharp = cv2.addWeighted(warped, 1.3, gauss, -0.3, 0)
cv2.imwrite("scratch/mawsoo3at_unwarped.jpg", sharp)

pil_im = Image.open("scratch/mawsoo3at_unwarped.jpg")
card = make_luxury_product_card(pil_im, target_size=800, padding_pct=0.08, corner_radius=18)
card.save("scratch/mawsoo3at_card_test.webp", "WEBP", quality=90)
print("Saved scratch/mawsoo3at_card_test.webp")
