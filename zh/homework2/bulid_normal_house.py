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


#pos = POS(50, 0, 50)

bulid_id = 5


class House(object):
    def __init__(self, x, y, z, length, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height
        print("the house location:(" + str(x) + ", " + str(y) + ", " + str(z) + ") the size is: " + str(length) + '*' + str(width))

    def clear(self):
        for i in range(-2 * self.length, 2 * self.length + 1):
            for j in range(-2 * self.width, 2 * self.width + 1):
                for k in range(3 * self.height):
                    mc.setBlock(pos.x + i, pos.y + k, pos.z + j, 0)

    def creat_wall_and_floor(self):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for i in range(-(self.length//2), l_ceil):
            for j in range(-(self.width // 2), w_ceil):
                mc.setBlock(pos.x + i, pos.y, pos.z + j, bulid_id)

        for i in range(self.height):
            for j in range(-(self.width//2), w_ceil):
                mc.setBlock(pos.x - (self.length//2), pos.y + i, pos.z + j, bulid_id)
                mc.setBlock(pos.x + l_ceil - 1, pos.y + i, pos.z + j, bulid_id)
            for k in range(-(self.length//2), l_ceil):
                mc.setBlock(pos.x + k, pos.y + i, pos.z - (self.width//2), bulid_id)
                mc.setBlock(pos.x + k, pos.y + i, pos.z + w_ceil - 1, bulid_id)


        # roof
        glass_id_1 = 20

        tem_tall = (min(self.width, self.length) // 2)
        for i in range(1, tem_tall + 1):
            tem_width = self.width - 2 * i
            tem_length = self.length - 2 * i
            for j in range(-(tem_width // 2), math.ceil(tem_width / 2)):
                mc.setBlock(pos.x - (self.length // 2) + i, pos.y + self.height + i - 1, pos.z + j, 20)
                mc.setBlock(pos.x + l_ceil - 1 - i, pos.y + self.height + i - 1, pos.z + j, 20)
            for j in range(-(tem_length // 2), math.ceil(tem_length / 2)):
                mc.setBlock(pos.x + j, pos.y + self.height + i - 1, pos.z - (self.width // 2) + i, 20)
                mc.setBlock(pos.x + j, pos.y + self.height + i - 1, pos.z + w_ceil - 1 - i, 20)

    def creat_door(self):
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 1, pos.z, 0)
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 2, pos.z, 0)
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 1, pos.z, 324)

    def creat_window(self):
        glass_id_2 = 102
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for k in range(self.width // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(pos.x + l_ceil - 1, pos.y + 2 + i, pos.z + 2 + 4 * k + j, glass_id_2)
                    mc.setBlock(pos.x + l_ceil - 1, pos.y + 2 + i, pos.z - 2 - 4 * k - j, glass_id_2)
                    mc.setBlock(pos.x - (self.length // 2), pos.y + 2 + i, pos.z + 2 + 4 * k + j, glass_id_2)
                    mc.setBlock(pos.x - (self.length // 2), pos.y + 2 + i, pos.z - 2 - 4 * k - j, glass_id_2)
        for k in range(self.length // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(pos.x + 2 + 4 * k + j, pos.y + 2 + i, pos.z + w_ceil - 1, glass_id_2)
                    mc.setBlock(pos.x - 2 - 4 * k - j, pos.y + 2 + i, pos.z + w_ceil - 1, glass_id_2)
                    mc.setBlock(pos.x + 2 + 4 * k + j, pos.y + 2 + i, pos.z - (self.width // 2), glass_id_2)
                    mc.setBlock(pos.x - 2 - 4 * k - j, pos.y + 2 + i, pos.z - (self.width // 2), glass_id_2)

    def creat_whole_house(self):
        self.clear()
        self.creat_wall_and_floor()
        self.creat_door()
        self.creat_window()


house = House(pos.x, pos.y, pos.z, 28, 19, 5)
house.clear()
house.creat_whole_house()

'''
stayed_time = 0
while True:

    time.sleep(0.5)

    pos_now = mc.player.getTilePos()
    mc.postToChat(
        "please goto home x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z) + " for serveral seconds to fly")
    mc.postToChat("x:" + str(pos_now.x) + "y:" + str(pos_now.y) + "z:" + str(pos_now.z))
    
    if pos.x - size // 2 <= pos_now.x <= pos.x + size // 2 and pos.y <= pos_now.y <= pos.y + size // 2 and pos.z - size // 2 <= pos_now.z <= pos.z + size // 2:
        mc.postToChat("welcome home,please wait for 30 rounds for fly")
        # mc.postToChat("Or hit something by right click sword, you will fly immediately")
        # if len(hits) !=0:
        #    stayed_time=31
        stayed_time = stayed_time + 1
        print("stay_time" + str(stayed_time))
        if stayed_time >= 30:
            mc.player.setTilePos(pos.x, 50, pos.y)
            stayed_time = 0
    else:
        stayed_time = 0
'''