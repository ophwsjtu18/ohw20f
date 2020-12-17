from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

mx = MOOCXING()

# 自己注册百度API
APP_ID='23084383'
API_KEY='OVroLCSOKhNl2XOZ155PlknW'
SECRET_KEY='Af4yMbptkkXdz7gw7LzUL5Sa49y3Mc8m'

# 初始化播放器和录音模块
media = mx.initMedia()
# 初始化多线程模块
thread = mx.initThread()
# 初始化MQTT模块
mqtt = mx.initMqtt()
# 初始化拼音模块
pinyin = mx.initPinyin()
# 初始化我的世界
mc = mx.initMinecraft()
# 初始化串口模块
serial = mx.initSerial(com="COM3",bps=9600)
# 初始化语音识别+语音合成模块
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)
# 初始化NLP模块
nlp = mx.initNLP(APP_ID, API_KEY, SECRET_KEY)


print("******************初始化完成******************\n")

# 初始化技能插件
brain = Brain({"media": media,
               "speech": speech,
               "nlp": nlp,
               "mqtt": mqtt,
               "serial": serial,
               "thread": thread,
               "pinyin": pinyin,
               "minecraft": mc})

print("***************技能插件加载完成***************\n")

# 语音合成+播放
def TTSPlay(text):
    speech.TTS(text)
    media.play()

# 录音+语音识别
def recordSTT():
    media.record()
    return speech.STT()


while True:
    result = recordSTT()

    '''
    brain.query(result,_print = False)
    参数: 
        result: 语言识别内容
        _print: 是否打印识别内容
    返回: 技能是否匹配成功(True/False)
    技能: 查时间、查天气、听音乐
    查时间关键词: 时间、几点、日期、日子、几号、星期
    查天气关键词: 天气（要加城市）
    听音乐关键词: 听、播放、首、歌 + 歌名
                暂停、继续、停止
                (网易云API部分歌曲可能不版权)
    '''
    if not brain.query(result, _print=True):
        if "向前" in result:
            TTSPlay("好的，向前走")
            pos=mc.player.getTilePos()
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
        if "向后" in result:
            TTSPlay("好的，向后走")
            pos=mc.player.getTilePos()
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
        if "向左" in result:
            TTSPlay("好的，向左走")
            pos=mc.player.getTilePos()
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
        if "向右" in result:
            TTSPlay("好的，向右走")
            pos=mc.player.getTilePos()
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
