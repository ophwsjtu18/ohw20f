from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

mx = MOOCXING()

APP_ID = '23084347'
API_KEY =  'YKQvo3XqV2WSdRxj61q4f5M4'
SECRET_KEY = '36nC0XiFUPMlWNFRPnsONrsYr86Dd1D5'

media = mx.initMedia()
serial = mx.initSerial(com='COM1', bps=9600)
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)
mc = mx.initMinecraft()

brain = Brain({
    'media': media,
    'speech': speech,
    'serial': serial,
    'minecraft': mc
})

def TTSPlay(text):
    speech.TTS(text)
    media.play()

def recordSTT():
    media.record()
    return speech.STT()

while True:
    result = recordSTT()

    if not brain.query(result, _print=True):
        if '左转' in result:
            TTSPlay('好的，左转')
            serial.send('tl$')
        if '右转' in result:
            TTSPlay('好的，右转')
            serial.send('tr$')
        if '前进' in result:
            TTSPlay('好的，前进')
            pos = mc.player.getTilePos()
            mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
        if '后退' in result:
            TTSPlay('好的，后退')
            pos = mc.player.getTilePos()
            mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
        if '左移' in result:
            TTSPlay('好的，左移')
            pos = mc.player.getTilePos()
            mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
        if '右移' in result:
            TTSPlay('好的，右移')
            pos = mc.player.getTilePos()
            mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        if '约翰' in result:
            if '左转' in result:
                TTSPlay('好的，约翰左转')
                mc.player.setDirection()
                rotation = mc.player.getRotation()
                mc.player.setRotation(rotation - 30)
            elif '右转' in result:
                TTSPlay('好的，约翰右转')
                mc.player.setDirection()
                rotation = mc.player.getRotation()
                mc.player.setRotation(rotation + 30)

        