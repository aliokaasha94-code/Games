import cv2
import numpy as np

roi = cv2.imread("scratch/waraa_roi.jpg")

# Let's adjust quad points:
# Top-Left: (172, 16)
# Top-Right: (360, 16)
# Bottom-Left: (70, 308)
# Bottom-Right: (340, 308)

pts1 = np.float32([
    [174, 16],
    [360, 16],
    [70, 308],
    [342, 308]
])

out_w, out_h = 480, 640
pts2 = np.float32([
    [0, 0],
    [out_w, 0],
    [0, out_h],
    [out_w, out_h]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(roi, matrix, (out_w, out_h), flags=cv2.INTER_LANCZOS4)

# Enhance contrast and sharpness slightly to make the artwork pop
# Unsharp mask
gaussian = cv2.GaussianBlur(warped, (0, 0), 2.0)
sharpened = cv2.addWeighted(warped, 1.4, gaussian, -0.4, 0)

cv2.imwrite("scratch/waraa_unwarped_fine.jpg", sharpened)
print("Saved scratch/waraa_unwarped_fine.jpg")
