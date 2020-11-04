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
                    mc.setBlock(self.x0+x,self.y0+height,self.z0+z,17)
            length=length-1
            width=width-1
            print(length)
            print(width)
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

    def buildAll(self):
        basePlus()
        wall()
        roof()
        doorAndWindows()                            
            


mh=house(-904,1,-466,"first",10,8,6)
mh.wall()
mh.doorAndWindows()
mh.roof()
mh.basePlus()
while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.postToChat("x="+str(pos.x)+"y"+str(pos.y)+"z"+str(pos.z))
        

