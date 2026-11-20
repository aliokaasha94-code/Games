import cv2
import numpy as np
from PIL import Image

roi = cv2.imread("scratch/waraa_roi.jpg")

# Source quad corners:
# Top-Left: around (165, 20)
# Top-Right: around (340, 20) - just before the adjacent box
# Bottom-Left: around (68, 308)
# Bottom-Right: around (330, 308)

pts1 = np.float32([
    [165, 20],
    [340, 20],
    [68, 308],
    [330, 308]
])

# Destination: upright box art (aspect ratio ~1.3: height 600, width 460)
out_w, out_h = 460, 600
pts2 = np.float32([
    [0, 0],
    [out_w, 0],
    [0, out_h],
    [out_w, out_h]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(roi, matrix, (out_w, out_h), flags=cv2.INTER_LANCZOS4)
cv2.imwrite("scratch/waraa_unwarped.jpg", warped)
print("Saved scratch/waraa_unwarped.jpg")
