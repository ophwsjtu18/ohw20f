import cv2
import numpy as np
import random


def beatGopher(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse down')
        param.beatGopher(x, y)


class GopherGame:
    width = 800
    height = 600

    backgroundImage = 100 * np.ones((height, width, 3), dtype=np.uint8)
    backgroundImageShown = backgroundImage.copy()
    gopherImage = cv2.imread('./gopher.png')[0:150, 70: 250]

    grid = [[True for i in range(3)] for j in range(3)]

    windowName = 'gophers'

    score = 0

    sleepTime = 1000

    def __init__(self):
        # print(self.grid)
        print('Build game object!')

    def start(self):
        self.__initGame()

        while True:
            self.__generateRandomGophers()
            self.__flashScreen()

            if cv2.waitKey(self.sleepTime) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

    def setGopherImage(self, newImage):
        self.gopherImage = newImage

    def setBackgroundImage(self, newImage):
        self.backgroundImage = newImage

    def __initGame(self):
        cv2.namedWindow(self.windowName)
        cv2.setMouseCallback(self.windowName, beatGopher, self)

    def __generateRandomGophers(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = random.randint(0, 10) > 5

    def __drawGophers(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]:
                    x1 = j*180
                    y1 = i*150
                    x2 = x1 + 180
                    y2 = y1 + 150
                    self.backgroundImageShown[y1:y2, x1:x2] = self.gopherImage

    def __flashScreen(self):
        self.backgroundImageShown = self.backgroundImage.copy()
        self.__drawGophers()
        cv2.imshow('gophers', self.backgroundImageShown)
        print('The score is: {}'.format(self.score))

    def beatGopher(self, x, y):
        if 0 <= x <= 540 and 0 <= y <= 450:
            i = int(y/150)
            j = int(x/180)
            if self.grid[i][j]:
                self.grid[i][j] = False
                self.score = self.score + 1
                print('Go it!')
                self.__flashScreen()
