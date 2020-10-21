import cv2 as cv
import sys
img_src = "pic.png"
img = cv.imread(img_src,cv.IMREAD_UNCHANGED)
cv.imshow("Display",img)
k = cv.waitKey(0)
if k==ord("s"):
    cv.destroyAllWindows()
    

