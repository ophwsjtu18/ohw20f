import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()

class House():

    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z

        self.l=l
        self.w=w
        self.h=h
        print("hello world",self.x,self.y,self.z)

    def __buildwall(self):
        print("I will build wall",self.x,self.y,self.z)
        for y  in range(self.w):
            for x in range (self.l):
                mc.setBlock(self.x+x,self.y+y,self.z,3)
                mc.setBlock(self.x+x,self.y+y,self.z+self.h-1,3)
        for y in range(self.w):
            for a in range(self.h-2):
                mc.setBlock(self.x,self.y+y,self.z+1+a,3)
                mc.setBlock(self.x+self.l-1,self.y+y,self.z+1+a,3)
    def __buildroof(self):
        print("i will build 4 line as 4 wall at",self.x,self.y+self.h,self.z)
        for x in range(self.l):
            for z in range(self.h):
                mc.setBlock(self.x+x,self.y,self.z+z,2)
        for x in range(self.l):
            for z in range(self.h):
               mc.setBlock(self.x+x,self.y+self.w-1,self.z+z,2)

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
    def buildall(self):
        self.__buildwall()
        self.__buildroof()
        self.__builddoor()
        self.__buildwindows()


pos=mc.player.getTilePos()
 

L=12
W=8
H=20

house1=House(x0,y0,z0,L,W,H)

house1.buildall()
