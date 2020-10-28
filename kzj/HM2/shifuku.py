from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("shifuku...")
for a in range(-7,8):
	for b in range(-7,8):
		mc.setBlock(pos.x+a,pos.y-1,pos.z+b,95)
	for b in range(0,11):
		mc.setBlock(pos.x-7,pos.y+b,pos.z+a,95)
		mc.setBlock(pos.x+a,pos.y+b,pos.z-7,95)
		mc.setBlock(pos.x+7,pos.y+b,pos.z+a,95)
		mc.setBlock(pos.x+a,pos.y+b,pos.z+7,95)
for a in range(11,22):
	for b in range(a-21,22-a):
		mc.setBlock(pos.x+a-21,pos.y+a,pos.z+b,7)
		mc.setBlock(pos.x+b,pos.y+a,pos.z+a-21,7)
		mc.setBlock(pos.x+21-a,pos.y+a,pos.z+b,7)
		mc.setBlock(pos.x+b,pos.y+a,pos.z+21-a,7)