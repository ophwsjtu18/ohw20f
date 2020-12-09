from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain
import time
mx = MOOCXING()

#百度API
APP_ID = '23084421'
API_KEY = 'lSSiLK5SQpqfY8XWv44Phsyx'
SECRET_KEY = 'NnXueTntGHywGYHUTSZuQdE92qQX6nnQ'

#初始化播放器和录音模块
media = mx.initMedia()
#初始化串口模块
serial = mx.initSerial(com='COM3',bps=9600)
#初始化我的世界
mc = mx.initMinecraft()
#初始化语音识别+语音合成模块
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

print("*************初始化完成*************\n")

#初始化技能插件
brain = Brain({"media": media,
               "speech": speech,
               "serial": serial,
               "minecraft":mc,})
print("*************初始化完成*************\n")

#语音合成+播放
def TTSPlay(text):
    speech.TTS(text)
    media.play()

#录音+语音识别
def recordSTT():
    media.record()
    return speech.STT()

while True:
    result = recordSTT()
    pos = mc.player.getTilePos()
    print('pos:(', pos.x, ',', pos.y, ',', pos.z, ')')
    if not brain.query(result, _print=True):
        if "向前" in result:
            TTSPlay("好的，向前")
            for i in range(10):
                mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
                pos = mc.player.getTilePos()
                time.sleep(0.2)
        if "向后" in result:
            TTSPlay("好的，向后")
            for i in range(10):
                mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
                pos = mc.player.getTilePos()
                time.sleep(0.2)
        if "向左" in result:
            TTSPlay("好的，向左")
            for i in range(10):
                mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
                pos = mc.player.getTilePos()
                time.sleep(0.2)
        if "向右" in result:
            TTSPlay("好的，向右")
            for i in range(10):
                mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
                pos = mc.player.getTilePos()
                time.sleep(0.2)
        if "向左转30度" in result:
            TTSPlay("好的，向左转30度")
            serial.send('L')
        if "向右转30度" in result:
            TTSPlay("好的，向右转30度")
            serial.send('R')
