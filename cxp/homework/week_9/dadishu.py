import numpy as np
import cv2
import random

# 列表中的列表的元素表示每只地鼠的坐标，是否被打中，出现时间
di_shu_s = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score = 0


def da(event, x, y, flags, param):
    global di_shu_s, score
    if event == cv2.EVENT_LBUTTONDOWN:
        for dishu in di_shu_s:
            if (dishu[0] <= x <= dishu[0] + 100) and (dishu[1] <= y <= dishu[1] + 100):
                dishu[2] = 0
                score += 1


cv2.namedWindow('da_di_shu', cv2.WINDOW_NORMAL)

bg = np.zeros((600, 600, 3), np.uint8)
cao_di = cv2.imread('cao_di.png', 1)
di_shu = cv2.imread('di_shu.jpg', 1)

# bg[0:600, 0:600] = cao_di
# bg[200:400, 400:600] = di_shu

cv2.setMouseCallback('da_di_shu', da)

while True:
    for dishu in di_shu_s:
        if dishu[2] == 0:
            dishu[0] = random.randint(0, 5)*100
            dishu[1] = random.randint(0, 5)*100
            dishu[2] = 1
            dishu[3] = 0
        elif dishu[3] == 4:
            dishu[0] = random.randint(0, 5)*100
            dishu[1] = random.randint(0, 5)*100
            dishu[3] = 0
        dishu[3] += 1

    bg[0:600, 0:600] = cao_di
    for dishu in di_shu_s:
        bg[dishu[1]:dishu[1]+100, dishu[0]:dishu[0]+100] = di_shu

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(bg, "score:" + str(score), (10, 30), font, 1, (255, 255, 255), 2)

    cv2.imshow('da_di_shu', bg)
    # 可以设置速度，地鼠出现的时间等于waitkey*4
    if cv2.waitKey(200) & 0xFF == 27:
        break

cv2.destroyAllWindows()
