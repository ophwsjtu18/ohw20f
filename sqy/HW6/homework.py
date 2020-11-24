import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))

class House():
    def __init__(self,x,y,z,L,W,H):
        self.x=x
        self.y=y
        self.z=z
        self.L=L
        self.W=W
        self.H=H
        print("I will build a house on",self.x,self.y,self.z,self.L,self.W,self.H)
    def __buildwall__(self):
        print("build wall",self.L,self.W,self.H)
        for c in range(self.H):
            for a in range(self.L):
                mc.setBlock(self.x+a,self.y+c,self.z,5)
                mc.setBlock(self.x+a,self.y+c,self.z+self.W-1,5)
            for b in range(self.W-2):
                mc.setBlock(self.x,self.y+c,self.z+1+b,5)
                mc.setBlock(self.x+self.L-1,self.y+c,self.z+1+b,5)
        print("done")
    def __buildroof(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y+self.H-1,self.z+b,5)
        print("done")
    def __builddoor(self):
        mc.setBlock(self.x+self.L/2,self.y+1,self.z,0)
        mc.setBlock(self.x+self.L/2,self.y+2,self.z,0)
        print("done")
    def __buildwindows(self):
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+self.L-1,self.y+y+2,self.z+z+4,20)
        print("done")
    def __buildground(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y,self.z+b,5)
        print("done")
    def buildall(self):
        self.__buildwall__()
        self.__buildroof()
        self.__builddoor()
        self.__buildwindows()
        self.__buildground()

house1=House(190,90,250,8,8,8)
house1.buildall()

class RoundHouse(House):
    def __init__(self,x,y,z,L,W,H,R):
        super(RoundHouse,self).__init__(x,y,z,L,W,H)
        self.R=R
        print("i will build a round roof house r is",self.R)
    def __buildroof(self):
        print("build a round roof")
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y+self.H-1,self.z+b,5)
        for a in range(self.L-2):
            mc.setBlock(self.x+1+a,self.y+self.H-1,self.z-1,5)
            mc.setBlock(self.x+1+a,self.y+self.H-1,self.z+self.W,5)
            mc.setBlock(self.x-1,self.y+self.H-1,self.z+1+a,5)
            mc.setBlock(self.x+self.L,self.y+self.H-1,self.z+1+a,5)
        for a in range(self.L-4):
            mc.setBlock(self.x+2+a,self.y+self.H-1,self.z-2,5)
            mc.setBlock(self.x+2+a,self.y+self.H-1,self.z+self.W+1,5)
            mc.setBlock(self.x-2,self.y+self.H-1,self.z+2+a,5)
            mc.setBlock(self.x+self.L+1,self.y+self.H-1,self.z+2+a,5)
        for a in range(self.L-4):
            mc.setBlock(self.x+3+a,self.y+self.H-1,self.z-3,5)
            mc.setBlock(self.x+3+a,self.y+self.H-1,self.z+self.W+2,5)
            mc.setBlock(self.x-3,self.y+self.H-1,self.z+3+a,5)
            mc.setBlock(self.x+self.L+2,self.y+self.H-1,self.z+3+a,5)
    def buildall(self):
        super(RoundHouse,self).__buildwall__()
        self.__buildroof()

        

house2=RoundHouse(210,90,250,8,8,8,8)
house2.buildall()

class TRIHouse(House):
    def __init__(self,x,y,z,L,W,H,R):
        super(TRIHouse,self).__init__(x,y,z,L,W,H)
        self.R=R
        print("i will build a round roof house r is",self.R)
    def __buildroof(self):
        print("build a round roof")
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y+self.H-1,self.z+b,5)
        for a in range(self.L-2):
            mc.setBlock(self.x+1+a,self.y+self.H-1,self.z-1,5)
            mc.setBlock(self.x+1+a,self.y+self.H-1,self.z+self.W,5)
            mc.setBlock(self.x-1,self.y+self.H-1,self.z+1+a,5)
            mc.setBlock(self.x+self.L,self.y+self.H-1,self.z+1+a,5)
        for a in range(self.L-4):
            mc.setBlock(self.x+2+a,self.y+self.H-1,self.z-2,5)
            mc.setBlock(self.x+2+a,self.y+self.H-1,self.z+self.W+1,5)
            mc.setBlock(self.x-2,self.y+self.H-1,self.z+2+a,5)
            mc.setBlock(self.x+self.L+1,self.y+self.H-1,self.z+2+a,5)
        for a in range(self.L-6):
            mc.setBlock(self.x+3+a,self.y+self.H-1,self.z-3,5)
            mc.setBlock(self.x+3+a,self.y+self.H-1,self.z+self.W+2,5)
            mc.setBlock(self.x-3,self.y+self.H-1,self.z+3+a,5)
            mc.setBlock(self.x+self.L+2,self.y+self.H-1,self.z+3+a,5)
    def buildall(self):
        super(TRIHouse,self).__buildwall__()

        self.__buildroof()

        

house2=RoundHouse(230,90,250,8,8,8,8)
house2.buildall()
