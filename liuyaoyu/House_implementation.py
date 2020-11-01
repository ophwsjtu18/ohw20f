import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

class House:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        mc.postToChat("A house will be build at"+"x="+str(self.x)+" y="+str(self.y)+" z="+str(self.z))
        self.__setName__()
        self.__setSong__()
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    
    def __setName__(self):
        self.name = input("Please name the house: ")

    def __setSong__(self):
        self.song = input("Please give it a song: ")

    def build_three_walls(self):
        for x in range(self.l):
            for y in range(self.h):
                mc.setBlock(self.x+x,self.y+y,self.z,1)
        for z in range(self.w):
            for y in range(self.h):
                mc.setBlock(self.x+self.l,self.y+y,self.z+z,1)
        for x in range(self.l):
            for y in range(self.h):
                mc.setBlock(self.x+self.l-x,self.y+y,self.z+self.w,1)
        mc.postToChat("Three Walls complete.")

    def build_door_and_window(self):
        for y in range(self.h):
            mc.setBlock(self.x,self.y+y,self.z+self.w,1)
        mc.setBlock(self.x,self.y,self.z+self.w-1,0)
        for y in range(3,self.h):
            mc.setBlock(self.x,self.y+y,self.z+self.w-1,1) # build the door
        for y in range(self.h):
            mc.setBlock(self.x,self.y+y,self.z+self.w-2,1) 
        for y in range(2):
            mc.setBlock(self.x,self.y+y,self.z+self.w-3,1)
        for y in range(2):
            mc.setBlock(self.x,self.y+y,self.z+self.w-4,1)
        mc.setBlock(self.x,self.y+2,self.z+self.w-3,102)
        mc.setBlock(self.x,self.y+2,self.z+self.w-4,102)
        for y in range(3,self.h):
            mc.setBlock(self.x,self.y+y,self.z+self.w-3,1)
        for y in range(3,self.h):
            mc.setBlock(self.x,self.y+y,self.z+self.w-4,1) # build the window
        for z in range(5,self.w):
            for y in range(self.h):
                mc.setBlock(self.x,self.y+y,self.z+self.w-z,1)
        mc.postToChat("A wall with door and window complete.")
    def build_roof(self):
        for x in range(self.l+1):
            for z in range(self.w+1):
                mc.setBlock(self.x+x,self.y+self.h,self.z+z,2)

    def decorate_floor(self):
        f = open("tile.csv","r")
        for z in range(5):
            style = f.readline()
            x = 0
            for i in range(9):   
                if style[i] == ',':
                    x = x
                elif int(style[i]) == 0:
                    x = x + 1
                    mc.setBlock(self.x+x,self.y,self.z+1+z, 41)
                elif int(style[i]) == 1:
                    x = x + 1
                    mc.setBlock(self.x+x,self.y,self.z+1+z, 5)
        

pos=mc.player.getTilePos()
house1=House(pos.x,pos.y,pos.z)
house1.setLWH(6,6,5)
house1.build_three_walls()
house1.build_door_and_window()
house1.build_roof()
house1.decorate_floor()
