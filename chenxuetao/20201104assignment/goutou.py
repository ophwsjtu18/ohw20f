import numpy as np
import cv2
import random

randx=0
randy=0
point=0
curr=0

def draw_circle(event,x,y,flags,param):
    global point
    global curr
    if event==cv2.EVENT_LBUTTONDOWN:
        if 50*randx<y<50+50*randx and 50*randy<x<50+50*randy and curr==0:
            point=point+1
            print(point)
            curr=1

img=cv2.imread("doge.png")
imgold=img.copy()
cv2.namedWindow('dog_head')
cv2.setMouseCallback('dog_head',draw_circle)

while True:
    curr=0
    img=imgold.copy()
    head=img[230:280,70:120].copy()
    randx=random.randint(0,4)
    randy=random.randint(0,4)
    img[50*randx:50+50*randx,50*randy:50+50*randy]=head
            
    for i in range(0,5):
        for j in range(0,5):
            cv2.rectangle(img,(50*i,50*j),(50*i+50,50*j+50),(55,200,0),3)
    cv2.imshow('dog_head',img)
    
    if cv2.waitKey(700)&0xFF==27:
        break
        
