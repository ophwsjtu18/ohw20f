import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
class house():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print("hello world. I will build the house at",self.x,self.y,self.z)
        
    def buildfloor(self,length,width,block1):
        self.length=length
        self.width=width
        self.block1=block1
        for x in range(self.length):
            for z in range(self.width):
                mc.setBlock(self.x+x+1,self.y,self.z+z+1,self.block1)
        print("I will build the floor at",self.x,self.y,self.z)
                
    def buildwall(self,high,block2):
        self.high=high
        self.block2=block2
        for x in range(self.length):
            for y in range(self.high):
                mc.setBlock(self.x+x+1,self.y+1+y,self.z+1,self.block2)
        for z in range(self.width):
            for y in range(self.high):
                mc.setBlock(self.x+1,self.y+1+y,self.z+z+1,self.block2)
        for x in range(self.length):
            for y in range(self.high):
                mc.setBlock(self.x+x+1,self.y+1+y,self.z+self.width,self.block2)
        for z in range(self.width):
            for y in range(self.high):
                mc.setBlock(self.x+self.length,self.y+1+y,self.z+z+1,self.block2)
        print("I will build 4 line as 4 wall at",self.x,self.y,self.z)
    def builddoor(self,width2,high2):
        self.width2=width2
        self.high2=high2
        for x in range(self.width2):
            for y in range(self.high2):
                mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y+y+1,self.z+1,0)
        for x in range(self.width2):
            mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y,self.z,126)
        
    def buildwindow(self):
        if(self.length>10):
            for x in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length/4+x,self.y+self.high/2+y,self.z+1,0)
            for x in range(2):
                for y in range(2):
                    mc.setBlock(self.x+3*self.length/4+x+1,self.y+self.high/2+y,self.z+1,0)
            for z in range(2):
                for  y in range(2):
                    mc.setBlock(self.x+1,self.y+self.high/2+y,self.z+self.width/2+z,0)
            for z in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length,self.y+self.high/2+y,self.z+self.width/2+z,0)
        if(self.length<=10):
            mc.setBlock(self.x+(self.length-self.width2)/2-2,self.y+self.high/2,self.z+1,0)
            mc.setBlock(self.x+(self.length+self.width2)/2+2,self.y+self.high/2,self.z+1,0)
            for z in range(2):
                for  y in range(2):
                    mc.setBlock(self.x+1,self.y+self.high/2+y,self.z+self.width/2+z,0)
            for z in range(2):
                for y in range(2):
                    mc.setBlock(self.x+self.length,self.y+self.high/2+y,self.z+self.width/2+z,0)
    def buildroof(self):
        for x in range(self.length+2):
            for z in range(self.width+2):
                mc.setBlock(self.x+x,self.y+self.high,self.z+z,5)
        
    def buildall(self):
        self.buildfloor(10,10,5)
        self.buildwall(6,5)
        self.builddoor(2,2)
        self.buildwindow()
        self.buildroof()

        
class trianglehouse(house):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        print("i will build a triangle house ")
    def __buildroof(self):
        self.length2=self.length/2+2
        for x in range(1,int(self.length2)-1,2):
            for z in range(self.width):
                mc.setBlock(self.x+x,self.y+self.high+(x+1)/2,self.z+z+1,126)
        for x in range(1,int(self.length2)-1,2):
            for z in range(self.width):
                mc.setBlock(self.x+self.length+1-x,self.y+self.high+(x+1)/2,self.z+z+1,126)
        for x in range(0,int(self.length2),2):
            for z in range(self.width):
                mc.setBlock(self.x+x,self.y+self.high+x/2,self.z+z+1,5)
        for x in range(0,int(self.length2),2):
            for z in range(self.width):
                mc.setBlock(self.x+self.length+1-x,self.y+self.high+x/2,self.z+z+1,5)
        for x in range(self.length-4):
            mc.setBlock(self.x+3+x,self.y+self.high+1,self.z+1,5)
        for x in range(self.length-4):
            mc.setBlock(self.x+3+x,self.y+self.high+1,self.z+self.width,5)
        for x in range(self.length+2):
            mc.setBlock(self.x+x,self.y+self.high,self.z,5)
        for x in range(self.length+2):
            mc.setBlock(self.x+x,self.y+self.high,self.z+self.width+1,5)
        for x in range(self.width2):
            mc.setBlock(self.x+1+(self.length-self.width2)/2+x,self.y+self.high2+1,self.z,126)
    def buildall(self):
        self.buildfloor(10,10,5)
        self.buildwall(6,5)
        self.builddoor(2,2)
        self.buildwindow()
        self.__buildroof()

