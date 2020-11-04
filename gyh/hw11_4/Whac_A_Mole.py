import cv2
import random

class Whac_A_Mole:
    def __init__(self, bkg, obj):
        self.bkg = bkg.copy()
        self.obj = obj.copy()
        self.img = bkg.copy()
        self.x = 0
        self.y = 0
        self.point = 0
        self.state = 0
        cv2.namedWindow('Whac-A-Mole')
        cv2.setMouseCallback('Whac-A-Mole',self.__mouse_check)
    def __img_show(self):
        cv2.imshow("Whac-A-Mole",self.img)
        cv2.waitKey(500)
    def __clean(self):
        self.img[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)] = bkg[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)]
        self.state = 0
        self.__img_show()
    def __set_obj(self):
        self.x = random.randint(0, 2)
        self.y = random.randint(0, 2)
        self.img[200*self.x:200*(self.x+1), 200*self.y:200*(self.y+1)] = self.obj
        self.state = 1
        self.__img_show()
    def __mouse_check(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN and self.state == 1:
            if 200*self.x <= x <= 200*(self.x+1) and 200*self.y <= y <= 200*(self.y+1):
                self.point += 1
    def run(self):
        self.__clean()
        self.__set_obj()
        print("Point:", self.point)


bkg = cv2.imread("./background.jpg")
hj = cv2.imread("./huaji.jpg")
game = Whac_A_Mole(bkg, hj)

while True:
    game.run()
