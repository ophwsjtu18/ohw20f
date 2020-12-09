import mcpi
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    for a in range (10):
        mc.player.setPos(pos.x+a,pos.y,pos.z)
        time.sleep(1)
    pos = mc.player.getTilePos()
    for b in range (10):
        mc.player.setPos(pos.x-b,pos.y,pos.z)
        time.sleep(1)
    pos = mc.player.getTilePos()
    for c in range (10):
        mc.player.setPos(pos.x,pos.y,pos.z+c)
        time.sleep(1)
    pos = mc.player.getTilePos()
    for d in range (10):
        mc.player.setPos(pos.x,pos.y,pos.z-d)
        time.sleep(1)
