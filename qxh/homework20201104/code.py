import cv2
import random
import numpy as np

print("hello")
img=cv2.imread("cat.png")
imgold = img.copy()
point = 0



def mouse(event,x,y,flags,param):
    global point,curr
    if event == cv2.EVENT_LBUTTONDOWN:
        if i*50<=x<=(i+1)*50 and j*50<=y<=(j+1)*50:
            point = point+1
            print(point)

cv2.namedWindow('qxh')
cv2.setMouseCallback('qxh',mouse)
while True:
    img = imgold.copy()
    head= img[400:450,500:550].copy()
    i = random.randint(0,2)
    j = random.randint(0,2)
    img[i*50:(i+1)*50,j*50:(j+1)*50]=head
    
    for a in range(0,3):
        for b in range(0,3):
            cv2.rectangle(img,(50*a,50*b),(50+50*a,50+50*b),(0,255,0),3)
    cv2.imshow('qxh',img)
    cv2.waitKey(500)
