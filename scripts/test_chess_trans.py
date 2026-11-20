from PIL import Image
import sys
sys.path.append('scripts')
from test_flood_fill import remove_outer_bg

im = Image.open('downloads_official/chess_official.jpg')
trans = remove_outer_bg(im, bg_is_white=True, tolerance=25)
trans.save('scratch/chess_trans.png')
print("Saved scratch/chess_trans.png")
