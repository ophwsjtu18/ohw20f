import cv2
import random
import time

#变量初始化
score = 0
x1 = -1
y1 = -1
x2 = -1
y2 = -1

#导入背景图片
img = cv2.imread('BG.jpg')
#备份背景图片
imgcp = img.copy()

#获取图片尺寸
shape = img.shape
w = shape[1]
h = w

shape = [w,h]

#定义计分函数
def addScore(event,x,y,flags,param):
    global score,x1,x2,y1,y2
    #生成矩形坐标
    i = random.randint(0,2)
    j = random.randint(0,2)
    x1 = int(w/3*i)
    y1 = int(h/3*j)
    x2 = int(x1 + w/3)
    y2 = int(y1 + h/3)

    #绘制矩形和坐标
    cv2.rectangle(img, (x1,y1), (x2, y2),(0, 255, 0), 3)
    cv2.imshow('Game',img)

    #计分判断
    if event == cv2.EVENT_LBUTTONDOWN and x1<x<x2 and y1<y<y2:
        score = score + 1
    
    time.sleep(0.5)

#创建窗口
cv2.namedWindow('Game')
cv2.setMouseCallback('Game',addScore,shape)

#主函数
while True:
    cv2.imshow('Game',img)
    if cv2.waitKey(500)&0xff == 27:
        break
    print(x1,y1,score)
cv2.destroyAllWindows()
