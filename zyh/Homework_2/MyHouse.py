import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print("hello world, I will build a house at",self.x,self.y,self.z)
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def __buildWall(self):
        print("I will build 4 lines as 4 walls at", self.x,self.y,self.z)
    def __buildRoof(self):
        print("I will build 4 lines as 4 roof at", self.x,self.y+10,self.z)
    def buildAll(self):
        self.__buildWall()
        self.__buildRoof()
house1=House(60,0,50)
house2=House(60,40,50)

house1.buildAll()
house2.buildAll()

house1.setLWH(10,10,10)
house1.setLWH(8,10,12)


