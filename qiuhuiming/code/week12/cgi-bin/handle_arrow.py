#!C:\dev\Anaconda3\python.exe
#coding=utf-8
import cgi, cgitb
from typing import AnyStr 
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# 创建 FieldStorage 实例化
form = cgi.FieldStorage() 

log_file = 'log'
arrow = form.getvalue('arrow')

mc.player.setDirection([1, 0, 0])
steps = {
    'up': [5, 0],
    'down': [-5, 0],
    'left': [0, -5],
    'right':[0, 5]
}

def move(step):
    pos = mc.player.getTilePos()
    mc.player.setTilePos(pos.x + step[0], pos.y, pos.z + step[1])

if arrow in steps.keys():
    move(steps[arrow])
elif arrow == 'cycle': # 循环向前后左右各走10步
    for direct in steps.keys():
        for i in range(10):
            move(steps[direct])
            time.sleep(0.1)

#*******************************************************************
print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>MOOC</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s:%s</h2>" % (log_file, arrow))
print ("</body>")
print ("</html>")
#*******************************************************************


with open(log_file+'.txt', 'w') as f:
    f.write(f'{arrow}')

