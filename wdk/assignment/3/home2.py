import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import serial

#歌曲需要板子才能运行
#ser = serial.Serial("COM6")
mc = minecraft.Minecraft.create()

class House():
    def __init__(self,x,y,z,na,song):
        self.x=x
        self.y=y
        self.z=z
        self.na=na
        self.song=song
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def __buildwall(self):
        for y in range(self.h):
            for x in range(self.l):
                mc.setBlock(self.x+x,self.y+y,self.z,112)
                mc.setBlock(self.x+x,self.y+y,self.z+self.w-1,112)
            for z in range(self.w):
                mc.setBlock(self.x,self.y+y,self.z+z,112)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+z,112)
    def __buildroof(self):
        for x in range(self.l-2):
            for z in range(self.w-2):
                mc.setBlock(self.x+x+1,self.y+self.h-1,self.z+z+1,20)
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
        f=open("floor.csv",'r')
        floorx=[]
        floorz={}
        i=0
        for line in f:
            linedata=line.strip().split(",")
            floorx.append(linedata)
            floorz[i]=linedata[0:-1]
            i=i+1
        for x in range(self.l-2):
            for z in range(self.w-2):
                if floorz[z][x]=='0':
                    mc.setBlock(self.x+x+1,self.y-1,self.z+z+1,5,2)
                if floorz[z][x]=='1':
                    mc.setBlock(self.x+x+1,self.y-1,self.z+z+1,41)
    def name(self):
        mc.postToChat("welcome to the home of "+self.na)
    '''
    def songs(self):
        f=open("songs.csv","r")
        songs=[]
        songmenu={}
        for line in f:
            line = f.readline()
            linedata=line.strip().split(",")
            songs.append(linedata)
            songmenu[linedata[0]]=linedata[1:-1]
            for i in [0,-1]:
                songmenu[linedata[0]][i] = songmenu[linedata[0]][i] + "a"
        for i in [0,-1]:
            ser.write(songmenu[song][i].encode())
            time.sleep(0.2)
    '''
    def buildall(self):
        self.__buildfoundation()
        self.__buildwall()
        self.__buildroof()
        self.__builddoor()
        self.__buildwindow()
        self.__buildfloor()

    
X=0
Y=50
Z=0
Name="wdk"
Song="tinklestar"
house1=House(X,Y,Z,Name,Song)
mc.player.setTilePos([X-1,Y,Z-1])

L=10
W=10
H=6

house1.setLWH(L,W,H)

house1.buildall()

while True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    if X<=pos.x<=X+L-1 and Z<=pos.z<=Z+W-1 and Y<=pos.y<=Y+H-1:
        house1.name()
        #house1.songs()
    
