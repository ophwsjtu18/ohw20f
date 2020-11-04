import numpy as np
import random
import cv2

img = cv2.imread("cat.jpg")

img_old = img.copy()

img_part = np.zeros((450,510,3), np.uint8)

head = img_old[100:250, 180:350].copy()

res = cv2.resize(img_old,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

res_old = res.copy()

flag = [0, 0, 0, 0, 0, 0, 0, 0, 0]

score = 0

def if_click(event, x, y, flags, param):
    global score, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(9):
            flags = flag[i]
            if flags and (i // 3)*150 <= y <= ((i // 3) + 1)*150 and (i % 3)*170 <= x <= ((i % 3) + 1)*170:
                score += 1
                print("click:" + str(i) + ' x:' + str(x) + ' y:' + str(y) + " score:" + str(score))
                flag[i] = 0 #only click once
                font = cv2.FONT_HERSHEY_SIMPLEX
                res[550:800, 550:800] = res_old[550:800, 550:800]
                cv2.putText(res,'score:' + str(score),(600,600), font, 1,(255,255,255),2)
                cv2.imshow('image_ex',res)

while True:
    flag = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    res = cv2.resize(img_old,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    for i in range(3):
        for j in range(3):
            if random.randint(0, 8) > 4:
                flag[i * 3 + j] = True
                res[i * 150:(i+1) * 150, j * 170: (j+1) * 170] = head
            cv2.rectangle(res,(j * 170,i * 150),((j+1) * 170,(i+1) * 150),(255,255,255),3)


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(res,'score:' + str(score),(600,600), font, 1,(255,255,255),2)

    res_new = res.copy()
    
    cv2.imshow('image_ex',res)

    #print(flag)

    cv2.setMouseCallback("image_ex", if_click)

    cv2.waitKey(2000)


