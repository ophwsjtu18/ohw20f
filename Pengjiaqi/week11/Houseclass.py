import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
elem=5

class House():
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        print("I will build a house on",self.x,self.y,self.z,self.l,self.w,self.h)
        
    def __buildwall__(self):
        print("build wall",self.l,self.w,self.h)
        for y in range(self.h):
            for a in range(self.l):
                mc.setBlock(self.x+a, self.y+y, self.z,elem)
                mc.setBlock(self.x+a, self.y+y, self.z+self.w-1,elem)
            for a in range(self.w):
                mc.setBlock(self.x, self.y+y, self.z+a,elem)
                mc.setBlock(self.x+self.l-1, self.y+y, self.z+a,elem)
        #地板
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x+x, self.y, self.z+z,elem)
                mc.setBlock(self.x+x, self.y, self.z+z,elem)
        
        #地基
        for x in range(self.l+2):
            mc.setBlock(self.x-1+x, self.y, self.z-1,4)
            mc.setBlock(self.x-1+x, self.y, self.z+self.w,4)
        for z in range(self.w+2):
            mc.setBlock(self.x-1, self.y, self.z-1+z,4)
            mc.setBlock(self.x+self.l, self.y, self.z-1+z,4)
        
        
    def __buildroof(self):
        print("build a rectangel roof")
        
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x+x, self.y+self.h-1, self.z+z,elem)
##                mc.setBlock(self.x+x, self.y, self.z+z,elem)
        
        
    def buildDoorAndWindow(self):
        if self.h<4 or self.l<4 or self.w<4:
            print("The House is too small!")
            return
        print("build a Door And a Window")
        mc.setBlock(self.x+self.l//2, self.y+1, self.z,64)
        mc.setBlock(self.x+self.l//2, self.y+2, self.z,64)

        mc.setBlock(self.x+self.l//2-1, self.y+1, self.z-1,38)
        mc.setBlock(self.x+self.l//2+1, self.y+1, self.z-1,38)
        
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x, self.y+y+2, self.z+z+self.w//2-1, 20)
                mc.setBlock(self.x+self.l-1, self.y+y+2, self.z+z+self.w//2-1, 20)
    
        
    def buildall(self):
        self.__buildwall__()
        self.__buildroof()
        self.buildDoorAndWindow()

        for y in range(self.h):
            mc.setBlock(self.x,self.y+y,self.z,17)
            mc.setBlock(self.x+self.l-1,self.y+y,self.z,17)
            mc.setBlock(self.x,self.y+y,self.z+self.w-1,17)
            mc.setBlock(self.x+self.l-1,self.y+y,self.z+self.w-1,17)
            
        for x in range(self.l+2):
            mc.setBlock(self.x-1+x, self.y+self.h-1, self.z-1,5)
            mc.setBlock(self.x-1+x, self.y+self.h-1, self.z+self.w,5)
        for z in range(self.w+2):
            mc.setBlock(self.x-1, self.y+self.h-1, self.z-1+z,5)
            mc.setBlock(self.x+self.l, self.y+self.h-1, self.z-1+z,5)
            
        for x in range(self.l):
            mc.setBlock(self.x+x, self.y+self.h, self.z,5)
            mc.setBlock(self.x+x, self.y+self.h, self.z+self.w-1,5)
        for z in range(self.w):
            mc.setBlock(self.x, self.y+self.h, self.z+z,5)
            mc.setBlock(self.x+self.l-1, self.y+self.h, self.z+z,5)
        
        for x in range(self.l-2):
            for z in range(self.w-2):
                mc.setBlock(self.x+1+x, self.y+self.h+1, self.z+1+z,5)

        mc.setBlock(self.x+self.l//2, self.y, self.z-1,44)

        

#house1=House(pos.x,pos.y,pos.z,10,10,10)
#house1.buildall()

class RoundHouse(House):
    def __init__(self,x,y,z,l,w,h,r):
        super(RoundHouse,self).__init__(x,y,z,l,w,h)
        self.r=r
        print("i will build a round roof house r is",self.r)
    def __buildroof(self):
        print("build a round roof")
##        l=self.l
##        w=self.w
##        h=self.h
##        r=int((l*l+w*w)**0.5//2)+1
        r=self.r
        mdx=self.x+self.l//2-1
        mdz=self.z+self.w//2-1
        mdy=self.y+self.h
        for x in range(-r-1,r+1):
            for y in range(0,r+1):
                for z in range(-r-1,r+1):
                    if (x*x+y*y+z*z)<=r*r:
                        mc.setBlock(mdx+x, mdy+y, mdz+z,4)
                    
        
    def buildall(self):
        super(RoundHouse,self).__buildwall__()
        self.__buildwall__()
        self.__buildroof()
        self.buildDoorAndWindow()

#house2=RoundHouse(pos.x,pos.y,pos.z,10,10,10,8)
#house2.buildall()

class TriangleHouse(House):
    def __init__(self,x,y,z,l,w,h,r):
        super(TriangleHouse,self).__init__(x,y,z,l,w,h)
        self.r=r
        print("i will build a Triangle roof house")
    def __buildroof(self):
        print("build a Triangle roof")
        if self.w!=self.l:
            return
        '''
        r=self.r
        mdx=self.x+self.l//2-1
        mdz=self.z+self.w//2-1
        mdy=self.y+self.h
        for y in range(r//2):
            for x in range(-self.l+2*y,self.l-2*y):
                mc.setBlock(mdx+x, mdy+y, mdz-self.w//2+2*y,5)
                mc.setBlock(mdx+x, mdy+y, mdz+self.w//2-2*y,5)
            for z in range(-self.w-2*y,self.w+2*y):
                mc.setBlock(mdx+self.w//2-2*y, mdy+y, mdz+z,5)
                mc.setBlock(mdx-self.w//2+2*y, mdy+y, mdz+z,5)
        '''
        
        for x in range(self.l+2):
            mc.setBlock(self.x-1+x, self.y+self.h-1, self.z-1,5)
            mc.setBlock(self.x-1+x, self.y+self.h-1, self.z+self.w,5)
        for z in range(self.w+2):
            mc.setBlock(self.x-1, self.y+self.h-1, self.z-1+z,5)
            mc.setBlock(self.x+self.l, self.y+self.h-1, self.z-1+z,5)


        for y in range(self.l//2):
            for x in range(self.l-2*y):
                mc.setBlock(self.x+y+x, self.y+y+self.h, self.z+y,5)
                mc.setBlock(self.x+y+x, self.y+y+self.h, self.z+y+self.w-1-2*y,5)
            for z in range(self.w-2*y):
                mc.setBlock(self.x+y, self.y+y+self.h, self.z+y+z,5)
                mc.setBlock(self.x+y+self.l-1-2*y, self.y+y+self.h, self.z+y+z,5)

        
        '''
        for x in range(self.l):
            mc.setBlock(self.x+x, self.y+self.h, self.z,5)
            mc.setBlock(self.x+x, self.y+self.h, self.z+self.w-1,5)
        for z in range(self.w):
            mc.setBlock(self.x, self.y+self.h, self.z+z,5)
            mc.setBlock(self.x+self.l-1, self.y+self.h, self.z+z,5)
        '''            

    def buildall(self):
        self.__buildwall__()
        self.__buildroof()
        self.buildDoorAndWindow()

#house2=TriangleHouse(pos.x,pos.y,pos.z,10,10,10,20)
#house2.buildall()

for x in range(3):
    house1=House(pos.x+20*x,pos.y,pos.z,10,10,5)
    house1.buildall()

for x in range(3):
    house1=TriangleHouse(pos.x+20*x,pos.y,pos.z+40,10,10,5,8)
    house1.buildall()

for x in range(3):
    house1=RoundHouse(pos.x+20*x,pos.y,pos.z+20,10,10,5,8)
    house1.buildall()
