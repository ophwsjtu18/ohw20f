import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))

class House():
    def __init__(self,x_,y_,z_,L,W,H):
        self.x=x_
        self.y=y_
        self.z=z_
        self.L=L
        self.W=W
        self.H=H
    def buildground(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y,self.z+b,5)
        print("done")
    def buildwall(self):
        for c in range(self.H):
            for a in range(self.L):
                mc.setBlock(self.x+a,self.y+c,self.z,5)
                mc.setBlock(self.x+a,self.y+c,self.z+self.W-1,5)
            for b in range(self.W-2):
                mc.setBlock(self.x,self.y+c,self.z+1+b,5)
                mc.setBlock(self.x+self.L-1,self.y+c,self.z+1+b,5)
        print("done")
    def buildroof(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y+self.H-1,self.z+b,5)
        print("done")
    def builddoor(self):
        mc.setBlock(self.x+self.L/2,self.y+1,self.z,0)
        mc.setBlock(self.x+self.L/2,self.y+2,self.z,0)
        print("done")
    def buildwindows(self):
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+self.L-1,self.y+y+2,self.z+z+4,20)
        print("done")
    def buildall(self):
        self.buildground()
        self.buildroof()
        self.buildwall()
        self.buildwindows()
        self.builddoor()

house1=House(130,50,210,10,10,10)
house1.buildall()
house2=House(150,50,230,10,10,10)
house2.buildall()
house3=House(170,50,250,10,10,10)
house3.buildall()
