#!C:\Program Files\Python38\python.exe
#coding=utf-8
import cgi, cgitb

import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1", 4711)

form = cgi.FieldStorage()

site_dir = form.getvalue("mc_dir")



print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset = \"utf-8\" />")
print("<title>mc movement</title>")
print("</head>")
print("<body>")
print("<h2>%s</h2>" % (site_dir))
print("</body>")
print("</html>")

pos = mc.player.getTilePos()

if site_dir=="1":
    mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
    pos = mc.player.getTilePos()
    time.sleep(0.2)

elif site_dir=="2":
    mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
    pos = mc.player.getTilePos()
    time.sleep(0.2)

elif site_dir=="3":
    mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
    pos = mc.player.getTilePos()
    time.sleep(0.2)

elif site_dir=="4":
    mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
    pos = mc.player.getTilePos()
    time.sleep(0.2)

elif site_dir=="5":
    for i in range(10):
        mc.player.setTilePos(pos.x+1, pos.y, pos.z)
        pos = mc.player.getTilePos()
        time.sleep(0.1)
    for i in range(10):
        mc.player.setTilePos(pos.x+1, pos.y, pos.z+1)
        pos = mc.player.getTilePos()
        time.sleep(0.1)
    for i in range(10):
        mc.player.setTilePos(pos.x-1, pos.y, pos.z)
        pos = mc.player.getTilePos()
        time.sleep(0.1)
    for i in range(10):
        mc.player.setTilePos(pos.x, pos.y, pos.z-1)
        pos = mc.player.getTilePos()
        time.sleep(0.1)






    
