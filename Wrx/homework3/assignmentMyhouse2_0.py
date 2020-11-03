
song1=["1","1","5","5","6","6","5"]
song2=["3","3","4","5","5","4","3","2","1","1","2","3","3"]
songMenu={}
songMenu["tinkleStar"]=song1
songMenu["OdeToJoy"]=song2

class myHouse():
    houseName="spouse"
    # position
    x=None
    y=None
    z=None
    # size
    L=None
    W=None
    H=None
    song=None

    def __init__(self,Length,Wide,Height,pos):
        self.L=Length
        self.W=Wide
        self.H=Height
        self.pos=pos
        
    def rename(self,newName):
        self.houseName=newName

    def setSong(self,song):
        self.song=song

    def singSong(self):
        ser=serial.Serial("COM6",9600,timeout=1)
        for a in self.song:
            ser.write(a.encode())
            time.sleep(0.5)

    def buildFloor(self):
        with open("floor.csv","r") as f:
            reader=csv.reader(f)
            for x in range(self.L):
                for z in range (self.W):
                    mc.setBlock(self.pos.x+x,self.pos.y,self.pos.z+z,block.STONE.id)
            for i,row in enumerate(reader):
                for j,a in enumerate(row):
                    if a=='1':
                        mc.setBlock(self.pos.x+i,self.pos.y,self.pos.z+j,41)
                    if a=='2':
                        mc.setBlock(self.pos.x+i,self.pos.y,self.pos.z+j,57)
                        

    def buildWall(self):
        for x in range(self.L):
            for y in range (self.H):
                mc.setBlock(self.pos.x+x,self.pos.y+y+1,self.pos.z,block.STONE.id)
                mc.setBlock(self.pos.x+x,self.pos.y+y+1,self.pos.z+self.W-1,block.STONE.id)
        for z in range(self.W-2):
            for y in range (self.H):
                mc.setBlock(self.pos.x,self.pos.y+y+1,self.pos.z+z+1,block.STONE.id)
                mc.setBlock(self.pos.x+self.L-1,self.pos.y+y+1,self.pos.z+z+1,block.STONE.id)

    def buildRoof(self):
        for y in range(6):
             for x in range(self.L+2-2*y):
                 for z in range(self.W+2-2*y):
                     if y%2:
                         mc.setBlock(self.pos.x+x-1+y,self.pos.y+self.H+1+y,self.pos.z+z-1+y,57)
                     else:
                         mc.setBlock(self.pos.x+x-1+y,self.pos.y+self.H+1+y,self.pos.z+z-1+y,79)


    def buildDoor(self):
        for x in range(2):
            for y in range (3):
                 mc.setBlock(pos.x+x+(self.L)//2,pos.y+1+y,pos.z,330)
                 
    def buildWindow(self):
        for z in range(4):
            for y in range (4):
                mc.setBlock(pos.x, pos.y+y+2, pos.z+z+4,20)

    def buildAll(self):
        self.buildFloor()
        self.buildWall()
        self.buildRoof()
        self.buildDoor()
        self.buildWindow()

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
house1=myHouse(15,15,7,pos)
house1.buildAll()
house1.setSong("song1")
house1.singSong()
