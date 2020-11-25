import mcpi.minecraft as minecraft
import time
import mcpi.block as block
import serial
mc = minecraft.Minecraft.create()
                
class House():
        def __init__(self,x,y,z,l,w,h,name):
                self.x=x
                self.y=y
                self.z=z
                self.l=l
                self.w=w
                self.h=h
                self.name=name
                mc.postToChat("hello world. I will build a house named "+ self.name +" at "+str(self.x)+", "+str(self.y)+", "+str(self.z))
                

        def buildfloor(self):
                f = open(r'C:\Users\Caizilin\Desktop\floor.csv', "r")
                floor = []
                t = f.readlines()
                for line in t:
                    line = line.strip().split(",")
                    floor.append(line)

                for a in range(self.l):
                    for c in range(self.w):
                        if floor[a][c] == '0':
                            bl = 5
                        else:
                            bl = 41
                        mc.setBlock(self.x + 1 + a, self.y, self.z + 1+ c, bl)

        def buildwall(self):
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
                self.buildfloor()
                self.buildwall()
                self.buildroof()
                self.builddoor()
                self.buildwindow()
                self.builddecoration()
           


class RoundHouse(House):
    def __init__(self,x,y,z,l,w,h,r,name):
        super(RoundHouse,self).__init__(x,y,z,l,w,h,name)
        self.r=r
        print("i will build a round roof house r is",self.r)
    def buildroof(self):
        XO=self.x+int(self.l/2)
        ZO=self.z+int(self.w/2)
        for ry in range(self.r):
            for rx in range(self.r):
             for rz in range(self.r):
                 rr=rx*rx+rz*rz+ry*ry
                 if rr<=self.r*self.r:
                  mc.setBlock(XO+rx, self.y+self.h-1+ry, ZO-rz-1,45)
                  mc.setBlock(XO+rx, self.y+self.h-1+ry, ZO+rz,45)
                  mc.setBlock(XO-rx-1, self.y+self.h-1+ry, ZO+rz,45)
                  mc.setBlock(XO-rx-1, self.y+self.h-1+ry, ZO-rz-1,45)

                    
    def buildall(self):
        super(RoundHouse,self).buildall()
        self.buildroof()

class TriangleHouse(House):
    def __init__(self,x,y,z,l,w,h,name):
        super(TriangleHouse,self).__init__(x,y,z,l,w,h,name)
    def buildroof(self):
        for c in range(self.w):
            for a in range(self.l):
                mc.setBlock(self.x+1+a, self.y+self.h, self.z+1+c, 45)
        t=0
        while(t<=(self.l/2+1)):
            for c in range(self.w+2-2*t):
                for a in range(self.l+2):
                    mc.setBlock(self.x+a, self.y+self.h+t, self.z+c+t, 45)
            t=t+1


    def buildall(self):
        super(TriangleHouse,self).buildall()
        self.buildroof()

        
for i in range(3):
    house1=House(-46,11,-37-15*i,10,10,5,"czl_house")        
    house1.buildall()

  
for i in range(3):
    house2=RoundHouse(-31,11,-37-15*i,10,10,5,7,"czl_house")        
    house2.buildall()

for i in range(3):
    house3=TriangleHouse(-16,11,-37-15*i,10,10,5,"czl_house")        
    house3.buildall()
