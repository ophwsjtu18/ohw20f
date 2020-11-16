import cv2
import random
import numpy as np

score=0
tmp=random.randint(0,3)
def dazhong(event,x,y,flags,param):
    global score,tmp
    if tmp==0:
        if event==cv2.EVENT_LBUTTONDOWN:
            if(0<=x<=200) and (0<=y<=200):
                score+=1
    elif tmp==1:
        if event==cv2.EVENT_LBUTTONDOWN:
            if(0<=x<=200) and (200<=y<=400):
                score+=1
    elif tmp==2:
        if event==cv2.EVENT_LBUTTONDOWN:
            if(200<=x<=400) and (0<=y<=200):
                score+=1
    elif tmp==3:
        if event==cv2.EVENT_LBUTTONDOWN:
            if(200<=x<=400) and (200<=y<=400):
                score+=1

img=cv2.imread("dishu.jpg")
dishu=img[125:325,125:325].copy()
img=cv2.imread("field.jpg")
cv2.imshow("p1",img)
cv2.setMouseCallback('p1', dazhong)
while True:
    tmp=random.randint(0,3)
    img=cv2.imread("field.jpg")
    if tmp==0:
        img[0:200,0:200]=dishu
    elif tmp==1:
        img[200:400,0:200]=dishu
    elif tmp==2:
        img[0:200,200:400]=dishu
    elif tmp==3:
        img[200:400,200:400]=dishu
    cv2.imshow("p1",img)
    if cv2.waitKey(100)&0xFF==27:
        break
    print (score)
cv2.destroyAllWindows()
