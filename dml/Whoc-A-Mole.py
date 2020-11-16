import cv2
import random
import numpy as np

score=0
time=0

def WhacAMole(event,x,y,flags,param):
    global score,x1,x2
    if event==cv2.EVENT_LBUTTONDOWN and 50*x1<=x<=50*(x1+1) and 50*y1<=y<=50*(y1+1):
        score=score+1
        print("your score is :"+str(score))

print("hello")
img=cv2.imread("20.png")

imgold=img.copy()
while True:
    img=imgold.copy()
    head=img[220:270,235:285].copy()
    x1=random.randint(0,2)
    y1=random.randint(0,2)
    img[50*x1:50*(x1+1),50*y1:50*(y1+1)]=img[220:270,235:285]
    
    for x2 in range(3):
        for y2 in range(3):
            cv2.rectangle(img,(0+50*x2,0+50*y2),(50+50*x2,50+50*y2),(0,255,0),3)
            
    cv2.imshow("image",img)
    cv2.setMouseCallback('image',WhacAMole)
    cv2.waitKey(500)
    time=time+1
    if time>30:
        break;
print("Game over. Your final score is "+str(score))
