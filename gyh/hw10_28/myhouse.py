import mcpi.block as block
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

class House():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Build a house at", self.x, self.y, self.z)

    def set_LWH(self, l, w, h):
        if(l < 4):
            l = 4
        if(w < 4):
            w = 4
        if(h < 4):
            h = 4
        self.l = l
        self.w = w
        self.h = h
    
    def set_name(self, name):
        self.name = name
    
    def set_music(self, music):
        self.music = music  #todo

    def __build_wall(self):
        print("Build walls")
        mc.setBlocks(self.x, self.y, self.z, self.x + self.l - 1, self.y + self.h - 1, self.z + self.w - 1, block.BRICK_BLOCK.id)
        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1, self.x + self.l - 2, self.y + self.h - 2, self.z + self.w - 2, block.AIR.id)

    def __build_door(self):
        print("Build door")
        mc.setBlocks(self.x + 1, self.y + 1, self.z, self.x + 1, self.y + 2, self.z, block.AIR.id)

    def __build_window(self):
        print("Build windows")
        mc.setBlocks(self.x + self.l - 1, self.y + 2, self.z + 2, self.x + self.l - 1, self.y + 2, self.z + 3, block.GLASS.id)
        mc.setBlocks(self.x + 2, self.y + 2, self.z + self.w - 1, self.x + 3, self.y + 2, self.z + self.w - 1, block.GLASS.id)

    def __build_roof(self):
        print("Build roof")
        mc.setBlocks(self.x - 1, self.y + self.h, self.z - 1, self.x + self.l, self.y + self.h, self.z + self.w, block.STONE_SLAB.id)
        mc.setBlocks(self.x, self.y + self.h, self.z, self.x + self.l - 1, self.y + self.h, self.z + self.w - 1, block.STONE_BRICK.id)

    def __build_floor(self):
        print("BUild floor")
        f = open("floor.csv","r")
        ori_data = f.readlines()
        for x in range(len(ori_data)):
            data = ori_data[x].strip().split(",")
            for z in range(len(data)):
                if int(data[z]) == 0:
                    mc.setBlock(self.x + 1 + x, self.y, self.z + 1 + z, block.WOOD_PLANKS.id)
                else:
                    mc.setBlock(self.x + 1 + x, self.y, self.z + 1 + z, block.GOLD_BLOCK.id)
                

    def build_all(self):
        self.__build_wall()
        self.__build_door()
        self.__build_window()
        self.__build_roof()
        self.__build_floor()
        print("Finish building", self.name)

house1 = House(40, 2, -50)
house1.set_LWH(6, 6, 5)
house1.set_name("my house")

house1.build_all()

while True:
    time.sleep(2.0)
    pos=mc.player.getTilePos()
    #mc.postToChat("x:"+str(pos.x)+" y:"+str(pos.y)+" z:"+str(pos.z)) 
