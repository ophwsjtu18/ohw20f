import mcpi.minecraft as minecraft
import serial
import time

##ser = serial.Serial("COM3")
mc=minecraft.Minecraft.create()

##houseNum = 0

f = open("songs.csv","r")
songmenu = {}
songs = []
while True:
    line = f.readline()
    if line == "":
        break
    linedata = line.strip().split(",")
    print(linedata)
    songs.append(linedata)
    songmenu[linedata[0]] = linedata[1:-1]
print(songmenu)
print(songs)

class house():
    def __init__(self,x0,y0,z0,name,length,width,height):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        ##self.houseNum = houseNum
        ##houseNum = houseNum+1
        mc.postToChat("this is a house named:"+self.name+"."+"which lies in "+str(self.x0)+" "+str(self.y0)+" "+str(self.z0))
    def base(self):
        for x in range(self.length):
            for z in range(self.width):
                mc.setBlock(self.x0+x,self.y0,self.z0+z,17)
                    
    def wall(self):
        for x in range(self.length):
            for z in range(self.width):
                for y in range(self.height):
                    mc.setBlock(self.x0+x,self.y0+y,self.z0+z,5)
        for x in range(self.length-2):
            for z in range(self.width-2):
                for y in range(self.height-1):
                    mc.setBlock(self.x0+x+1,self.y0+y+1,self.z0+z+1,0)
        mc.postToChat("wall complate")

    def roof(self):
        length = self.length
        width = self.width
        y0 = self.y0
        height = self.height
        while(length>0 and width>0):
            
            for x in range(length):
                for z in range(width):
                    mc.setBlock(self.x0+x,y0+height,self.z0+z,17)
            length=length-1
            width=width-1
            ##print(length)
            ##print(width)
            y0=y0+1
        mc.postToChat("roof complate")

    def doorAndWindows(self):
        for x in range(1):
            for y in range(2):
                mc.setBlock(self.x0+1+x,self.y0+1+y,self.z0,0)
        for x in range(2):
            for y in range(2):
                mc.setBlock(self.x0+5+x,self.y0+3+y,self.z0,20)

        mc.postToChat("door and windows complate")

    

    def basePlus(self):
        print("in basePlus")
        elem1 = 20
        elem2 = 21
        p=open("design.csv","r")
        x=0
        while True:
            line=p.readline()
            if line=="":
                break
            linedata=line.strip('\n').split(",")
            for z in range(self.width):
                if linedata[z]=='1':
                    mc.setBlock(self.x0+x, self.y0, self.z0+z,elem1)
                else:
                    mc.setBlock(self.x0+x, self.y0, self.z0+z,elem2)
            x=x+1
            if x>self.length:
                break
            
        mc.postToChat("base complate")

##    def songs(self):
##        for i in songmenu[self.houseNum]:
##            print(i)
##            ser.write(i.encode())
##           time.sleep(1)

    '''def buildAll(self):
        basePlus()
        wall()
        roof()
        doorAndWindows()   '''                         
            
class RoudHouse(house):
    def __init__(self,x0,y0,z0,name,length,width,height):
        super().__init__(x0,y0,z0,name,length,width,height)

    def roof(self):
        length = self.length
        width = self.width
        y0 = self.y0
        x0=self.x0
        z0=self.z0
        height = self.height
        while(length>0 and width>0):
            
            for x in range(length):
                for z in range(width):
                    mc.setBlock(x0+x,y0+height,z0+z,17)
            length=length-2
            width=width-2
            x0=x0+1
            z0=z0+1
            ##print(length)
            ##print(width)
            y0=y0+1
        mc.postToChat("roof complate")

class TriangleHouse(house):
    def __init__(self,x0,y0,z0,name,length,width,height):
        super().__init__(x0,y0,z0,name,length,width,height)

    def roof(self):
        length = self.length
        width = self.width
        y0 = self.y0
        x0=self.x0
        z0=self.z0
        height = self.height
        i=0
        j=1
        while(length>0 and width>0):
            
            for x in range(length):
                for z in range(width):
                    for y in range(i):

                        mc.setBlock(x0+x,y0+height+y,z0+z,17)
            length=length-2
            width=width-2
            x0=x0+1
            z0=z0+1
            ##print(length)
            ##print(width)
            y0=y0+1+i
            i=i+j
            j=j+j
        mc.postToChat("roof complate")

mh0=house(-904,1,-466,"first",10,10,10)
'''mh.wall()
mh.doorAndWindows()
mh.roof()
mh.basePlus()'''
mh1=house(-924,1,-466,"second",10,10,10)
mh2=house(-944,1,-466,"third",10,10,10)
mh3=RoudHouse(-904,1,-486,"forth",10,10,10)
mh4=RoudHouse(-924,1,-486,"fifth",10,10,10)
mh5=RoudHouse(-944,1,-486,"sixth",10,10,10)
mh6=TriangleHouse(-904,1,-506,"seventh",10,10,10)
mh7=TriangleHouse(-924,1,-506,"eighth",10,10,10)
mh8=TriangleHouse(-944,1,-506,"ninth",10,10,10)
#for a in range(mh0,mh1,mh2,mh3,mh4,mh5,mh6,mh7,mh8):
mh0.wall()
mh0.doorAndWindows()
mh0.roof()
mh0.base()
mh1.wall()
mh1.doorAndWindows()
mh1.roof()
mh1.base()
mh2.wall()
mh2.doorAndWindows()
mh2.roof()
mh2.base()
mh3.wall()
mh3.doorAndWindows()
mh3.roof()
mh3.base()
mh4.wall()
mh4.doorAndWindows()
mh4.roof()
mh4.base()
mh5.wall()
mh5.doorAndWindows()
mh5.roof()
mh5.base()
mh6.wall()
mh6.doorAndWindows()
mh6.roof()
mh6.base()
mh7.wall()
mh7.doorAndWindows()
mh7.roof()
mh7.base()
mh8.wall()
mh8.doorAndWindows()
mh8.roof()
mh8.base()
while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.postToChat("x="+str(pos.x)+"y"+str(pos.y)+"z"+str(pos.z))