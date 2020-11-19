from math import sqrt
import mcpi.block as block
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


class House():
    # x, y, z 是房子一个角的坐标
    x = None
    y = None
    z = None
    # length，width，height分别加在x、z、y上
    length = None
    width = None
    height = None

    def set_size(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_position(self):
        mc.postToChat('Your house at (x: {}, y: {}, z: {})'.format(
            self.x, self.y, self.z))

    def __build_wall(self):
        print('I will build 4 lines as 4 wall at', self.x, self.y, self.z)

        block_id = block.GOLD_BLOCK.id
        mc.setBlocks(self.x, self.y + 1, self.z, self.x + self.length - 1,
                     self.y + self.height - 2, self.z + self.width - 1, block_id)
        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1, self.x + self.length - 2,
                     self.y + self.height - 2, self.z + self.width - 2, block.AIR.id)

    def build_roof(self):
        print('I will build 4 lines as 4 roof at',
              self.x, self.y + self.height, self.z)
        block_id = block.DIAMOND_ORE.id
        mc.setBlocks(self.x, self.y + self.height - 1, self.z, self.x + self.length -
                     1, self.y + self.height - 1, self.z + self.width - 1, block_id)

    def __build_floor(self):
        print('I will build the floor')
        mc.setBlocks(self.x, self.y, self.z, self.x + self.length - 1,
                     self.y, self.z + self.width - 1, block.STONE.id)

    def __build_door(self):
        print('I will build the door')
        # 门宽为3，高为4，要确保长和高足够大
        if self.length > 6 and self.height > 6:
            mc.setBlocks(self.x + 4, self.y + 1, self.z, self.x + 6,
                         self.y + 4, self.z, block.DOOR_DARK_OAK.id)

    def __build_window(self):
        print('I will build the window.')
        if self.width > 6 and self.height > 10:
            mc.setBlocks(self.x, self.y + self.height - 6, self.z + 7, self.x,
                         self.y + self.height - 3, self.z + 10, block.AIR.id)
            mc.setBlocks(self.x + self.length - 1, self.y + self.height - 6, self.z + 7, self.x + self.length - 1,
                         self.y + self.height - 3, self.z + 9, block.AIR.id)

    def __decorate(self):
        mc.setBlock(self.x + 3, self.y + 4, self.z, block.FIRE.id)
        mc.setBlock(self.x + 7, self.y + 4, self.z, block.FIRE.id)

    def build(self):
        if not self.is_complete():
            print('Some parameters are not set yet!')
            return
        self.__build_floor()
        self.__build_wall()
        self.build_roof()
        self.__build_door()
        self.__build_window()
        self.__decorate()

    def is_comtain_tile(self, pos):
        return self.x <= pos.x < self.x + self.length and self.y <= pos.y < self.y + self.height and self.z <= pos.z < self.z + self.width

    def is_complete(self) -> bool:
        return self.x != None and self.y != None and self.z != None and self.width != None and self.height != None and self.length != None


class TriangleHouse(House):
    # 尖顶房子
    def build_roof(self):
        print('TriangleHouse Roof.')

        block_id = block.DIAMOND_ORE.id
        i = min(self.length, self.width) + 4
        count = -2
        while i > 0:
            mc.setBlocks(self.x + count, self.y + self.height - 1 + count, self.z + count, self.x + self.length - 1 - count,
                         self.y + self.height - 1 + count, self.z + self.width - 1 - count, block_id)
            i = i - 2
            count = count + 1


def distance(p1, p2, d=3):
    # p1, p2: 元组，长度为d
    res = 0
    for i in range(d):
        res = res + (p1[i] - p2[i])**2
    return sqrt(res)


class RoundHouse(House):
    # 圆顶房子
    def build_roof(self):
        print('RoundHouse Roof.')
        # 建议长宽相等
        ratio = int(min(self.width, self.length)/2)
        center_x = self.x + self.length/2
        center_y = self.y + self.height
        center_z = self.z + self.width/2
        center = (center_x, center_y, center_z)
        block_id = block.DIAMOND_ORE.id
        mc.setBlocks(self.x, self.y + self.height - 1, self.z, self.x + self.length -
                     1, self.y + self.height - 1, self.z + self.width - 1, block_id)
        # 以(center_x,  center_y, center_z)为圆心，ratio为半径，做一个上半球
        for x in range(self.x - 2, self.x + self.length + 2):
            for y in range(center_y, center_y + 2*ratio):
                for z in range(self.z - 2, self.z + self.width + 2):
                    if distance(center, (x, y, z)) <= ratio:
                        mc.setBlock(x, y, z, block_id)


if __name__ == "__main__":
    house = House()
    pos = mc.player.getTilePos()
    house.set_position(pos.x + 1, pos.y, pos.z + 5)
    house.set_size(30, 30, 20)

    triangle_house = TriangleHouse()
    triangle_house.set_position(pos.x + 50, pos.y, pos.z + 5)
    triangle_house.set_size(30, 30, 20)

    round_house = RoundHouse()
    round_house.set_position(pos.x + 100, pos.y, pos.z + 5)
    round_house.set_size(30, 30, 20)

    mc.postToChat('Start to build.')

    house.build()
    triangle_house.build()
    round_house.build()

    mc.postToChat('Build Successfully!')
