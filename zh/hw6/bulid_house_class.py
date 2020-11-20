import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()


class POS():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# pos = POS(50, 0, 50)

bulid_id = 5


class House(object):
    def __init__(self, x, y, z, length, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height
        print("the house location:(" + str(x) + ", " + str(y) + ", " + str(z) + ") the size is: " + str(
            length) + '*' + str(width))

    def clear(self):
        for i in range(-2 * self.length, 2 * self.length + 1):
            for j in range(-2 * self.width, 2 * self.width + 1):
                for k in range(3 * self.height):
                    mc.setBlock(self.x + i, self.y + k, self.z + j, 0)

    def creat_wall_and_floor(self, build_id=41):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)

        for i in range(-(self.length // 2), l_ceil):
            for j in range(-(self.width // 2), w_ceil):
                mc.setBlock(self.x + i, self.y, self.z + j, build_id)

        for i in range(self.height):
            for j in range(-(self.width // 2), w_ceil):
                mc.setBlock(self.x - (self.length // 2), self.y + i, self.z + j, build_id)
                mc.setBlock(self.x + l_ceil - 1, self.y + i, self.z + j, build_id)
            for k in range(-(self.length // 2), l_ceil):
                mc.setBlock(self.x + k, self.y + i, self.z - (self.width // 2), build_id)
                mc.setBlock(self.x + k, self.y + i, self.z + w_ceil - 1, build_id)

    def creat_roof(self, roof_id = 57):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for i in range(-(self.length // 2) + 1, l_ceil - 1):
            for j in range(-(self.width // 2) + 1, w_ceil - 1):
                mc.setBlock(self.x + i, self.y + self.height - 1, self.z + j, roof_id)

    def creat_door(self):
        mc.setBlock(self.x + math.ceil(self.length / 2) - 1, self.y + 1, self.z, 0)
        mc.setBlock(self.x + math.ceil(self.length / 2) - 1, self.y + 2, self.z, 0)
        mc.setBlock(self.x + math.ceil(self.length / 2) - 1, self.y + 1, self.z, 324)

    def creat_window(self, window_id=102):

        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for k in range(self.width // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(self.x + l_ceil - 1, self.y + 2 + i, self.z + 2 + 4 * k + j, window_id)
                    mc.setBlock(self.x + l_ceil - 1, self.y + 2 + i, self.z - 2 - 4 * k - j, window_id)
                    mc.setBlock(self.x - (self.length // 2), self.y + 2 + i, self.z + 2 + 4 * k + j, window_id)
                    mc.setBlock(self.x - (self.length // 2), self.y + 2 + i, self.z - 2 - 4 * k - j, window_id)
        for k in range(self.length // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(self.x + 2 + 4 * k + j, self.y + 2 + i, self.z + w_ceil - 1, window_id)
                    mc.setBlock(self.x - 2 - 4 * k - j, self.y + 2 + i, self.z + w_ceil - 1, window_id)
                    mc.setBlock(self.x + 2 + 4 * k + j, self.y + 2 + i, self.z - (self.width // 2), window_id)
                    mc.setBlock(self.x - 2 - 4 * k - j, self.y + 2 + i, self.z - (self.width // 2), window_id)

    def creat_whole_house(self):
        self.creat_wall_and_floor()
        self.creat_door()
        self.creat_window()
        self.creat_roof()

class House_triangle(House):
    def creat_roof(self, roof_id = 57):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        tem_tall = (min(self.width, self.length) // 2)
        for i in range(1, tem_tall + 1):
            tem_width = self.width - 2 * i
            tem_length = self.length - 2 * i
            for j in range(-(tem_width // 2), math.ceil(tem_width / 2)):
                mc.setBlock(self.x - (self.length // 2) + i, self.y + self.height + i - 1, self.z + j, roof_id)
                mc.setBlock(self.x + l_ceil - 1 - i, self.y + self.height + i - 1, self.z + j, roof_id)
            for j in range(-(tem_length // 2), math.ceil(tem_length / 2)):
                mc.setBlock(self.x + j, self.y + self.height + i - 1, self.z - (self.width // 2) + i, roof_id)
                mc.setBlock(self.x + j, self.y + self.height + i - 1, self.z + w_ceil - 1 - i, roof_id)

    def creat_whole_house(self):
        self.creat_wall_and_floor()
        self.creat_door()
        self.creat_window()
        self.creat_roof()

class House_circle(House):
    def creat_roof(self, roof_id = 57):
        r = int(min(self.width, self.length) / 2) - 1
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for i in range(-(self.length // 2) + 1, l_ceil - 1):
            for j in range(-(self.width // 2) + 1, w_ceil - 1):
                mc.setBlock(self.x + i, self.y + self.height - 1, self.z + j, roof_id)
        # r为半径，做一个上半球
        #print('r:' ,r)
        for i in range(-(self.length // 2), l_ceil):
            x = self.x + i
            for j in range(self.y + self.height, self.y + 2 * r + self.height):
                y = j
                for k in range(-(self.width // 2), w_ceil):
                    z = self.z + k
                    if self.__distance__(self.x, self.y + self.height, self.z, x, y, z) <= r:
                        mc.setBlock(x, y, z, roof_id)

    def __distance__(self, x1, y1, z1, x2, y2, z2):
        dis = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        return math.sqrt(dis)

    def creat_whole_house(self):
        self.creat_wall_and_floor()
        self.creat_door()
        self.creat_window()
        self.creat_roof()

if __name__ == '__main__':
    #clear

    print('clearing...')
    for i in range(-100, 100):
        for j in range(-50, 50):
            for k in range(25):
                mc.setBlock(pos.x + i, pos.y + k, pos.z + j, 0)
    print('clear over')
    print('creating house...')
    house1 = House(pos.x, pos.y, pos.z, 21, 21, 6)
    house1.creat_whole_house()
    print('creat house end')

    print('creating house_triangle...')
    house2 = House_triangle(pos.x - 30, pos.y, pos.z, 21, 21, 6)
    house2.creat_whole_house()
    print('creat house_triangle end')

    print('creating house_circle...')
    house3 = House_circle(pos.x + 30, pos.y, pos.z, 21, 21, 6)
    house3.creat_whole_house()
    print('creat house_circle end')
    