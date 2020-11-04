import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import serial as se

song1 = ['1','1','5','5','6','6','5','4','4','3','3','2','2','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5'] 
mc=minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))

class House():
    def __init__(self,x_,y_,z_,L,W,H,name,song):
        self.x=x_
        self.y=y_
        self.z=z_
        self.L=L
        self.W=W
        self.H=H
        self.name=name
        self.song=song
    def printName(self):
        print("the house's name is",self.name)
    def playtheSong(self):
        if self.song == 'xiaoxinxin':
            self.song = song1
        if self.song == 'datuhao':
            self.song = song2
        """
        ser = se.Serial("COM7",9600,timeout=1)
        while True:
            i=0
            x=str(self.song[i])
            if x == "":
                break
            ser.write(x.encode())
        """
    def buildground(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y,self.z+b,5)
        print("done")

    def buildwall(self):
        for c in range(self.H):
            for a in range(self.L):
                mc.setBlock(self.x+a,self.y+c,self.z,5)
                mc.setBlock(self.x+a,self.y+c,self.z+self.W-1,5)
            for b in range(self.W-2):
                mc.setBlock(self.x,self.y+c,self.z+1+b,5)
                mc.setBlock(self.x+self.L-1,self.y+c,self.z+1+b,5)
        print("done")
    def buildroof(self):
        for a in range(self.L):
            for b in range(self.W):
                mc.setBlock(self.x+a,self.y+self.H-1,self.z+b,5)
        print("done")
    def builddoor(self):
        mc.setBlock(self.x+self.L/2,self.y+1,self.z,0)
        mc.setBlock(self.x+self.L/2,self.y+2,self.z,0)
        print("done")
    def buildwindows(self):
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x+self.L-1,self.y+y+2,self.z+z+4,20)
        print("done")
    def decoratefloor(self):
        with open('C:\\Users\\86159\\Desktop\\homework\\homework3\\floor.csv') as f:
            reader = csv.reader(f)
            for i,rows in enumerate(reader):
                for a in range(1,self.W-1):
                    if i == a:
                        for b in range(1,self.L-1):
                            if rows[b]=='0':
                                mc.setBlock(self.x+b,self.y,self.z+i,5)
                            if rows[b]=='1':
                                mc.setBlock(self.x+b,self.y,self.z+i,41)

    def buildall(self):
        self.buildground()
        self.buildroof()
        self.buildwall()
        self.buildwindows()
        self.builddoor()
        self.printName()
        self.playtheSong()
        self.decoratefloor()

house1=House(170,90,250,10,10,8,"BILL's house","datuhao")
house1.buildall()
