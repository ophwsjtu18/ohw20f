'''20201104assignment'''


import cv2
import random

bkg = cv2.imread("./cd.jpg")
lyy = cv2.imread("./LYY.jpg")
print("抓住懒羊羊，游戏开始!按空格退出")

class click_Testing:
    def __init__(self, bkg, obj):
        self.x = 0
        self.y = 0
        self.point = 0
        self.state = 0
        self.bkg = bkg.copy()
        self.obj = obj.copy()
        self.img = bkg.copy()
        cv2.namedWindow('CatchLYY,Press Space Button to exit')
        cv2.setMouseCallback('CatchLYY,Press Space Button to exit',self.judge)
    def img_out(self):
        cv2.imshow('CatchLYY,Press Space Button to exit',self.img)
        cv2.waitKey(400)
    def reset(self):
        self.img[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)] = bkg[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)]
        self.img_out()
        self.state = 0
    def set_obj(self):
        self.x = random.randint(0, 3)
        self.y = random.randint(0, 3)
        self.img[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)] = self.obj
        self.state = 1
        self.img_out()
    def judge(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN and self.state == 1:
            if 200*self.x <= y <= 200*(self.x+1) and 200*self.y <= x <= 200*(self.y+1):
                self.point += 1
    def run(self):
        self.reset()
        self.set_obj()
        print("分数:", self.point)


game = click_Testing(bkg, lyy)


while True :
    game.run()
    if cv2.waitKey(1) ==ord(' '):
        break

cv2.destroyAllWindows()        
print("游戏结束，您的分数为:"+str(game.point))

