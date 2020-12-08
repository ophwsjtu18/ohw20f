from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

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

print("************技能插件加载完毕**********")

def TTSPlay(text):
    speech.TTS(text)
    media.play()

def recordSTT():
    media.record()
    return speech.STT()

while True:
    result = recordSTT()
    #请说 将舵机调整为几级
    if not brain.query(result, _print=True):
        if "0" in result or "零" in result:
            TTSPlay("好的，将舵机调整为0级")
            serial.send("0")
            # continue
        if "1" in result or "一" in result:
            TTSPlay("好的，将舵机调整为1级")
            serial.send("1")
            # continue
        if "2" in result or "二" in result:
            TTSPlay("好的，将舵机调整为2级")
            serial.send("2")
            # continue
        if "3" in result or "三" in result:
            TTSPlay("好的，将舵机调整为3级")
            serial.send("3")
            # continue
        if "4" in result or "四" in result:
            TTSPlay("好的，将舵机调整为4级")
            serial.send("4")
            # continue
        if "5" in result or "五" in result:
            TTSPlay("好的，将舵机调整为5级")
            serial.send("5")
            # continue
        if "6" in result or "六" in result:
            TTSPlay("好的，将舵机调整为6级")
            serial.send("6")
            # continue
        if "7" in result or "七" in result:
            TTSPlay("好的，将舵机调整为7级")
            serial.send("7")
            # continue
        if "8" in result or "八" in result:
            TTSPlay("好的，将舵机调整为8级")
            serial.send("8")
            # continue
        if "9" in result or "九" in result:
            TTSPlay("好的，将舵机调整为9级")
            serial.send("9")
            # continue
