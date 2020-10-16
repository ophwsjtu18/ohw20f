import numpy as np
import cv2

pikachu = cv2.imread('pikachu.jpg', 0)

cv2.imshow('pikachu', pikachu)
cv2.waitKey(0)
cv2.destroyAllWindows()
