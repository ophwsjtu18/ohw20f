import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1", 4711)

j = 0
while j < 10:
    pos = mc.player.getTilePos()
    for i in range(10):
        mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
        pos = mc.player.getTilePos()
        #time.sleep(0.3)
    for i in range(10):
        mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        pos = mc.player.getTilePos()
        #time.sleep(0.3)
    for i in range(10):
        mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
        pos = mc.player.getTilePos()
        #time.sleep(0.3)
    for i in range(10):
        mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
        pos = mc.player.getTilePos()
        #time.sleep(0.3)
    j += 1