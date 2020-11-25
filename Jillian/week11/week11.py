import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import serial as se

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


class House():
    # name of house
    name = None
    # position of house
    x = None
    y = None
    z = None
    #size of house
    l = None
    w = None
    h = None
    #song of house
    song = None
    
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print("hello world, I will build a house at ",self.x,self.y,self.z)
        self.l = 0
        self.w = 0
        self.h = 0
        name = 'MY_House'
        

    #基础设定
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        print("set LWH",l,w,h)

    def setName(self,name):
        self.name = name
        print("set name: ",self.name)

    
            
    #建造房屋    
    def __buildwall(self):
        for a in range(self.l):
            for b in range(self.h):
                mc.setBlock(self.x+a,self.y+b,self.z,b%4+13)
                mc.setBlock(self.x+a,self.y+b,self.z+self.w-1,b%4+13)
        for a in range(1,self.w-1):
            for b in range(self.h):
                mc.setBlock(self.x,self.y+b,self.z+a,b%4+13)
                mc.setBlock(self.x+self.l-1,self.y+b,self.z+a,b%4+13)
        print("build wall")

    def __builddoor(self):
        for a in range(4):
            mc.setBlock(self.x+self.l/2,self.y+a,self.z,0)
            mc.setBlock(self.x+self.l/2-1,self.y+a,self.z,0)
        print("build door")

    def __buildwindow(self):
        for a in range(2,self.h-2):
            for b in range(1,int(self.l/2)-2):
                mc.setBlock(self.x+b,self.y+a,self.z,20)
            for c in range(int(self.l/2)+2,self.l-1):
                mc.setBlock(self.x+c,self.y+a,self.z,20)
        print("build window")

    def buildroof(self):
        for a in range(-1,self.l+1):
            for b in range(-1,self.w+1):
                mc.setBlock(self.x+a,self.y+self.h-1,self.z+b,22)

    def buildfloor(self):
        with open('floor.csv','r')as f:
            reader = csv.reader(f)
            for i,rows in enumerate(reader):
                for a in range(1,self.w-1):
                    if i==a:
                        for b in range(1,self.l-1):
                            if rows[b]=='0':
                                mc.setBlock(self.x+b,self.y,self.z+i,5)
                            if rows[b]=='1':
                                mc.setBlock(self.x+b,self.y,self.z+i,41)

    def buildall(self):
        self.__buildwall()
        self.__builddoor()
        self.__buildwindow()
        self.buildroof()
        self.buildfloor()


class RoundHouse(House):
    
    def buildroof(self):
        for a in range(self.l):
            mc.setBlock(self.x+a,self.y+self.h,self.z+self.w-1,22)
            mc.setBlock(self.x+a,self.y+self.h,self.z,22)
            for b in range(3):
                mc.setBlock(self.x+a,self.y+self.h+1+b,self.z+self.w-1-b,22)
                mc.setBlock(self.x+a,self.y+self.h+1+b,self.z+b,22)
       
       
        print("ROOFROOFROOF")


class TriangleHouse(House):

    def buildroof(self):
        for a in range(self.w):
            for b in range(self.l):
                mc.setBlock(self.x+b,self.y+self.h+a,self.z+a,22)
            for c in range(self.w-a):
                mc.setBlock(self.x,self.y+self.h+a,self.z+self.w-1-c,22)
                mc.setBlock(self.x+self.l-1,self.y+self.h+a,self.z+self.w-1-c,22)
        for a in range(self.l):
            for b in range(self.w):
                mc.setBlock(self.x+a,self.y+self.h+b,self.z+self.w-1,22)
       
house1=House(pos.x,pos.y,pos.z)
house1.setLWH(14,6,7)

house2=House(pos.x+20,pos.y,pos.z)
house2.setLWH(14,6,7)

house3=House(pos.x+40,pos.y,pos.z)
house3.setLWH(14,6,7)

Rhouse1=RoundHouse(pos.x,pos.y,pos.z+12)
Rhouse1.setLWH(14,6,7)

Rhouse2=RoundHouse(pos.x+20,pos.y,pos.z+12)
Rhouse2.setLWH(14,6,7)

Rhouse3=RoundHouse(pos.x+40,pos.y,pos.z+12)
Rhouse3.setLWH(14,6,7)

Thouse1=TriangleHouse(pos.x,pos.y,pos.z+24)
Thouse1.setLWH(14,6,7)

Thouse2=TriangleHouse(pos.x+20,pos.y,pos.z+24)
Thouse2.setLWH(14,6,7)

Thouse3=TriangleHouse(pos.x+40,pos.y,pos.z+24)
Thouse3.setLWH(14,6,7)



house1.buildall()
house2.buildall()
house3.buildall()
Rhouse1.buildall()
Rhouse2.buildall()
Rhouse3.buildall()
Thouse1.buildall()
Thouse2.buildall()
Thouse3.buildall()
