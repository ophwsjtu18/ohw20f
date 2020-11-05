import cv2
import random
import numpy as np
#img = cv2.imread(r"C:\Users\OUT XB\Desktop\H.M\大二上\开源硬件\Mouse.jpg")
img_mouse = cv2.imread("Mouse.jpg")
img_mouse=cv2.resize(img_mouse, (int(150), int(150)), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('img_mouse',img_mouse)
#events=[i for i in dir(cv2) if 'EVENT'in i]
#print events
# mouse callback function
global count,moreCount
global param_x,param_y
param_x=[]
param_y=[]
count=0
moreCount=0
def ifPunchMouse(event,x,y,flags,param):
    global count,moreCount,param_x,param_y
    if event==cv2.EVENT_LBUTTONDOWN and param_x[0]<=x \
       and param_x[1]>=x and param_y[0]<=y and param_y[1]>=y \
       and moreCount==0:
        count+=1
        moreCount+=1

# 创建图像与窗口并将窗口与回调函数绑定
img_old=np.zeros((550,450,3),np.uint8)
img_empty=np.zeros((150,150,3),np.uint8)
cv2.namedWindow('MouseShow')
cv2.setMouseCallback('MouseShow',ifPunchMouse)

font=cv2.FONT_HERSHEY_PLAIN
while True:
    img=img_old.copy()
    cv2.putText(img,'score:%d'%count,(10,520), font, 4,(255,255,255),2)
    i = int(random.random()*3)
    j = int(random.random()*3)
    img[150*i:150*(i+1),150*j:150*(j+1)]=img_mouse
    param_x=[150*j,150*(j+1)]
    param_y=[150*i,150*(i+1)]
    cv2.imshow('MouseShow',img)
    cv2.waitKey(1000)
    img[150*i:150*(i+1),150*j:150*(j+1)]=img_empty
    moreCount=0
