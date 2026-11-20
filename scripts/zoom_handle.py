import cv2
import numpy as np

roi = cv2.imread("scratch/waraa_roi.jpg")
# zoom into the instagram handle at bottom center: y=270..315, x=150..300
handle = roi[265:315, 160:290]
cv2.imwrite("scratch/waraa_handle.jpg", handle)

# enhance contrast
gray = cv2.cvtColor(handle, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
enhanced = clahe.apply(gray)
cv2.imwrite("scratch/waraa_handle_enhanced.jpg", enhanced)
print("Saved waraa handle")
