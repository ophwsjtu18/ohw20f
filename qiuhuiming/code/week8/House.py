import mcpi.block as block
from mcpi.minecraft import Minecraft
import time
import serial

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

    name = 'Awesome House'  # 默认名字
    song = ['1', '2', '3', '2', '2']  # 默认歌曲名
    floor = None  # 地板花纹

    def __init__(self):
        print('The house position is not set yet!')

    def set_size(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_name(self, name):
        self.name = name

    def set_song(self, song):
        self.song = song

    def set_floor(self, floor):
        self.floor = floor
        self.length = len(floor)
        self.width = len(floor[0])

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

    def __build_roof(self):
        print('I will build 4 lines as 4 roof at',
              self.x, self.y + self.height, self.z)
        i = min(self.length, self.width) + 4
        count = -2
        while i > 0:
            mc.setBlocks(self.x + count, self.y + self.height - 1 + count, self.z + count, self.x + self.length - 1 - count,
                         self.y + self.height - 1 + count, self.z + self.width - 1 - count, block.DIAMOND_ORE.id)
            i = i - 2
            count = count + 1

    def __build_floor(self):
        print('I will build the floor')
        if self.floor is None:
            mc.setBlocks(self.x, self.y, self.z, self.x + self.length - 1,
                         self.y, self.z + self.width - 1, block.WOOD.id)
        else:
            for x in range(self.length):
                for z in range(self.width):
                    # print(x, z)
                    id = block.GOLD_BLOCK.id if self.floor[x][z] == '1' else block.WOOD.id
                    mc.setBlock(x + self.x, self.y, z + self.z, id)

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
        print('Start to build {}'.format(self.name))
        mc.postToChat('Start to build {}'.format(self.name))
        self.__build_floor()
        self.__build_wall()
        self.__build_roof()
        self.__build_door()
        self.__build_window()
        self.__decorate()
        mc.postToChat('Build successfully!')
        print('Build successfully!')

    def sing(self):
        ser = serial.Serial("COM3")
        while True:
            print('{} will sing: {}'.format(self.name, self.song))
            for i in self.song:
                ser.write((i + '$').encode())
                time.sleep(0.5)

    def is_comtain_tile(self, pos):
        return self.x <= pos.x < self.x + self.length and self.y <= pos.y < self.y + self.height and self.z <= pos.z < self.z + self.width

    def is_complete(self) -> bool:
        return self.x != None and self.y != None and self.z != None and self.width != None and self.height != None and self.length != None
