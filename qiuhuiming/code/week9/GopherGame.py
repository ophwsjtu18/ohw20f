import cv2
import numpy as np
import random


class GopherGame:
    width = 800
    height = 600

    backgroundImage = 100 * np.ones((height, width, 3), dtype=np.uint8)
    gopherImage = cv2.imread('./gopher.png')[0:150, 70: 250]

    grid = [[True for i in range(3)] for j in range(3)]

    windowName = 'gophers'

    def __init__(self):
        # print(self.grid)
        print('Build game object!')

    def setGopherImage(self, newImage):
        self.gopherImage = newImage

    def setBackgroundImage(self, newImage):
        self.backgroundImage = newImage

    def start(self):
        while True:
            backgroundImageShown = self.backgroundImage.copy()
            self.__generateRandomGophers()
            self.__drawGophers(backgroundImageShown)
            cv2.imshow('gophers', backgroundImageShown)

            if cv2.waitKey(1000) & 0xFF == ord('q'):
                break

    def __generateRandomGophers(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = random.randint(0, 10) > 5

    def __drawGophers(self, backgroundImageShown):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]:
                    x1 = i*180
                    y1 = j*150
                    x2 = x1 + 180
                    y2 = y1 + 150
                    backgroundImageShown[y1:y2, x1:x2] = self.gopherImage
