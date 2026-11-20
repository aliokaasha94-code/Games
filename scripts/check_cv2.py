import cv2
from PIL import Image
import numpy as np

# Let's see if OpenCV or PIL can do perspective transform
# Let's check if cv2 is installed
try:
    import cv2
    has_cv2 = True
except ImportError:
    has_cv2 = False
print("OpenCV installed:", has_cv2)
