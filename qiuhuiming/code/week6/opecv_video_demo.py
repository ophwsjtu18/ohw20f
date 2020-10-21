"""
@author: Huiming Qiu
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# 5.1 从摄像头中捕获视频
# ********************************************
cap = cv2.VideoCapture(0)

while True:
    # ret: 帧是否读取正确
    # frame: 帧
    ret, frame = cap.read()

    # 把frame调成灰色
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
        break

cap.release()
cv2.destroyAllWindows()
# ********************************************

# 5.2 从文件中播放视频
