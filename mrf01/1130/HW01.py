import os
from time import sleep
from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1",4711)

while True:
    for i in range(10):
        pos=mc.player.getTilePos()
        print(pos)
        mc.player.setTilePos(pos.x+1,pos.y,pos.z)
        sleep(1)
    
    for i in range(10):
        pos=mc.player.getTilePos()
        print(pos)
        mc.player.setTilePos(pos.x-1,pos.y,pos.z)
        sleep(1)
    
    for i in range(10):
        pos=mc.player.getTilePos()
        print(pos)
        mc.player.setTilePos(pos.x,pos.y,pos.z+1)
        sleep(1)
    
    for i in range(10):
        pos=mc.player.getTilePos()
        print(pos)
        mc.player.setTilePos(pos.x,pos.y,pos.z-1)
        sleep(1)
