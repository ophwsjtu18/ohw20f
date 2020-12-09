from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain
import mcpi.minecraft as minecraft
#mc = minecraft.Minecraft.create()
import time
mx = MOOCXING()

APP_ID='23084374'
API_KEY='tpX4lf7mGrrEsZEbi22DrvcE'
SECRET_KEY='fDlmrcLxGqcPPbO8phNxu7FMQ97V928j'


media = mx.initMedia()

thread = mx.initThread()

mqtt = mx.initMqtt()

pinyin = mx.initPinyin()

mc = mx.initMinecraft()

serial = mx.initSerial(com="COM3",bps=9600)

speech = mx.initSpeech(APP_ID,API_KEY,SECRET_KEY)

nlp = mx.initNLP(APP_ID,API_KEY,SECRET_KEY)

print("********************初始化完成************************\n")

brain = Brain({"media":media,
               "speech":speech,
               "nlp":nlp,
               "mqtt":mqtt,
               "serial":serial,
               "thread":thread,
               "pintin":pinyin,
               "minecraft":mc})

print("********************技能插件加载完成*******************\n")


#语音合成与播放
def TTSPlay(text):
    speech.TTS(text)
    media.play()

#录音加语音识别
def recondSTT():
    media.record()
    return speech.STT()

a=1
while True():
    result = recondSTT()
    #pos = mc.player.getTilePos()
    #mc.postToChat("x=" + str(pos.x) + "y" + str(pos.y) + "z" + str(pos.z))
    #time.sleep(1)

    if not brain.query(result, _print=False):
        if "左转" in result:
            TTSPlay("好的，向左转")
            serial.send("1a")
            #mc.player.setTilePos([pos.x+10,pos.y,pos.z])
        if "右转" in result:
            TTSPlay("好的，向右转")
            serial.send("2a")
            #mc.player.setTilePos([pos.x+10,pos.y,pos.z])
            


