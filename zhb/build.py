import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
import time

class house():
    def __init__(self,data):
        self.data = data
    def base(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        length=self.data[3]
        width=self.data[4]
        height=self.data[5]
            
        for x in range(length):
            for z in range(width):
                mc.setBlock(x0+x,y0,z0+z,17)
                    
    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        length=self.data[3]
        width=self.data[4]
        height=self.data[5]

        for x in range(length):
            for z in range(width):
                for y in range(height):
                    mc.setBlock(x0+x,y0+y,z0+z,5)
        for x in range(length-2):
            for z in range(width-2):
                for y in range(height-1):
                    mc.setBlock(x0+x+1,y0+y+1,z0+z+1,0)

    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        length=self.data[3]
        width=self.data[4]
        height=self.data[5]
        while(length>0 and width>0):
             
            for x in range(length):
                for z in range(width):
                    mc.setBlock(x0+x,y0+height,z0+z,17)
            length=length-1
            width=width-1
            y0=y0+1

    def doorAndWindows(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        length=self.data[3]
        width=self.data[4]
        height=self.data[5]

        for x in range(1):
            for y in range(2):
                mc.setBlock(x0+1+x,y0+1+y,z0,0)
        for x in range(2):
            for y in range(2):
                mc.setBlock(x0+5+x,y0+3+y,z0,20)

    def buildAll(self):
        base()
        wall()
        roof()
        doorAndWindows()


mh=house([-914,1,-476,10,8,6])
mh.base()
mh.wall()
mh.doorAndWindows()
mh.roof()
while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.postToChat("x="+str(pos.x)+"y"+str(pos.y)+"z"+str(pos.z))
        
