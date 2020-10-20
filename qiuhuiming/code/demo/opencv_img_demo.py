from cv2 import cv2

imagePath = './zhihu.jpg'
image = cv2.imread(imagePath, 0)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()