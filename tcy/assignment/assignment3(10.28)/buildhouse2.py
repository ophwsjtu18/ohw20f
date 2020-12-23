import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import time
mc=minecraft.Minecraft.create()
ser = serial.Serial("COM10")
f=open("blocks.csv","r")


class Katya_House():

    def __init__(self,xyz,q,u,v):
        self.x=xyz[0]
        self.y=xyz[1]
        self.z=xyz[2]

        self.q=q
        self.u=u
        self.v=v
        print("hello world",self.x,self.y,self.z)
    def setLWH(self, lwh):
        self.l = lwh[0]
        self.w = lwh[1]
        self.h = lwh[2]

    def set_housename(self,name):
        self.name=name

    def add_song(self,song):
        self.song=song
    def __buildwall(self):
        print("I will build wall",self.x,self.y,self.z)
        for y  in range(self.w):
            for x in range (0,self.l-1,2):
                mc.setBlock(self.x+x,self.y+y,self.z,self.q)
                mc.setBlock(self.x+x,self.y+y,self.z+self.h-1,self.q)
                mc.setBlock(self.x+x+1,self.y+y,self.z,self.u)
                mc.setBlock(self.x+x+1,self.y+y,self.z+self.h-1,self.u)
        for y in range(self.w):
            for a in range(0,self.h-3,2):
                mc.setBlock(self.x,self.y+y,self.z+1+a,self.q)
                mc.setBlock(self.x,self.y+y,self.z+1+a+1,self.u)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+1+a,self.u)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+1+a+1,self.q)
    def __buildroof(self):
        print("i will build 4 line as 4 wall at",self.x,self.y+self.h,self.z)
        for x in range(0,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y,self.z+z,self.v)
                mc.setBlock(self.x+x,self.y,self.z+z+1,self.u)
        for x in range(1,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y,self.z+z,self.u)
                mc.setBlock(self.x+x,self.y,self.z+z+1,self.v)
                
        for x in range(self.l):
            for z in range(self.h):
               mc.setBlock(self.x+x,self.y+self.w-1,self.z+z,89)

    def __builddoor(self):
        print("I will build 1 door at",self.x+self.l/2,self.y,self.z)
        mc.setBlock(self.x+self.l-1,self.y+1,self.z+self.h/2,0)
        mc.setBlock(self.x+self.l-1,self.y+2,self.z+self.h/2,0)
        
    def __buildwindows(self):
        print("I will build 1 windows at",self.x+self.l,self.y+3,self.z+5)
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+self.l-1,self.y+y+2,self.z+z+self.h/4,20)
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+self.l-1,self.y+y+2,self.z+z+self.h*3/4,20)
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x,self.y+y+2,self.z+z+self.h/4,20)
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x,self.y+y+2,self.z+z+self.h*3/4,20)
    def buildall(self):
        self.__buildwall()
        self.__buildroof()
        self.__builddoor()
        self.__buildwindows()

    def rebuild_floor(self, floor):
        for x in range(self.l):
            for z in range(self.w):
                if floor[x][z] == '0':
                    cl = 5
                else:
                    cl = 41
                mc.setBlock(self.x + x, self.y - 1, self.z + z, cl)
bases=[[(-26,21,-20),(9,9,9),"cc","You Are Not Alone"],
       [(-13, 21, -20), (9, 9, 9), "dd", "Yesterday once more"],
       [(-0, 21, -20), (9, 9, 9), "ee", "Fairy Tale"]]

houses = []

pos=mc.player.getTilePos()
x0=pos.x
y0=pos.y
z0=pos.z

for base in bases:
    house = House(base[0],46,41,5)
    house.setLWH(base[1])
    house.set_housename(base[2])
    house.add_song(base[3])
    houses.append(house)

for house in houses:
    house.build_all()

f = open("floor.csv", "r")
floor = []
t = f.readlines()
for line in t:
    line = line.strip().split(",")
    floor.append(line)

for house in houses:
    house.rebuild_floor(floor)

while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()
    for base in bases:
        if base[0][0] <= pos.x <= base[0][0] + base[1][0] \
                and base[0][1] <= pos.y <= base[0][1] + base[1][1] and \
                base[0][2] <= pos.z <= base[0][2] + base[1][2]:
            print("Welcome to", base[2])
