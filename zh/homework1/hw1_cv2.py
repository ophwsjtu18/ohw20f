import cv2

img = cv2.imread("Targaryen.jpg")
cv2.imshow('image', img)
img_cvtGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("cvtGRAY2",img_cvtGRAY)

cv2.waitKet(0)
cv2.destroyAllWindows()
