import mcpi.minecraft as minecraft
import mcpi.block as block

mc= minecraft.Minecraft.create()

pos=mc.player.getTilePos()   


class House():
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print("hello world, I will build a house at ",self.x,self.y,self.z)
        self.l=0
        self.w=0
        self.h=0

    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        print("set LWH")
        
    def buildwall_01(self):
        """build the door"""
        for a in range(3):
            mc.setBlock(self.x+1,self.y+a,self.z,5)
            mc.setBlock(self.x+2,self.y+a,self.z,5)
        """build the window"""
        for a in range(1,self.h-1):
            for b in range(4,self.l-1):
                mc.setBlock(self.x+b,self.y+a,self.z,20)
        """build the other part"""
        for a in range(self.h):
            mc.setBlock(self.x,self.y+a,self.z,1)
            mc.setBlock(self.x+3,self.y+a,self.z,1)
            mc.setBlock(self.x+self.l-1,self.y+a,self.z,1)
        for a in range(3,self.h):
            mc.setBlock(self.x+1,self.y+a,self.z,1)
            mc.setBlock(self.x+2,self.y+a,self.z,1)
        for a in range(4,self.l-1):
            mc.setBlock(self.x+a,self.y,self.z,1)
            mc.setBlock(self.x+a,self.y+self.h-1,self.z,1)
        print("build wall_1")

    def buildwall_02(self):
        for a in range(self.w):
            for b in range(self.h):
                mc.setBlock(self.x,self.y+b,self.z+a,1)
        print("build wall_2")

    def buildwall_03(self):
        for a in range(self.w):
            for b in range(self.h):
                mc.setBlock(self.x+self.l-1,self.y+b,self.z+a,1)
        print("build wall_3")

    def buildwall_04(self):
        for a in range(1,self.l-1):
            for b in range(self.h):
                if b==self.h-2:
                    mc.setBlock(self.x+a,self.y+b,self.z+self.w-1,20)
                else:
                    mc.setBlock(self.x+a,self.y+b,self.z+self.w-1,1)
        print("build wall_4")
        
                            
    def buildroof(self):
        for a in range(self.l+2):
            for b in range(self.w+2):
                mc.setBlock(self.x+a-1,self.y+self.h,self.z+b-1,1)
        print("build roof")
        
    def buildall(self):
        self.buildwall_01()
        self.buildwall_02()
        self.buildwall_03()
        self.buildwall_04()
        self.buildroof()
        

house1=House(pos.x,pos.y,pos.z)
house1.setLWH(8,5,6)

house1.buildall()

