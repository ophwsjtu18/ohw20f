import mcpi.minecraft as minecraft


mc = minecraft.Minecraft.create()


class House():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setLWH(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def __build_roof(self):
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x + x, self.y + self.h-1, self.z + z, 1)

    def __build_wall(self):
        for y in range(self.h):
            for x in range(self.l):
                mc.setBlock(self.x + x, self.y + y, self.z, 1)
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 1)
            for z in range(self.w):
                mc.setBlock(self.x, self.y + y, self.z + z, 1)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + z, 1)

    def __build_floor(self):
        for x in range(self.l+6):
            for z in range(self.w+6):
                mc.setBlock(self.x - 3 + x, self.y, self.z - 3 + z, 2)
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x + x, self.y, self.z + z, 3)

    def __build_door(self):
        door_l = self.l//3
        door_h = self.h//2
        for x in range(door_l, 2*door_l):
            for y in range(1, door_h):
                mc.setBlock(self.x + x, self.y + y, self.z, 0)

    def __build_window(self):
        window_l = self.l//3
        window_h = self.h//3
        for x in range(window_l, 2*window_l):
            for y in range(window_h, 2*window_h):
                mc.setBlock(self.x + x, self.y + y, self.z + self.w - 1, 20)
                mc.setBlock(self.x, self.y + y, self.z + x, 20)
                mc.setBlock(self.x + self.l - 1, self.y + y, self.z + x, 20)

    def build_all(self):
        self.__build_floor()
        self.__build_wall()
        self.__build_roof()
        self.__build_door()
        self.__build_window()


house1 = House(-364, -2, -48)
house1.setLWH(10, 10, 10)
house1.build_all()
