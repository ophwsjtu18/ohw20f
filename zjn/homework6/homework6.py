import mcpi
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x0=pos.x+1
y0=pos.y+1
z0=pos.z+1

class House():
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        mc.postToChat("I will build house at "+" x="+str(self.x) +" y="+str(self.y)+" z="+str(self.z))
    def buildwindow(self):
        for z1 in range(2):
         for y1 in range(2):
          mc.setBlock(self.x+self.l-1, self.y+y1+3, self.z+z1+round(self.w/2)-1, 20)
    def buildbottom(self):
          for a in range(self.l+2):
           for a1 in range(self.w+2):
            mc.setBlock(self.x-1+a, self.y,self.z-1+a1,block.WOOL.id)
          mc.setBlock(self.x-1, self.y+1, self.z-1,50)
          mc.setBlock(self.x+self.l, self.y+1, self.z+self.w,50)
          mc.setBlock(self.x-1, self.y+1, self.z+self.w,50)
          mc.setBlock(self.x+self.l, self.y+1, self.z-1,50)
    def buildwall(self):
      for y in range(self.h):
       for a in range(self.l):
         mc.setBlock(self.x+a, self.y+y, self.z,block.STONE.id)
         mc.setBlock(self.x+a, self.y+y, self.z+self.w-1,block.STONE.id)
       for a in range(self.w-2):
         mc.setBlock(self.x, self.y+y, self.z+1+a,block.STONE.id)
         mc.setBlock(self.x+self.l-1, self.y+y, self.z+1+a,block.STONE.id)
    def builddoor(self):
         mc.setBlock(self.x+round(self.l/2), self.y+1, self.z,0)
         mc.setBlock(self.x+round(self.l/2), self.y+2, self.z,0)
    def buildroof(self):
        for x in range(self.l+2):
          for z in range(self.w+2):
              mc.setBlock(self.x-1+x, self.y+self.h-1, self.z-1+z,57)
    def buildall(self):
        self.buildwall()
        self.buildroof()
        self.builddoor()
        self.buildwindow()
        self.buildbottom()
        



class TriangleHouse(House):
    def __init__(self,x,y,z,l,w,h,roofl,roofw):
        super(TriangleHouse,self).__init__(x,y,z,l,w,h)
        self.roofl=roofl
        self.roofw=roofw
        mc.postToChat("i will build a triangle roof house at"+" x="+str(self.x) +" y="+str(self.y)+" z="+str(self.z))
    def buildroof(self):
        
        hh=self.h
        ll=self.roofl
        ww=self.roofw
        addl=(self.roofl-self.l)/2
        addw=(self.roofw-self.w)/2
        i=0
        while ll>=1 and ww>=1:
            for a in range(ll):
               for a1 in range(ww):
                mc.setBlock(self.x+i+a-addl, self.y+hh-1, self.z+i+a1-addw,57)
            ll=ll-2
            ww=ww-2
            hh=hh+1
            i=i+1
    def buildall(self):
        self.buildwall()
        self.buildroof()
        self.builddoor()
        self.buildwindow()
        self.buildbottom()



class RoundHouse(House):
    def __init__(self,x,y,z,l,w,h,r):
        super(RoundHouse,self).__init__(x,y,z,l,w,h)
        self.r=r
        mc.postToChat("i will build a Roundroof house at"+" x="+str(self.x) +" y="+str(self.y)+" z="+str(self.z))
    def buildroof(self):
        R=round(self.r)
        X=self.x+round(self.l/2)
        Z=self.z+round(self.w/2)
        for ay in range(R):
            for ax in range(R):
             for az in range(R):
                 ar=ax*ax+az*az+ay*ay
                 if ar<=R*R:
                  mc.setBlock(X+ax, self.y+self.h-1+ay, Z-az-1,41)
                  mc.setBlock(X+ax, self.y+self.h-1+ay, Z+az,41)
                  mc.setBlock(X-ax-1, self.y+self.h-1+ay, Z+az,41)
                  mc.setBlock(X-ax-1, self.y+self.h-1+ay, Z-az-1,41)
    def buildall(self):
        super(RoundHouse, self).buildall()
        self.buildroof()



for i in range(3):
    house3=TriangleHouse(x0+20,y0,z0+20*i,10,10,10,12,12)
    house3.buildall()
for i in range(3):
    house3=RoundHouse(x0+40,y0,z0+20*i,10,10,10,10)
    house3.buildall()
for i in range(3):
    house3=House(x0+60,y0,z0+20*i,10,10,10)
    house3.buildall()















        
