>>> import numpy as np
>>> import cv2
>>> img=cv2.imread('D:\\photo\\a.jpg',cv2.IMREAD_COLOR)
>>> cv2.imshow('image',img)


//minecraft house类
import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
class house():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print("hello world. I will build the house at",self.x,self.y,self.z)
        
    def buildfloor(self,length,width,block1):
        self.length=length
        self.width=width
        self.block1=block1
        for x in range(self.length):
            for z in range(self.width):
                mc.setBlock(self.x+x+1,self.y,self.z+z+1,self.block1)
        print("I will build the floor at",self.x,self.y,self.z)
                
    def buildwall(self,high,block2):
        self.high=high
        self.block2=block2
        for x in range(self.length):
            for y in range(self.high):
                mc.setBlock(self.x+x+1,self.y+1+y,self.z+1,self.block2)
        for z in range(self.width):
            for y in range(self.high):
                mc.setBlock(self.x+1,self.y+1+y,self.z+z+1,self.block2)
        for x in range(self.length):
            for y in range(self.high):
                mc.setBlock(self.x+x+1,self.y+1+y,self.z+self.width,self.block2)
        for z in range(self.width):
            for y in range(self.high):
                mc.setBlock(self.x+self.length,self.y+1+y,self.z+z+1,self.block2)
        print("I will build 4 line as 4 wall at",self.x,self.y,self.z)
    def builddoor(self,width2,high2):
        self.width2=width2
        self.high2=high2
        for x in range(self.width2):
            for y in range(self.high2):
                mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y+y+1,self.z+1,0)
        for x in range(self.width2):
            mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y,self.z,126)
        
    def buildwindow(self):
        if(self.length>10):
            for x in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length/4+x,self.y+self.high/2+y,self.z+1,0)
            for x in range(2):
                for y in range(2):
                    mc.setBlock(self.x+3*self.length/4+x+1,self.y+self.high/2+y,self.z+1,0)
            for z in range(2):
                for  y in range(2):
                    mc.setBlock(self.x+1,self.y+self.high/2+y,self.z+self.width/2+z,0)
            for z in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length,self.y+self.high/2+y,self.z+self.width/2+z,0)
        if(self.length<=10):
            mc.setBlock(self.x+(self.length-self.width2)/2-2,self.y+self.high/2,self.z+1,0)
            mc.setBlock(self.x+(self.length+self.width2)/2+2,self.y+self.high/2,self.z+1,0)
            for z in range(2):
                for  y in range(2):
                    mc.setBlock(self.x+1,self.y+self.high/2+y,self.z+self.width/2+z,0)
            for z in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length,self.y+self.high/2+y,self.z+self.width/2+z,0)

    def buildroof(self):
        self.length2=self.length/2+2
        for x in range(1,int(self.length2)-1,2):
            for z in range(self.width):
                mc.setBlock(self.x+x,self.y+self.high+(x+1)/2,self.z+z+1,126)
        for x in range(1,int(self.length2)-1,2):
            for z in range(self.width):
                mc.setBlock(self.x+self.length+1-x,self.y+self.high+(x+1)/2,self.z+z+1,126)
        for x in range(0,int(self.length2),2):
            for z in range(self.width):
                mc.setBlock(self.x+x,self.y+self.high+x/2,self.z+z+1,5)
        for x in range(0,int(self.length2),2):
            for z in range(self.width):
                mc.setBlock(self.x+self.length+1-x,self.y+self.high+x/2,self.z+z+1,5)
        for x in range(self.length-4):
            mc.setBlock(self.x+3+x,self.y+self.high+1,self.z+1,5)
        for x in range(self.length-4):
            mc.setBlock(self.x+3+x,self.y+self.high+1,self.z+self.width,5)
        for x in range(self.length+2):
            mc.setBlock(self.x+x,self.y+self.high,self.z,5)
        for x in range(self.length+2):
            mc.setBlock(self.x+x,self.y+self.high,self.z+self.width+1,5)
        for x in range(self.width2):
            mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y+self.high2+1,self.z,126)
        
    def addlanterns(self):
        mc.setBlock(self.x+2,self.y+self.high/2+2,self.z+2,89)
        mc.setBlock(self.x+2,self.y+self.high/2+2,self.z+self.width-1,89)
        mc.setBlock(self.x+self.length-1,self.y+self.high/2+2,self.z+2,89)
        mc.setBlock(self.x+self.length-1,self.y+self.high/2+2,self.z+self.width-1,89)
        mc.setBlock(self.x+self.length/4+1,self.y,self.z+self.width/4+1,89)
        mc.setBlock(self.x+3*self.length/4+1,self.y,self.z+self.width/4+1,89)
        mc.setBlock(self.x+self.length/4+1,self.y,self.z+3*self.width/4+1,89)
        mc.setBlock(self.x+3*self.length/4+1,self.y,self.z+3*self.width/4+1,89)
        mc.setBlock(self.x+self.length/2+1,self.y,self.z+self.width/2+1,89)
    def addrailway(self,length3):
        self.length3=length3
        for z in range(self.length3):
            mc.setBlock(self.x+self.length/2,self.y-1,self.z-z-1,91)
            mc.setBlock(self.x-1+self.length/2,self.y-1,self.z-z-1,57)
            mc.setBlock(self.x+1+self.length/2,self.y-1,self.z-z-1,57)
            mc.setBlock(self.x+self.length/2,self.y,self.z-z-1,27)
            mc.setBlock(self.x-1+self.length/2,self.y,self.z-z-1,76)
            mc.setBlock(self.x+self.length/2,self.y+1,self.z-z-1,0)
            
    def buildall(self):
        self.buildfloor(10,10,5)
        self.buildwall(6,5)
        self.builddoor(2,2)
        self.buildwindow()
        self.buildroof()
        self.addlanterns()
        self.addrailway(500)

![mc.photo](https://github.com/ophwsjtu18/ohw20f/blob/139bea3e631bf83a70777c2a593fef717f02dca3/dml/mc_20201026213012.png)
！[mc1](https://github.com/ophwsjtu18/ohw20f/blob/main/dml/mc3.png)




        
        



