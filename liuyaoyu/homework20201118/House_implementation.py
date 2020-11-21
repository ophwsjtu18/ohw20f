import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

class House:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        mc.postToChat("A house will be build at"+"x="+str(self.x)+" y="+str(self.y)+" z="+str(self.z))
    def setLWH(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    
    def build_three_walls(self):
        for x in range(self.l):
            for y in range(self.h):
                mc.setBlock(self.x+x,self.y+y,self.z,46)
        for z in range(self.w):
            for y in range(self.h):
                mc.setBlock(self.x+self.l,self.y+y,self.z+z,46)
        for x in range(self.l):
            for y in range(self.h):
                mc.setBlock(self.x+self.l-x,self.y+y,self.z+self.w,46)
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
        
    def build_all(self):
        self.build_three_walls()
        self.build_door_and_window()
        self.build_roof()
        print("Building complete!")
    

class Roundhouse(House):
    def __init__(self,x,y,z):
        super(Roundhouse, self).__init__(x,y,z)

    def setLWHR(self,l,w,h,r):
        super(Roundhouse, self).setLWH(l,w,h)
        self.r=r
    def build_roof(self):
        x_center = self.x + self.l*0.5
        z_center = self.z + self.w*0.5
        y_center = self.y + self.h
        r = self.r
        for x in range(-2*r, 2*r, 1):
            for z in range(-2*r, 2*r, 1):
                for y in range(0, 2*r, 1):
                    if x**2+y**2+z**2 <= 4*(r**2):
                        mc.setBlock(x_center+x,y_center+y,z_center+z,1)
    def build_all(self):
        super(Roundhouse, self).build_all()
        self.build_roof()

class Trianglehouse(House):
    def __init(self, x, y, z):
        super(Trianglehouse, self).__init__(x, y, z)
    def setLWH(self, l, w, h):
        super(Trianglehouse, self).setLWH(l, w, h)
        self.height = min(int(l/2)+1, int(w/2)+1)
    def build_roof(self):
        for y in range(self.height):
            for x in range(self.l+1-2*y):
                for z in range(self.w+1-2*y):
                    mc.setBlock(self.x+x+y,self.y+self.h+y,self.z+z+y,46)
    def build_all(self):
        super(Trianglehouse, self).build_all()
        self.build_roof()


pos=mc.player.getTilePos()
# house1=Roundhouse(pos.x,pos.y,pos.z)
# house1.setLWHR(6,6,5,3)
# house1.build_all()

house2 = Trianglehouse(pos.x, pos.y, pos.z)
house2.setLWH(6,6,5)
house2.build_all()
