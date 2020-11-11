import cv2
import numpy as np
import random
import time

yes = cv2.imread('yes.jpg')
background = cv2.imread('background.jpg')

ix,iy = -1,-1
score = 0

def mole(event,x,y,flags,param):
    global ix,iy,score
    if event==cv2.EVENT_LBUTTONDOWN and 0+ix*100<=y<=100+ix*100 and 0+iy*100<=x<=100+iy*100:
            score = score+1

img=np.zeros((400,300,3),np.uint8)
cv2.namedWindow('whac_a_mole',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('whac_a_mole',mole)

while True:
    ix,iy = -1,-1
    flag=0
    img=background.copy()
    ix=random.randint(0,2)
    iy=random.randint(0,2)
    img[0+ix*100:100+ix*100,0+iy*100:100+iy*100]=yes.copy()
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"your score is : "+str(score),(0,325),font,1,(0,0,0),2)
    cv2.putText(img,"press 'esc' to exit",(0,375),font,1,(0,0,0),2)
    cv2.imshow('whac_a_mole',img)
    t0 = time.time()
    while time.time()-t0<=1.0 :
        if cv2.waitKey(1)&0xFF==27:
            flag=1
            break
    if flag==1:
        break

cv2.destroyAllWindows()

