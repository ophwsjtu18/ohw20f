import cv2
import random
import numpy as np

print("hello")
img=cv2.imread("cat.png")
imgold = img.copy()

def mouse(event,x,y,flags,param):
    global i,j,point
    if event == cv2.EVENT_LBUTTONDOWN and i*100<=x<=(i+1)*100 and j*100<=y<=(j+1)*100:
        point = point+100
        print(point)

while True:
    img = imgold.copy()
    head= img[400:450,500:550]
    cv2.namedWindow('qxh')
    for a in range(0,3):
        for b in range(0,3):
            if random.randint(0,8)>4:
                img[50*a:50+50*a,50*b:50+50*b]=img[400:450,500:550]
    for i in range(0,3):
        for j in range(0,3):
            cv2.rectangle(img,(50*i,50*j),(50+50*i,50+50*j),(0,255,0),3)
    cv2.imshow("cathead",img)
    for n in range(10):
        cv2.setMouseCallback('qxh',mouse)
        cv2.waitKey(100)
