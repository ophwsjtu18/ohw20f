# This file is a test program for opencv-python
# Date:2020-10-14
import numpy as np
import cv2

img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
