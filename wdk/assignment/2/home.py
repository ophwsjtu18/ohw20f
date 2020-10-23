import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

class House():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def __buildwall(self):
        for y in range(self.h-1):
            for x in range(self.l):
                mc.setBlock(self.x+x,self.y+y,self.z,112)
                mc.setBlock(self.x+x,self.y+y,self.z+self.w-1,112)
            for z in range(self.w):
                mc.setBlock(self.x,self.y+y,self.z+z,112)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+z,112)
    def __buildroof(self):
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x+x,self.y+self.h-1,self.z+z,112)
    def __buildfoundation(self):
        for x in range(self.l+4):
            for z in range(self.w+4):
                mc.setBlock(self.x+x-2,self.y-1,self.z+z-2,168,1)
    def __builddoor(self):
        for y in range(2):
            mc.setBlock(self.x+self.l//2,self.y+y,self.z+self.w-1,71)    
    def __buildwindow(self):
        for y in range(3):
            for x in range(self.l//4):
                mc.setBlock(self.x+x+self.l//8,self.y+y+1,self.z+self.w-1,102)
                mc.setBlock(self.x-x+self.l*7//8,self.y+y+1,self.z+self.w-1,102)
                mc.setBlock(self.x+x+self.l//8,self.y+y+1,self.z,102)
                mc.setBlock(self.x-x+self.l*7//8,self.y+y+1,self.z,102)
            for z in range(self.w//4):
                mc.setBlock(self.x,self.y+y+1,self.z+z+self.w//8,102)
                mc.setBlock(self.x,self.y+y+1,self.z-z+self.w*7//8,102)
                mc.setBlock(self.x+self.l-1,self.y+y+1,self.z+z+self.w//8,102)
                mc.setBlock(self.x+self.l-1,self.y+y+1,self.z-z+self.w*7//8,102)
    def __buildfloor(self):
        for x in range(self.l-2):
            for z in range(self.w-2):
                mc.setBlock(self.x+x+1,self.y,self.z+z+1,171,6)
    def buildall(self):
        self.__buildfoundation()
        self.__buildwall()
        self.__buildroof()
        self.__builddoor()
        self.__buildwindow()
        self.__buildfloor()

    
house1=House(0,80,0)
mc.player.setTilePos([-1,80,-1])

house1.setLWH(10,10,6)

house1.buildall()


