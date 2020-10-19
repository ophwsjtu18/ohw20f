import cv2 as cv
img = cv.imread("2.jpg", 1)
cv.namedWindow('IMG')
cv.imshow("IMG", img)

cv.waitKey()
cv.destroyAllWindows()
