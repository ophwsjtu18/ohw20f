import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc=minecraft.Minecraft.create()

class buildMyHouse():
    L=0
    W=0
    H=0

    def __init__(self,Length,Wide,Height,position):
        self.L=Length
        self.W=Wide
        self.H=Height
        self.pos=position
    def buildFloor(self):
        for x in range(self.L):
            for z in range (self.W):
                mc.setBlock(self.pos.x+x,self.pos.y,self.pos.z+z,block.STONE.id)
    def buildGrass(self):
        for x in range(self.L):
            for z in range (2):
                mc.setBlock(self.pos.x+x,self.pos.y,self.pos.z-z-1,2)
    def buildWall(self):
        for x in range(self.L):
            for y in range (self.H):
                mc.setBlock(self.pos.x+x,self.pos.y+y+1,self.pos.z,block.STONE.id)
                mc.setBlock(self.pos.x+x,self.pos.y+y+1,self.pos.z+self.W-1,block.STONE.id)
        for z in range(self.W-2):
            for y in range (self.H):
                mc.setBlock(self.pos.x,self.pos.y+y+1,self.pos.z+z+1,block.STONE.id)
                mc.setBlock(self.pos.x+self.L-1,self.pos.y+y+1,self.pos.z+z+1,block.STONE.id)
    def buildRoof(self):
         for x in range(self.L-2):
             for z in range(self.W-2):
                 mc.setBlock(self.pos.x+x+1,self.pos.y+self.H,self.pos.z+z+1,block.STONE.id)
    def buildDoor(self):
        for x in range(2):
            for y in range (3):
                 mc.setBlock(x+pos.x+(self.L)//2,pos.y+1+y,pos.z,0)
    def buildWindow(self):
        for z in range(4):
            for y in range (4):
                mc.setBlock(pos.x, pos.y+y+2, pos.z+z+4,20)
    def buildAll(self):
        self.buildFloor()
        self.buildWall()
        self.buildRoof()
        self.buildDoor()
        self.buildWindow()
        self.buildGrass()


pos=mc.player.getTilePos()
house1=buildMyHouse(10,10,6,pos)
house1.buildAll()
while True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))
   
