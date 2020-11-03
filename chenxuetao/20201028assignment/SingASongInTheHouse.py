from mcpi.minecraft import Minecraft
import csv
import time
import serial

ser=serial.Serial("COM4")

song1=["1","1","5","5","6","6","5","4","4","3","3","2","2","1"]


class House:
    posx = 0
    posy = 0
    posz = 0
    name = None
    def __init__(self, x, y, z):
        House.posx = x
        House.posy = y
        House.posz = z
    
    def wall(self):
        for tall in range(-4,10):
            for i in range(0,21):
                mc.setBlock(self.posx+i-10,self.posy+tall,self.posz+10,42)
                mc.setBlock(self.posx+i-10,self.posy+tall,self.posz-10,42)
                mc.setBlock(self.posx+10,self.posy+tall,self.posz+i-10,42)
                mc.setBlock(self.posx-10,self.posy+tall,self.posz+i-10,42)
    def roof(self):
        tall_most = 10
        for i in range(0,21):
            for j in range(0,21):
                mc.setBlock(self.posx+i-10,self.posy+10,self.posz+j-10,95)
    def window(self):
        for i in range(2,5):
            for j in range(0,10):
                mc.setBlock(self.posx+10,self.posy+i,self.posz+j-5,20)
    def door(self):
        mc.setBlock(self.posx-10,self.posy,self.posz+1,0)
        mc.setBlock(self.posx-10,self.posy,self.posz,0)
        mc.setBlock(self.posx-10,self.posy+1,self.posz+1,0)
        mc.setBlock(self.posx-10,self.posy+1,self.posz,0)
        
    def create_all(self):
        self.wall()
        self.roof()
        self.window()
        self.door()

    def set_name(self,name):
        print("set the name of the house:",name)
        self.name = name

    def song(self):
        time.sleep(2)
        for i in song1:
            ser.write(i.encode())
            time.sleep(1)

    def detect_pos(self,currx,curry,currz):
        if(self.posx-10<=currx<=self.posx+10 and self.posz-10<=currz<=self.posz+10):
            self.set_name("a simple house")
            self.song()
            
        
mc=Minecraft.create()

pos=mc.player.getTilePos()

t = House(pos.x,pos.y,pos.z)

t.create_all()

while True:
    pos=mc.player.getTilePos()
    t.detect_pos(pos.x,pos.y,pos.z)
