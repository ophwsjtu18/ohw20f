import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import serial
from math import *
f=open(r'C:\Users\OUT XB\Desktop\floor.csv',"r")
while True:
    line=f.readline()
    if line == "":
	    break
    floorData=line.strip().split(",")
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
def Trans2int(x):
    if x - int(x) >= 0.3:
        return int(x) + 1
    else:
        return int(x)
class House():
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        print("hello world, I will build a house at",self.x,self.y,self.z)
    def __buildBase__(self):
        for x in range(self.l):
            for z in range(self.w+3):
                if floorData[x*self.w+z]=='0':
                    mc.setBlock(self.x+x,self.y-1,self.z+z-2,block.STONE.id)
                else:
                    mc.setBlock(self.x+x,self.y-1,self.z+z-2,block.GOLD_BLOCK.id)
    def __buildWall__(self):
        for y in range(self.h):
            for a in range(self.l):
                mc.setBlock(self.x+a,self.y+y,self.z,45)
                mc.setBlock(self.x+a,self.y+y,self.z+self.w,45)
            for a in range(self.w-1):
                mc.setBlock(self.x,self.y+y,self.z+1+a,45)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+1+a,45)
    def __buildRoof__(self):
        for n in range(min(self.l,self.w)):
            for x in range(n,self.l-n):
                for z in range(n,self.w-n):
                    if n!=min(self.l/2,self.w/2)-1:
                        mc.setBlock(self.x+x,self.y+self.h-1+n,self.z+z,48)
                    else:
                        mc.setBlock(self.x+x,self.y+self.h-1+n,self.z+z,116)
    def __buildDoor__(self):
        mc.setBlock(self.x+(self.l)/2,self.y+1,self.z,0)
        mc.setBlock(self.x+(self.l)/2,self.y,self.z,0)
        mc.setBlock(self.x+(self.l)/2,self.y+1,self.z,64)
        mc.setBlock(self.x+(self.l)/2,self.y,self.z-1,64)
    def __buildWindow__(self):
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z,20)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+1,0)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+self.w,20)
                mc.setBlock(self.x+(self.l/2)+z,self.y+y+self.h-self.h/2,self.z+self.w-1,0)
    def WriteMyName__(self):
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
        self.__buildBase__()
        self.__buildWall__()
        self.__buildRoof__()
        self.__buildDoor__()
        self.__buildWindow__()
        ##self.WriteMyName__()
        mc.setBlock(self.x,self.y+self.h,self.z,76)
        mc.setBlock(self.x+self.l-1,self.y+self.h,self.z,76)
        mc.setBlock(self.x,self.y+self.h,self.z+self.w-1,76)
        mc.setBlock(self.x+self.l-1,self.y+self.h,self.z+self.w-1,76)
class RoundHouse(House):
    def __init__(self,x,y,z,l,w,h,r):
        super(RoundHouse,self).__init__(x,y,z,l,w,h)
        self.r=r
        print("i will build a round roof house r is",self.r)
    def __buildRoof(self):
        print("build a round roof")
        for a in range(self.l):
            for b in range(self.w):
                mc.setBlock(self.x + a,self.y + self.h,self.z + b,48)
        midPos = min(self.l,self.w)/2
        for floor in range(self.r):
            R = self.r - floor
            height = self.h + floor
            for i in range(2*R):
                if i < R:
                    Len = Trans2int((2.0*R*i-i**2)**0.5)
                else:
                    Len = Trans2int((2.0*R*(2.0*R-i)-(2.0*R-i)**2)**0.5)
                startPosx = self.x + floor
                startPosz = self.z + midPos - Len/2
                for j in range(Len):
                    mc.setBlock(startPosx + i,self.y+floor+self.h + 1,startPosz + j,48)
    def buildAll(self):
        super(RoundHouse,self).__buildBase__()
        self.__buildRoof()
        super(RoundHouse,self).__buildWall__()
        super(RoundHouse,self).__buildDoor__()
        super(RoundHouse,self).__buildWindow__()
        ##self.__buildRoof()
        ##super(RoundHouse,self).WriteMyName__()
class TriangleHouse(House):
    def __init__(self,x,y,z,l,w,h):
        super(TriangleHouse,self).__init__(x,y,z,l,w,h)
        print("i will build a triangle roof house")
    def __buildRoof(self):
        print("build a triangle roof")
        x0=self.x
        y0=self.y
        z0=self.z
        length=self.l
        width=self.w
        height=self.h
        while(length>0 and width>0):
            for x in range(length):
                for z in range(width):
                    mc.setBlock(x0+x,y0+height,z0+z,17)
            length=length-1
            width=width-1
            y0=y0+1
    def buildAll(self):
        super(TriangleHouse,self).__buildBase__()
        self.__buildRoof()
        super(TriangleHouse,self).__buildWall__()
        super(TriangleHouse,self).__buildDoor__()
        super(TriangleHouse,self).__buildWindow__()
        ##super(RoundHouse,self).WriteMyName__()
for i in range(3):
    House(pos.x,pos.y,pos.z+i*32,30,30,15).buildAll()
for i in range(3):
   TriangleHouse(pos.x+32,pos.y,pos.z+i*32,30,30,15).buildAll()
for i in range(3):
    RoundHouse(pos.x+64,pos.y,pos.z+i*32,30,30,15,15).buildAll()
##house2.buildall(
##for y in range(10):
##    for a in range(10):
##        mc.setBlock(pos.x+a, pos.y+y, pos.z,block.STONE.id)
##        mc.setBlock(pos.x+a, pos.y+y, pos.z+9,block.STONE.id)
##    for a in range(8):
##        mc.setBlock(pos.x, pos.y+y, pos.z+1+a,block.STONE.id)
##        mc.setBlock(pos.x+9, pos.y+y, pos.z+1+a,block.STONE.id)
##for x in range(10):
##    for z in range(10):
##        mc.setBlock(pos.x+x, pos.y, pos.z+z,block.STONE.id)
##for x in range(10):
##    for z in range(10):
##        mc.setBlock(pos.x+x, pos.y+9, pos.z+z, block.STONE.id)
##mc.setBlock(pos.x+5, pos.y+1, pos.z，block.AIR.id)
##
##mc.setBlock(pos.x+5, pos.y+1, pos.z，block.AIR.id)
##for z in range(2):
##    for y in range(2):
##        mc.setBlock(pos.x+10, pos.y+y+2, pos.z+z+4, block.GLASS.id)
##
