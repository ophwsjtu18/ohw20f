import cv2
import random

global numx
numx=-1
global numy
numy=-1

def judge(event,x,y,flags,param):
     global numx
     global numy
     if event==cv2.EVENT_LBUTTONDOWN:
          numx=x
          numy=y
     else:
          numx=-1
          numy=-1
        
print("hello world")
img=cv2.imread("pikaqiu.png")
imgold=img.copy()

array= [[0,0,0],[0,0,0],[0,0,0]]
num=[0]

while True:
     
     #随机产生图片
     for i in range(3):
          head=imgold[400:450,300:350].copy()
          for j in range(3):
               x0=50*i
               y0=50*j
               if random.randint(0,8)>4:
                    img[y0:y0+50,x0:x0+50]=head
                    array[i][j]=1
               else:
                    img[y0:y0+50,x0:x0+50]=imgold[y0:y0+50,x0:x0+50]
                    array[i][j]=0
     #绿框           
     for i in range(3):
          for j in range(3):
               x0=50*i
               y0=50*j
               cv2.rectangle(img,(x0,y0),(x0+50,y0+50),(0,255,0),3)

     cv2.setMouseCallback("test",judge)

     #计数
     if numx>=0:
          if array[numx//50][numy//50]==1:
               num[0]=num[0]+1
               print(num[0])
          
    
     cv2.imshow("test",img)
     cv2.waitKey(1000)
