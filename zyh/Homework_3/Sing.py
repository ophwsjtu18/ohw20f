import mcpi.minecraft as minecraft
import serial
mc = minecraft.Minecraft.create()
song = ['1','1','2','2','3','3','4','4']
pos = mc.player.getTilePos()
ser = serial.Serial("COM3")
base=[671,686,176,186,269,299,song],
while True:
    if pos.x>base[0] and pos.x<base[1] and \
       pos.y>base[2] and pos.y<base[3] and \
       pos.z>base[4] and pos.z<base[5]:
        for i in range(len(song)):
            ser.write(song[i].encode())
            time.sleep(1.0)
