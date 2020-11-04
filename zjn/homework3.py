import mcpi
import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import time
# 暂时没有ser=serial.Serial("COM3")

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x0=pos.x
y0=pos.y
z0=pos.z
class House():
    def __init__(self,x,y,z,name):
        self.x=x
        self.y=y
        self.z=z
        self.name=name
        mc.postToChat("This is "+self.name+" house, which lies in "+" x="+str(self.x) +" y="+str(self.y)+" z="+str(self.z)+"  I will sing a song")
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        
    def buildwall(self):
        for y1 in range(self.h):
          for a in range(self.l):
              if y1%2==0 and a%2==1:
                mc.setBlock(self.x+a, self.y+y1, self.z,block.STONE.id)
                mc.setBlock(self.x+a, self.y+y1, self.z+self.w-1,block.STONE.id)
              else:
                mc.setBlock(self.x+a, self.y+y1, self.z,41)
                mc.setBlock(self.x+a, self.y+y1, self.z+self.w-1,41)
          for a in range(self.w-2):
              if y1%2==0 and a%2==1:
                mc.setBlock(self.x, self.y+y1, self.z+1+a,block.STONE.id)
                mc.setBlock(self.x+self.l-1, self.y+y1, self.z+1+a,block.STONE.id)
              else:
                mc.setBlock(self.x, self.y+y1, self.z+1+a,41)
                mc.setBlock(self.x+self.l-1, self.y+y1, self.z+1+a,41)
                 
    def buildroof(self):
        hh=self.h
        ll=self.l
        ww=self.w
        i=0
        while ll>=1 and ww>=1:
            for a in range(ll):
               for a1 in range(ww):
                mc.setBlock(self.x+i+a, self.y+hh-1, self.z+i+a1,57)
            ll=ll-2
            ww=ww-2
            hh=hh+1
            i=i+1
        mc.setBlock(pos.x, pos.y+self.h, pos.z,50)
        mc.setBlock(pos.x+self.l-1, pos.y+self.h, pos.z+self.w-1,50)
        mc.setBlock(pos.x+self.l-1, pos.y+self.h, pos.z,50)
        mc.setBlock(pos.x, pos.y+self.h, pos.z+self.w-1,50)   
    def builddoor(self):
         mc.setBlock(self.x+round(self.l/2), self.y+1, self.z,0)
         mc.setBlock(self.x+round(self.l/2), self.y+2, self.z,0)
    def buildwindow(self):
        for z1 in range(2):
         for y1 in range(2):
          mc.setBlock(self.x+self.l-1, self.y+y1+3, self.z+z1+round(self.w/2)-1, 20)
    def buildbottom(self):
          for a in range(self.l+2):
           for a1 in range(self.w+2):
            mc.setBlock(pos.x+a-1, pos.y, pos.z-1+a1,block.WOOL.id)
          mc.setBlock(pos.x-1, pos.y+1, pos.z-1,50)
          mc.setBlock(pos.x+self.l, pos.y+1, pos.z+self.w,50)
          mc.setBlock(pos.x-1, pos.y+1, pos.z+self.w,50)
          mc.setBlock(pos.x+self.l, pos.y+1, pos.z-1,50)
    def designpattern(self):
        p=open(r'C:\Users\HP\desktop\ss.csv',"r")
        pattern=[]
        p=p.readlines()
        for line in p:
            line=line.strip().split(",")
            pattern.append(line)
        for a in range(self.l):
           for a1 in range(self.w):
             if pattern[a][a1]=="0":
                 x=5
             else:
                 x=41
             mc.setBlock(pos.x+a, pos.y, pos.z+a1,x)    
##
    def songs(self):
                t=open(r'C:\Users\HP\desktop\song.csv',"r")
                song=[]
                t=t.readlines()
                for line in t:
                    line=line.strip().split(",")
                    song.append(line)
                for i in range(len(song)):
                 b=song[i]
                 ser.write(b.encode())
                 time.sleep(1)
##
    def buildall(self):
        self.buildwall()
        self.buildroof()
        self.builddoor()
        self.buildwindow()
        self.buildbottom()
        self.designpattern()
        #self.songs()
house1=House(x0,y0,z0,"zjn")
house1.setLWH(10,10,10)
house1.buildall()