class roundhouse(house):
    def __init__(self,x,y,z,r):
        super().__init__(x,y,z)
        self.r=r
        print("i will build a round roof house r is",self.r)
    def __buildroof(self):
        for x in range(self.length-2):
            mc.setBlock(self.x+2+x,self.y+self.high,self.z,251)
            mc.setBlock(self.x+2+x,self.y+self.high,self.z+self.width+1,251)
        for x in range(self.length-6):
            mc.setBlock(self.x+4+x,self.y+self.high,self.z-1,251)
            mc.setBlock(self.x+4+x,self.y+self.high,self.z+self.width+2,251)
        for z in range(self.width-2):
            mc.setBlock(self.x,self.y+self.high,self.z+2+z,251)
            mc.setBlock(self.x+self.length+1,self.y+self.high,self.z+2+z,251)
        for z in range(self.width-6):
            mc.setBlock(self.x-1,self.y+self.high,self.z+4+z,251)
            mc.setBlock(self.x+self.length+2,self.y+self.high,self.z+4+z,251)
        for z in range(4):
            for x in range(self.width-4+2*z):
                mc.setBlock(self.x+3+x-z,self.y+self.high+1,self.z+z,251)
                mc.setBlock(self.x+3+x-z,self.y+self.high+1,self.z+self.width+1-z,251)
        for z in range(self.width-6):
            for x in range(self.length+2):
                mc.setBlock(self.x+x,self.y+self.high+1,self.z+4+z,251)
        for z in range(2):
            for x in range(2+4*z):
                mc.setBlock(self.x+5+x-2*z,self.y+self.high+2,self.z+z,251)
                mc.setBlock(self.x+5+x-2*z,self.y+self.high+2,self.z-z+self.width+1,251)
        for z in range(2):
            for x in range(self.length-2+2*z):
                mc.setBlock(self.x+2+x-z,self.y+self.high+2,self.z+z+2,251)
                mc.setBlock(self.x+2+x-z,self.y+self.high+2,self.z+self.width-z-1,251)
        for z in range(self.width-6):
            for x in range(self.length+2):
                mc.setBlock(self.x+x,self.y+self.high+2,self.z+4+z,251)
        for z in range(2):
            for x in range(self.length-6+2*z):
                mc.setBlock(self.x+4+x-z,self.y+self.high+3,self.z+z+1,251)
                mc.setBlock(self.x+4+x-z,self.y+self.high+3,self.z+self.width-z,251)
        for x in range(2):
            for z in range(self.width-6+4*x):
                mc.setBlock(self.x+1+x,self.y+self.high+3,self.z+4-2*x+z,251)
                mc.setBlock(self.x+self.length-x,self.y+self.high+3,self.z+4-2*x+z,251)
        for y in range(2):
            for x in range(6-2*y):
                for z in range(6-2*y):
                    mc.setBlock(self.x+3+x+y,self.high+self.y+4+y,self.z+3+z+y,251)

    def buildall(self):
        self.buildfloor(10,10,5)
        self.buildwall(6,5)
        self.builddoor(2,2)
        self.buildwindow()
        self.__buildroof()
        

for x in range(3):
        house1=roundhouse(pos.x+1,pos.y,pos.z+18*x+1,7)
        house1.buildall()
for x in range(3):
        house1=trianglehouse(pos.x+19,pos.y,pos.z+18*x+1)
        house1.buildall()
for x in range(3):
        house1=house(pos.x+37,pos.y,pos.z+18*x+1)
        house1.buildall()
