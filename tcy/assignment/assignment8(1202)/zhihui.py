from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

mx = MOOCXING()

APP_ID ='23084461'
API_KEY ='eSkkgBNvNncqoRrlZPsxCnGi'
SECRET_KEY ='mwlcVGM0qTfBhrtWSBcMNGVUI1K37mGa'

media = mx.initMedia()

thread = mx.initThread()
mqtt = mx.initMqtt()
pinyin = mx.initPinyin()
mc = mx.initMinecraft()
serial = mx.initSerial(com="COM5", bps=9600)
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp = mx.initNLP(APP_ID, API_KEY, SECRET_KEY)
print("******************初始化完成******************\n")

brain = Brain({"media": media,
               "speech": speech,
               "nlp": nlp,
               "mqtt": mqtt,
               "serial": serial,
               "thread": thread,
               "pinyin": pinyin,
               "minecraft": mc})
print("***************技能插件加载完成****************\n")


def TTSPlay(text):
    speech.TTS(text)
    media.play()


def recordSTT():
    media.record()
    return speech.STT()


while True:
    result = recordSTT()
    pos = mc.player.getTilePos()
    jiao_du = mc.player.getRotation()
    if "左转" in result:
        mc.player.setRotation(jiao_du - 30)
    if "右转" in result:
        mc.player.setRotation(jiao_du + 30)
    if "向前" in result:
        mc.player.getTilePos(pos.x + 1, pos.y, pos.z)
    if "向后" in result:
        mc.player.getTilePos(pos.x - 1, pos.y, pos.z)
    if "向左" in result:
        mc.player.getTilePos(pos.x, pos.y, pos.z + 1)
    if "向右" in result:
        mc.player.getTilePos(pos.x, pos.y, pos.z - 1)

    if not brain.query(result, _print=True):
        if "左转" in result:
            TTSPlay("好的，向左转")
            serial.send("1a")
        if "右转" in result:
            TTSPlay("好的，向右转")
            serial.send("2a")
