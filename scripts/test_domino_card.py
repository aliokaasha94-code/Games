from PIL import Image
import sys
sys.path.append('scripts')
from test_flood_fill import remove_outer_bg
from test_luxury_joker import make_luxury_product_card

im = Image.open('scratch/domino_tight_crop.jpg')
trans = remove_outer_bg(im, bg_is_white=True, tolerance=15)
trans.save('scratch/domino_trans.png')

# Create card
card = make_luxury_product_card(trans, target_size=800, padding_pct=0.10, corner_radius=0, add_shadow=True)
card.save('scratch/domino_card_test.webp', 'WEBP', quality=90)
print("Saved scratch/domino_card_test.webp")
