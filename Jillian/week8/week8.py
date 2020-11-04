import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import serial as se

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

song1 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']
song2 = ['1','1','5','5','6','6','5','4','4','3','3','2','2','1']
song3 = ['5','3','6','5','3','2','2','2','1','2','3','2','1','1']


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
        song = ['1','2','3','4','5','6','7']

    #基础设定
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        print("set LWH",l,w,h)

    def setName(self,name):
        self.name = name
        print("set name: ",self.name)

    def playSong(self,song):
        if song =='1':
            self.song = song1
        if song =='2':
            self.song = song2
        if song =='3':
            self.song = song3
        print("play song: ",song)
        
        ser = se.Serial("COM6")
        while True:
            for i in self.song:
                x = str(i+'a')
                ser.write(x.encode())
            
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

    def __buildroof(self):
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
        self.__buildroof()
        self.buildfloor()

     
house1=House(pos.x,pos.y,pos.z)
house1.setLWH(14,6,7)
house1.setName("blue_roof house")
house1.playSong('2')

house1.buildall()
