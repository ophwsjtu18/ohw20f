import os
from time import sleep
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
mc.player.setRotation(0)
while True:
    pos = mc.player.getTilePos()
    print(pos)
    if os.path.isfile("mc_move.txt"):
        with open("mc_move.txt", 'r+') as file:
            dir = file.read()
            file.truncate(0)
        if dir == "w":
            mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        elif dir == "s":
            mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
        elif dir == "a":
            mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
        elif dir == "d":
            mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
    sleep(0.2)
