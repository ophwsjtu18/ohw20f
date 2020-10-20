import os
from cv2 import cv2
path=os.path.abspath('.')
color_img=cv2.imread(path+'\\test.png')
print(path)
