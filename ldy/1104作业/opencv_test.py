import cv2 as cv
import numpy as np
import random


num=0
def click_add(event,x,y,flags,param):
    global num
    if event==cv.EVENT_LBUTTONDOWN:
        on = False
        for i in range(len(on_mat)):
            if(on_mat[i][0]<x<on_mat[i][1])and(on_mat[i][2]<y<on_mat[i][3]):
                on = True
        if on:
            num+=1
            print(num)


        





size = 400
time=2000


bgimg = cv.imread("./img/0.jpg")
bgcol = [ bgimg for i in range(3)]
bgs = [np.vstack(bgcol) for i in range(3)]
bg = np.hstack(bgs)
imgs= []
for i in range(9):
    imgname = "./img/"+str(i+1)+".jpg"
    imgs.append(cv.imread(imgname))
screen=[]
for i in range(3):
    screen.append(np.vstack(imgs[3*i:3*i+3]))
out = np.hstack(screen)
# cv.imshow("win",out)

# def slide(previous_img,now_img):
origin=bg.copy()


cv.imshow("win",bg)
cv.setMouseCallback("win",click_add)
cv.waitKey(time)
while(True):
    bg = origin.copy()
    t = random.randint(1,9)
    on_mat=[]
    for k in range(t):
        x,y = random.randint(0,2),random.randint(0,2)
        i,j = x,y
        bg[i*size:i*size+size,j*size:j*size+size]=out[i*size:i*size+size,j*size:j*size+size]
        on_mat.append([i*size,i*size+size,j*size,j*size+size])
        cv.rectangle(bg,(j*size,i*size),(j*size+size,i*size+size),(255,255,0),3)
    cv.imshow("win",bg)
    cv.waitKey(time)
cv.waitKey(0)

