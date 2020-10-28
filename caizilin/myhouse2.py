import mcpi.minecraft as minecraft
import time
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House():
        def __init__(self,x,y,z):
                self.x=x
                self.y=y
                self.z=z
                mc.postToChat("hello world. I will build a house at "+str(self.x)+", "+str(self.y)+", "+str(self.z))
        def setLWH(self,l,w,h):
                self.l=l
                self.w=w
                self.h=h
        def buildground(self):
                mc.postToChat("hello world. I will build 1 layer of blocks as the ground at "+str(self.x)+", "+str(self.y)+", "+str(self.z))
                for c in range(self.w):
                    for a in range(self.l):
                        mc.setBlock(self.x+1+a, self.y, self.z+1+c, 45)
        def buildwall(self):
                mc.postToChat("hello world. I will build 4 lines as 4 walls at "+str(self.x)+", "+str(self.y)+", "+str(self.z))
                for b in range(self.h):
                    for a in range(self.l):
                        mc.setBlock(self.x+1+a, self.y+1+b, self.z+1, 45)
                        mc.setBlock(self.x+1+a, self.y+1+b, self.z+self.w, 45)

                for b in range(self.h):
                    for c in range(self.w):
                        mc.setBlock(self.x+1, self.y+1+b, self.z+1+c, 45)
                        mc.setBlock(self.x+self.l, self.y+1+b, self.z+1+c, 45)
        def buildroof(self):
                for c in range(self.w):
                    for a in range(self.l):
                        mc.setBlock(self.x+1+a, self.y+self.h, self.z+1+c, 45)
                t=0
                while(t<=min((self.l/2+1),(self.w/2+1))):
                    for c in range(self.w+2-2*t):
                        for a in range(self.l+2-2*t):
                            mc.setBlock(self.x+a+t, self.y+self.h+t, self.z+c+t, 45)
                    t=t+1
                    
        def builddoor(self):
            for b in range(2):
                 mc.setBlock(self.x+3, self.y+1+b, self.z+1,0)
            
        def buildwindow(self):
            for b in range(2):
                for c in range(2):
                    mc.setBlock(self.x+1,self.y+2+b,self.z+3+c,20)
        def builddecoration(self):
            mc.setBlock(self.x+3, self.y+3, self.z, 45)
            mc.setBlock(self.x+3, self.y+4, self.z, 50)
            mc.setBlock(self.x+3, self.y, self.z, 53)
            for c in range(2):
                mc.setBlock(self.x,self.y+1,self.z+3+c,3)
                mc.setBlock(self.x,self.y+2,self.z+3+c,140)
                mc.setBlock(self.x,self.y+2,self.z+3+c,175)
        def buildall(self):
                self.buildground()
                self.buildwall()
                self.buildroof()
                self.builddoor()
                self.buildwindow()
                self.builddecoration()

                
house1=House(-46,11,-37)


house1.setLWH(10,10,5)



house1.buildall()

