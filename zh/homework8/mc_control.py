from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mx = MOOCXING()
'''
APP_ID = '22929503'
API_KEY = 'WresMkF1o4342KeqZBOsjXId'
SECRET_KEY = 'BrDOj5quiTuhwxpULsVzWdw5nmcyrTIl'
'''
APP_ID='23084382'
API_KEY='ka5P4d1iP9W8yEsIcFwGPYCm'
SECRET_KEY='xQXk8YV5YYPhIvmG23eX21Wgp5E6m8h6'

media = mx.initMedia()

serial = mx.initSerial(com="COM4", bps=9600)

speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

print("************initialization finish**********")

brain = Brain({"media": media, "speech": speech, "serial":serial})

print("************技能插件加载完毕************")

def TTSPlay(text):
    speech.TTS(text)
    media.play()

def recordSTT():
    media.record()
    return speech.STT()

pos = mc.player.getTilePos()

i = 1
j = 1

while True:
    result = recordSTT()

    if not brain.query(result, _print=True):
        if "左" in result:
            TTSPlay("好的，约翰将向左走10步")
            serial.send("1") #1表示舵机转为180
            mc.player.setTilePos(pos.x + 10*i, pos.y, pos.z)
            i += 1
        if "右" in result:
            TTSPlay("好的，约翰将向右走十步")
            serial.send("2") #2表示舵机转为0
            mc.player.setTilePos(pos.x - 10*j, pos.y, pos.z)
            j += 1
        if "正" in result:
            TTSPlay("好的，约翰将回正")
            serial.send("3")  #3表示舵机转为90
            mc.player.setTilePos(pos.x, pos.y, pos.z)
            i = 1
            j = 1
