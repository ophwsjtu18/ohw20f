import mcpi.block as block
import csv
import time
import math as m
import mcpi.minecraft as minecraft
song1=["1","1","5","5","6","6","5"]
song2=["3","3","4","5","5","4","3","2","1","1","2","3","3"]
songMenu={}
songMenu["tinkleStar"]=song1
songMenu["OdeToJoy"]=song2
class myHouse():
    houseName="spouse"
    # position
    x=0
    y=0
    z=0
    # size
    L=0
    W=0
    H=0
    song=None
       
    def __init__(self,Length,Wide,Height,x1,y1,z1,pos):
        self.L=Length
        self.W=Wide
        self.H=Height
        self.pos=pos
        self.x=x1+pos.x
        self.y=y1+pos.y
        self.z=z1+pos.z
    def rename(self,newName):
        self.houseName=newName
    def setSong(self,song):
        self.song=song
    def singSong(self):
        ser=serial.Serial("COM6",9600,timeout=1)
        for a in self.song:
            ser.write(a.encode())
            time.sleep(0.5)
    def buildFloor(self):
        with open("floor.csv","r") as f:
            reader=csv.reader(f)
            for x in range(self.L):
                for z in range (self.W):
                    mc.setBlock(self.x+x,self.y,self.z+z,block.STONE.id)
            for i,row in enumerate(reader):
                for j,a in enumerate(row):
                    if a=='1':
                        mc.setBlock(self.x+i,self.y,self.z+j,41)
                    if a=='2':
                        mc.setBlock(self.x+i,self.y,self.z+j,57)
    def buildWall(self):
        for x in range(self.L):
            for y in range (self.H):
                mc.setBlock(self.x+x,self.y+y+1,self.z,block.STONE.id)
                mc.setBlock(self.x+x,self.y+y+1,self.z+self.W-1,block.STONE.id)
        for z in range(self.W-2):
            for y in range (self.H):
                mc.setBlock(self.x,self.y+y+1,self.z+z+1,block.STONE.id)
                mc.setBlock(self.x+self.L-1,self.y+y+1,self.z+z+1,block.STONE.id)  
    def buildWindow(self):
        for z in range(4):
            for y in range (4):
                mc.setBlock(self.x,self.y+y+2, self.z+z+4,20)
    def buildRoof(self):
        for y in range(6):
             for x in range(self.L+2-2*y):
                 for z in range(self.W+2-2*y):
                     if y%2:
                         mc.setBlock(self.x+x-1+y,self.y+self.H+1+y,self.z+z-1+y,57)
                     else:
                         mc.setBlock(self.x+x-1+y,self.y+self.H+1+y,self.z+z-1+y,79)     
    def buildDoor(self):
        for x in range(2):
            for y in range (3):
                 mc.setBlock(self.x+x+(self.L)//2,self.y+1+y,self.z,330)
    def buildAll(self):
        self.buildFloor()
        self.buildWall()
        self.buildRoof()
        self.buildDoor()
        self.buildWindow()
class roundHouse(myHouse):
    def buildRoof(self):
        Midx=self.W/2
        Midz=self.L/2
        Radius=m.sqrt(Midx*Midx+Midz*Midz)
        for y in range(min(self.W,self.L)):
            for x in range(min(self.W,self.L)):
                for z in range (min(self.W,self.L)):
                    distance=m.sqrt(m.pow(Midx-x,2)+m.pow(Midz-z,2)+m.pow(y,2))
                    if distance<Radius:
                         mc.setBlock(self.x+x,self.y+self.H+1,self.z+z,57)
class TraHouse(myHouse):
    def buildRoof(self):
        Midx=self.W/2
        Midz=self.L/2
        for y in range(self.W):
            for x in range(self.W-y):
                for z in range (self.L-x-y):
                        mc.setBlock(self.x+x,self.y+self.H+1+y,self.z+z,57)
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
for x in range(3):
    print(pos)
    house1=myHouse(15,15,7,0,0,20*x,pos)
    house1.buildAll()
    house2=roundHouse(15,15,7,20,0,20*x,pos)
    house2.buildAll()
    house3=TraHouse(15,15,7,40,0,20*x,pos)
    house3.buildAll()
