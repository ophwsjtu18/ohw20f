import cgi, cgitb
import os
from time import sleep
from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1",4711)

form = cgi.FieldStorage() 

site_dir  = form.getvalue('mc_dir')

pos=mc.player.getTilePos()

if site_dir=='up':
    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
if site_dir=='down':
    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
if site_dir=='left':
    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
if site_dir=='right':
    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
