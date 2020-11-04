import mcpi.minecraft as minecraft
import time
import mcpi.block as block
import serial
mc = minecraft.Minecraft.create()
#ser = serial.Serial("COM3")
                
class House():
        def __init__(self,x,y,z,name):
                self.x=x
                self.y=y
                self.z=z
                self.name=name
                mc.postToChat("hello world. I will build a house named "+ self.name +" at "+str(self.x)+", "+str(self.y)+", "+str(self.z))

        def setLWH(self,l,w,h):
                self.l=l
                self.w=w
                self.h=h
                

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

                
house1=House(-46,11,-37,"czl_house")


house1.setLWH(10,10,5)



house1.buildall()
while True:
        time.sleep(0.5)
        pos = mc.player.getTilePos()
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
        if pos.x == -43 and pos.z == -36 and 10 < pos.y < 17:
                mc.postToChat("Welcome to czl_house")
        
#实现：当人物停在房屋门口时，显示房屋名称
##
f=open(r'C:\Users\Caizilin\Desktop\songs.csv',"r")

songs=[]
songmenu={}
while True:
    line=f.readline()
    if line == "":
        break
    linedata=line.strip().split(",")
    songs.append(linedata)
    print(line)
    songmenu[linedata[0]]=linedata[1:-1]
print(songs)
#未完成歌曲选择部分
while True:
        time.sleep(0.5)
        pos = mc.player.getTilePos()
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
        if -45 < pos.x < -35 and -37 < pos.z < -27 and 10 < pos.y < 17:
                for a in songs:
                    ser.write(a.encode())
                    time.sleep(5)
##
