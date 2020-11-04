from mcpi.minecraft import Minecraft
import csv
import time
import serial

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

    def detect_pos(self,currx,curry,currz):
        if self.posx-10<=currx<=self.posx+10 and self.posz-10<=currz<=self.posz+10:
            self.set_name("qxh")
            self.song()

    def build_the_floor(self):
        with open('floor.csv', newline='') as f:
            reader = csv.reader(f, delimiter='\t')
            j = 0
            for row in reader:
                for i in range(0,19):
                    if row[i]=='1':
                        mc.setBlock(self.posx-9+i,self.posy-1,self.posz-9+j,41)
                    elif row[i]=='0':
                        mc.setBlock(self.posx-9+i,self.posy-1,self.posz-9+j,5)
                j = j + 1
        
        
mc=Minecraft.create()

pos=mc.player.getTilePos()

t = House(pos.x,pos.y,pos.z)

t.create_all()

t.build_the_floor()
