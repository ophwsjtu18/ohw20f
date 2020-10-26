import os
print(os.path.abspath('.'))
import cv2
import numpy
img = cv2.imread("imagel.jpg",1)
img
cv2.imshow("image",img)
