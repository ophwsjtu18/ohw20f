import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from math import sin

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    for i in range(10):
        mc.player.setTilePos(pos.x+1+i,pos.y,pos.z)
        time.sleep(0.5)

    for i in range(10):
        mc.player.setTilePos(pos.x+9-i,pos.y,pos.z)
        time.sleep(0.5)
        
    for i in range(10):
        mc.player.setTilePos(pos.x,pos.y,pos.z+1+i)
        time.sleep(0.5)
        
    for i in range(10):
        mc.player.setTilePos(pos.x,pos.y,pos.z+9-i)
        time.sleep(0.5)
