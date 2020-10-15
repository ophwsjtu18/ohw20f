```
import numpy as np
import cv2

#读入图像
img = cv2.imread('C:/Users/97413/Desktop/Test.jpg',None)

#显示图像，等待键盘输入后关闭
cv2.namedWindow('Test',cv2.WINDOW_NORMAL)
cv2.imshow('Test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
