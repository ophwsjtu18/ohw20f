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
    def __buildwall__(self):
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
                mc.setBlock(self.x+x,self.y+self.h-1,self.z+z,45)
    def __buildfoundation__(self):
        for x in range(self.l+4):
            for z in range(self.w+4):
                mc.setBlock(self.x+x-2,self.y-1,self.z+z-2,168,1)
    def __builddoor__(self):
        for y in range(2):
            mc.setBlock(self.x+self.l//2,self.y+y,self.z+self.w-1,71)    
    def __buildwindow__(self):
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
    def __buildfloor__(self):
        for x in range(self.l-2):
            for z in range(self.w-2):
                mc.setBlock(self.x+x+1,self.y,self.z+z+1,171,6)
    def buildall(self):
        self.__buildfoundation__()
        self.__buildwall__()
        self.__buildroof()
        self.__builddoor__()
        self.__buildwindow__()
        self.__buildfloor__()

class RoundHouse(House):
    def __init__(self,x,y,z):
        super(RoundHouse,self).__init__(x,y,z)
    def setLWH(self,l,w,h):
        super(RoundHouse,self).setLWH(l,w,h)
    def __buildroof(self):
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x+x,self.y+self.h-1,self.z+z,45)
        f=open("roundroof.csv",'r')
        roundy=[]
        roundxz={}
        i=0
        for line in f:
            linedata=line.strip().split(",")
            roundy.append(linedata)
            roundxz[i]=linedata[0:-1]
            i=i+1
        for x in range(self.l):
            for z in range(self.w):
                for y in range(self.w//2):
                    if roundxz[x*15+z][y]=='0':
                        mc.setBlock(self.x+x,self.y+self.h+y,self.z+z,0)
                    if roundxz[x*15+z][y]=='1':
                        mc.setBlock(self.x+x,self.y+self.h+y,self.z+z,45)
        
    def buildall(self):
        super(RoundHouse,self).__buildfoundation__()
        super(RoundHouse,self).__buildwall__()
        super(RoundHouse,self).__builddoor__()
        super(RoundHouse,self).__buildwindow__()
        super(RoundHouse,self).__buildfloor__()
        self.__buildroof()

class TriangleHouse(House):
    def __init__(self,x,y,z):
        super(TriangleHouse,self).__init__(x,y,z)
    def setLWH(self,l,w,h):
        super(TriangleHouse,self).setLWH(l,w,h)
    def __buildroof(self):
        for y in range((self.w+1)//2):
            for x in range(self.l):
                for z in range(self.w-y*2):
                    mc.setBlock(self.x+x,self.y+self.h+y-1,self.z+z+y,45)
    def buildall(self):
        super(TriangleHouse,self).__buildfoundation__()
        super(TriangleHouse,self).__buildwall__()
        super(TriangleHouse,self).__builddoor__()
        super(TriangleHouse,self).__buildwindow__()
        super(TriangleHouse,self).__buildfloor__()
        self.__buildroof()
        
    
mc.player.setTilePos([-200,100,-200])


for i in range(3):
    house1=House(-200+i*20,100,-200)
    house1.setLWH(15,15,6)
    house1.buildall()

for i in range(3):
    house2=RoundHouse(-200+i*20,100,-220)
    house2.setLWH(15,15,6)
    house2.buildall()

for i in range(3):
    house3=TriangleHouse(-200+i*20,100,-240)
    house3.setLWH(15,15,6)
    house3.buildall()

