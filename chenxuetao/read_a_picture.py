# -*- coding: utf-8 -*-

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('./test_good.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
