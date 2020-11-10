import cv2
import random
import time

img=cv2.imread("pic.jpg")
cap=cv2.VideoCapture(0)
cv2.namedWindow("windowforPic")
count = 0
i=0
j=0
imgbackGrn=cv2.imread("background.png")
def clickMouse(event,x,y,flags,param):
    global i,j,count,aft,imgbackGrn
    if event==cv2.EVENT_LBUTTONDOWN and 120*i<y<(120+120*i)and 120*j<x<(120+120*j):
        count=count+1
        print("你的得分：")
        print(count)
        imgbackGrn[120*i:120+120*i,120*j:120+120*j]=aft
        cv2.imshow("windowforPic",imgbackGrn)
        
cv2.setMouseCallback("windowforPic",clickMouse)
imgOrign=img.copy()
img=cv2.imread("lovelyCat.jpg")
aft=cv2.imread("afterHit.jpg")
while True:
    stanCat = cv2.resize(img,(0, 0), fx=120/222, fy=120/226, interpolation=cv2.INTER_NEAREST)
    imgbackGrn=cv2.imread("background.png")
    head=stanCat.copy()
    for a in range(3):
        for b in range(3):
            cv2.rectangle(imgbackGrn,(120*a,120*b),(120+120*a,120+120*b),(0,255,0),3)
    i=random.randint(0,2)
    j=random.randint(0,2)
    imgbackGrn[120*i:120+120*i,120*j:120+120*j]=head            
    k=cv2.waitKey(1)&0xFF
    if k==ord('c'):
        print(count)
    if k==27:
        break
    cv2.imshow("windowforPic",imgbackGrn)
    cv2.waitKey(random.randint(600,2000))
cv2.destroyAllWindows()
