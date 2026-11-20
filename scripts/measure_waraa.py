import cv2
import numpy as np
from PIL import Image

im = cv2.imread(r"Image\WhatsApp Image 2026-11-17 at 12.53.11 AM.jpeg")
H, W, _ = im.shape

# Let's crop a region with high margin:
# y: 500 to 920, x: 30 to 450
ymin, ymax = int(0.50 * H), int(0.78 * H)
xmin, xmax = int(0.02 * W), int(0.26 * W)
roi = im[ymin:ymax, xmin:xmax]
cv2.imwrite("scratch/waraa_roi.jpg", roi)
print(f"ROI shape: {roi.shape}")
