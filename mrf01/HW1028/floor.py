import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

elem1=44
elem2=45

f=open("floor.csv","r")
while True:
    line=f.readline()
    if line=="":
        break
    linedata=line.strip('\n').split(",")
    for z in range(len(linedata)):
        if linedata[z]=='1':
            mc.setBlock(pos.x, pos.y, pos.z+z,elem1)
        else:
            mc.setBlock(pos.x, pos.y, pos.z+z,elem2)
