import cv2
import random
import time
import numpy as np

img1=cv2.imread("leiyi.jpg")
img=np.zeros((300,300,3),np.uint8)


cv2.namedWindow('image')
imgold1=img1.copy()
imgold=img.copy()
n=4
point=0
t=0


def getpoints(event,x,y,flags,param):
    global point,a,b,sign1,sign2
    
    if event==cv2.EVENT_LBUTTONDOWN:
        
        if sign1==1 and 70*b <= y <= 70*(1+b) and 70*a <= x <= 70*(1+a):
            point = point +1
            sign1=sign1+1
            print("get a point!")
        elif   sign2==1 and 70*d <= y <= 70*(1+d) and 70*c <= x <= 70*(1+c):
            point = point +1
            sign2=sign2+1
            print("get a point!")

while True:
    
    img=imgold.copy()
    head=img1[170:240,170:240].copy()
    a=random.randint(0,n-1)
    b=random.randint(0,n-1)
    c=random.randint(0,n-1)
    d=random.randint(0,n-1)    
    img[70*b:70*(b+1),70*a:70*(a+1)]=head
    img[70*d:70*(d+1),70*c:70*(c+1)]=head
    for i in range(0,n):
      for j in range(0,n):
          cv2.rectangle(img,(70*j,70*i),(70*(j+1),70*(i+1)),(0,255,0),5)
    
    sign1=1
    sign2=1
    cv2.setMouseCallback('image',getpoints)
    t=t+1
    cv2.imshow("image",img)
    if t<=10:
        cv2.waitKey(1000)
    elif t>10 and t<=15:
        cv2.waitKey(700)
    elif  t>15 and t<=20:
        cv2.waitKey(500)
    else:    
        break

print("You have got "+str(point)+" points.")
