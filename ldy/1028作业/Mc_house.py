from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

class House:
    def __init__(self,x,y,z,name="",song=""):
        self.a = x
        self.b = y
        self.c = z
        self.pos_list=[]
        self.name = name
        self.song =song
    def build_special_floor(self,filename,x,y,z):
        m=0

        with open(filename,"r") as f:
            for line in f.readlines():
                n = 0
                linedata=line.strip().split(",")
                for i in linedata:
                    i =eval(i)
                    if i==0:
                        block_type = block.WOOD
                    else:
                        block_type = block.GOLD_BLOCK
                    mc.setBlock(x+m,y,z+n,block_type)
                    n+=1
                m+=1
    def build(self,x,y,z):
        mc.setBlocks(x,y,z,x+self.a,y+self.b,z,block.WOOD)
        self.build_special_floor("the floor.csv",x,y,z)
        mc.setBlocks(x,y,z,x,y+self.b,z+self.c,block.WOOD)
        mc.setBlocks(x+self.a,y,z,x+self.a,y+self.b,z+self.c,block.WOOD)
        mc.setBlocks(x,y,z+self.c,x+self.a,y+self.b,z+self.c,block.WOOD)
        mc.setBlocks(x,y+self.b,z,x+self.a,y+self.b,z+self.c,block.WOOD)
        mc.setBlock(x+self.a/2,y+1,z,block.DOOR_WOOD)
        mc.setBlock(x+self.a/2,y+2,z,block.DOOR_WOOD)
        mc.setBlocks(x,y+self.b/2,z+self.c/2,x,y+self.b/3,z+self.c/3,block.GLASS)
        mc.setBlocks(x+self.a/2,y+self.b,z+self.c/2,x+self.a/3,y+self.b,z+self.c/3,block.GLASS)
        self.pos_list=[x,y,z]
    def set_length(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z
    def clear(self):
        x,y,z = self.pos_list
        mc.setBlocks(x,y,z,x+self.a,y+self.b,z,block.AIR)        




if __name__ == "__main__":
    #create the world
    mc = Minecraft.create()
    mc.postToChat("Hello World,Game will Start in 5s")

    x,y,z=10,10,8
    house = House(x,y,z)
    pos=mc.player.getTilePos()
    house.build(pos.x,pos.y,pos.z)
    