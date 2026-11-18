import os
from process_ecommerce_image import process_to_ecommerce_square

mapping = {
    "downloads_official/kadab_official.jpg": "public/games/kadab.webp",
    "downloads_official/el_3awz_official.png": "public/games/el-3awz.webp",
    "downloads_official/chess_official.jpg": "public/games/starting-chess.webp",
    "downloads_official/sahseh_official.jpg": "public/games/sahseh.webp",
    "downloads_official/ew3a_weshak_official.jpg": "public/games/ew3a-weshak.webp",
    "downloads_official/2oolameme_official.webp": "public/games/2oolameme-2.webp",
}

for inp, out in mapping.items():
    if os.path.exists(inp):
        process_to_ecommerce_square(inp, out, target_size=800, bg_color=(255, 255, 255))
        print(f"Updated {out} from {inp}")
    else:
        print(f"Missing {inp}")
