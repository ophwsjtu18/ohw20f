
import cv2
import random
import time
import numpy as np
img=np.zeros((300,300,3),np.uint8)
mole=cv2.imread("dog.png")
cv2.namedWindow('image')

imgold=img.copy()
point=0
time=0
def whack_a_mole(event,x,y,flags,param):
    global point,i,j
    if event==cv2.EVENT_LBUTTONDOWN:
                if 100*i <= x <= 100*(1+i) and 100*j <= y <= 100*(1+j):
                    point = point +1
                    print("you have hit " + str(point))
while True:
    img=imgold.copy()
    head=mole[0:100,0:100].copy()
    i=random.randint(0,2)
    j=random.randint(0,2)
    img[100*i:100*(1+i),100*j:100*(1+j)]= head
    for l in range(3):
        for m in range(3):
            cv2.rectangle(img,(100*l,100*m),(100*(1+l),100*(1+m)),(0,255,0),3)



    cv2.setMouseCallback('image',whack_a_mole)
    time=time+1
        
    cv2.imshow('image',img)

    cv2.waitKey(500)
    if time>=20:
        break

print("Your score is " + str(point)+". Feel free to try again")
#功能描述：在狗头出现位置单击鼠标即可获得一分，游戏开始十秒后结束，计总分并显示
