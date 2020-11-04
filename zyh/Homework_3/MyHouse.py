import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import serial
from math import *
#ser = serial.Serial("COM3")
f=open(r'C:\Users\OUT XB\Desktop\floor.csv',"r")
while True:
    line=f.readline()
    if line == "":
	    break
    floorData=line.strip().split(",")
print(len(floorData))
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
def setBlockUD(x,y,z,direct,n):
    for i in range(n):
        mc.setBlock(x,y+direct*i,z,57)            
def setBlockLR(x,y,z,direct,n):
    for i in range(n):
        mc.setBlock(x,y,z+direct*i,57)  
def setBlockLN(x,y,z,direct,n):
    for i in range(n):
        mc.setBlock(x,y+direct*i,z+direct*i,57)
def setBlockNL(x,y,z,direct,n):
    for i in range(n):
        mc.setBlock(x,y-direct*i,z+direct*i,57)
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
    def __buildBase(self):
        for x in range(self.l):
            for z in range(self.w+3):
                if floorData[x*self.w+z]=='0':
                    mc.setBlock(self.x+x,self.y-1,self.z+z-2,block.STONE.id)
                else:
                    mc.setBlock(self.x+x,self.y-1,self.z+z-2,block.GOLD_BLOCK.id)
    def __buildWall(self):
        for y in range(self.h):
            for a in range(self.l):
                mc.setBlock(self.x+a,self.y+y,self.z,45)
                mc.setBlock(self.x+a,self.y+y,self.z+self.w,45)
            for a in range(self.w-1):
                mc.setBlock(self.x,self.y+y,self.z+1+a,45)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+1+a,45)
    def __buildRoof(self):
        for n in range(min(self.l,self.w)):
            for x in range(n,self.l-n):
                for z in range(n,self.w-n):
                    if n!=min(self.l/2,self.w/2)-1:
                        mc.setBlock(self.x+x,self.y+self.h-1+n,self.z+z,48)
                    else:
                        mc.setBlock(self.x+x,self.y+self.h-1+n,self.z+z,116)
    def __buildDoor(self):
        mc.setBlock(self.x+(self.l)/2,self.y+1,self.z,0)
        mc.setBlock(self.x+(self.l)/2,self.y,self.z,0)
        mc.setBlock(self.x+(self.l)/2,self.y+1,self.z,64)
        mc.setBlock(self.x+(self.l)/2,self.y,self.z-1,64)
    def __buildWindow(self):
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z,20)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+1,0)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+self.w,20)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+self.w-1,0)
    def WriteMyName(self):
        ## Z
        setBlockLR(self.x,self.y+1,self.z+1,1,7)
        setBlockLN(self.x,self.y+1,self.z+1,1,7)
        setBlockLR(self.x,self.y+7,self.z+7,-1,7)
        ## Y
        setBlockNL(self.x,self.y+7,self.z+9,1,4)
        setBlockLN(self.x,self.y+4,self.z+12,1,4)
        setBlockUD(self.x,self.y+4,self.z+12,-1,4)
        ## H
        setBlockLR(self.x,self.y+4,self.z+18,1,7)
        setBlockUD(self.x,self.y+4,self.z+18,1,4)
        setBlockUD(self.x,self.y+4,self.z+18,-1,4)
        setBlockUD(self.x,self.y+4,self.z+24,1,4)
        setBlockUD(self.x,self.y+4,self.z+24,-1,4)
    def buildAll(self):
        self.__buildBase()
        self.__buildWall()
        self.__buildRoof()
        self.__buildDoor()
        self.__buildWindow()
        self.WriteMyName()
        mc.setBlock(self.x,self.y+self.h,self.z,76)
        mc.setBlock(self.x+self.l-1,self.y+self.h,self.z,76)
        mc.setBlock(self.x,self.y+self.h,self.z+self.w-1,76)
        mc.setBlock(self.x+self.l-1,self.y+self.h,self.z+self.w-1,76)
house1=House(pos.x,pos.y,pos.z)
##house2=House(100,200,200)

house1.setLWH(15,30,10)
##house2.setLWH(8,10,12)

house1.buildAll()
##house2.buildAll()



