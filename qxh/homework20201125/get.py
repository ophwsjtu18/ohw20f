#!C:\Users\Caizilin\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi, cgitb

import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1", 4711)

form = cgi.FieldStorage()

site_dir = form.getvalue("mc_dir")

move_loop = form.getvalue("mc_move_loop")




pos = mc.player.getTilePos()

if site_dir=="w":
    mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
    pos = mc.player.getTilePos()
    print('pos:(', pos.x, ',', pos.y, ',', pos.z, ')')
    time.sleep(0.2)

elif site_dir=="s":
    mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
    pos = mc.player.getTilePos()
    print('pos:(', pos.x, ',', pos.y, ',', pos.z, ')')
    time.sleep(0.2)

elif site_dir=="a":
    mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
    pos = mc.player.getTilePos()
    print('pos:(', pos.x, ',', pos.y, ',', pos.z, ')')
    time.sleep(0.2)

elif site_dir=="d":
    mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
    pos = mc.player.getTilePos()
    print('pos:(', pos.x, ',', pos.y, ',', pos.z, ')')
    time.sleep(0.2)
        
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
