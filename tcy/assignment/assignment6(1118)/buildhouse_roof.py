import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
import cmath

class House():

    def __init__(self,x,y,z,l,w,h,q,u,v):
        self.x=x
        self.y=y
        self.z=z

        self.l=l
        self.w=w
        self.h=h

        self.q=q
        self.u=u
        self.v=v
        print("hello world",self.x,self.y,self.z)

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
    def __buildfloor(self):
        print("i will build 4 line as 4 wall at",self.x,self.y+self.h,self.z)
        for x in range(0,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y,self.z+z,self.v)
                mc.setBlock(self.x+x,self.y,self.z+z+1,self.u)
        for x in range(1,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y,self.z+z,self.u)
                mc.setBlock(self.x+x,self.y,self.z+z+1,self.v)
    def __buildroof(self):      
         for x in range(0,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z,self.v)
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z+1,self.u)
         for x in range(1,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z,self.u)
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z+1,self.v)

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
        self.__buildfloor()
        self.__buildwindows()

class TriangleHouse(House):
    def __buildroof(self):
        midx=self.x+self.l/2
        midz=self.z+self.h/2
        for x in range(0,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y+self.w-1+5-max(abs(midx-x),abs(midz-z)),self.z+z,self.v)
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z+1,self.u)
        for x in range(1,self.l-1,2):
            for z in range(0,self.h-1,2):
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z,self.u)
                mc.setBlock(self.x+x,self.y+self.w-1,self.z+z+1,self.v)
        for y in range(0,self.l/2,1):
            for x in range(self.x+y,self.x+self.l-y,1):
                for z in range(self.z+y,self.z+self.h-y,1):
                    mc.setBlock(x,y,z,self.u)
    def buildhouse(self):
        super(House,self).buildall()
        self.__buildroof()


class RoundHouse(House):
    def __buildroof(self):
        x0=self.x+self.l/2
        z0=self.z+self.h/2
        r=cmath.sqrt((self.h/2)*(self.h/2)+(self.l/2)*(self.l/2))
        for y in range(0,r,1):
            dx=r-cmath.sqrt(r*r-y*y):
            for x in range (x0-r+dx,x0+r-dx,1):
                z=cmath.sqrt(r*r-y*y-x*x)
                mc.setBlock(x,y,z,self.u)
    def buildhouse(self):
        super(House,self).buildall()
        self.__buildroof()

x0=pos.x
y0=pos.y
z0=pos.z

L=7
W=7
H=7

house1=House(x0,y0,z0,L,W,H,46,41,5)
house1.buildall()
