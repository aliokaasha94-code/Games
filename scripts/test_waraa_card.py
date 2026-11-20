from PIL import Image
import cv2
from test_luxury_joker import make_luxury_product_card

# Load unwarped
warped = cv2.imread("scratch/waraa_unwarped_fine.jpg")
# Crop out the right edge (adjacent box) and clean borders:
# width: 8 to 448 (width 440)
# height: 8 to 635 (height 627)
cropped = warped[8:635, 8:448]
cv2.imwrite("scratch/waraa_clean_crop.jpg", cropped)

pil_crop = Image.open("scratch/waraa_clean_crop.jpg")
card = make_luxury_product_card(pil_crop, target_size=800, padding_pct=0.08, corner_radius=16)
card.save("scratch/waraa_card_test.webp", "WEBP", quality=90)
print("Saved scratch/waraa_card_test.webp")
