import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import serial
import math

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()


class POS():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# pos = POS(50, 0, 50)

class House(object):
    def __init__(self, x=0, y=0, z=0, length=10, width=10, height=5, name='myhouse', music='twotiger', filename='', musicfile='songs.csv'):
        self.x = x
        self.y = y
        self.z = z
        self.store = []
        self.file = filename
        self.musicfile = musicfile
        if self.file == '':
            self.length = length
            self.width = width
        else:
            f = open(self.file, 'r')
            while True:
                line = f.readline()
                if line == '':
                    break
                linedata = line.strip().split(",")
                self.store.append(linedata)
            self.length = len(self.store)
            self.width = len(self.store[0])
        self.height = height
        self.name = name
        self.music = music
        print("the house location:(" + str(x) + ", " + str(y) + ", " + str(z) + ") the size is: " + str(
            self.length) + '*' + str(self.width) + '*' + str(self.height))

    def clear(self):
        for i in range(-2 * self.length, 2 * self.length + 1):
            for j in range(-2 * self.width, 2 * self.width + 1):
                for k in range(3 * self.height):
                    mc.setBlock(pos.x + i, pos.y + k, pos.z + j, 0)

    def creat_floor(self, build_id=5):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for i in range(-(self.length // 2), l_ceil):
            for j in range(-(self.width // 2), w_ceil):
                mc.setBlock(pos.x + i, pos.y, pos.z + j, build_id)

    def creat_wall(self, build_id=5, roof_id=20):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for i in range(self.height):
            for j in range(-(self.width // 2), w_ceil):
                mc.setBlock(pos.x - (self.length // 2), pos.y + i, pos.z + j, build_id)
                mc.setBlock(pos.x + l_ceil - 1, pos.y + i, pos.z + j, build_id)
            for k in range(-(self.length // 2), l_ceil):
                mc.setBlock(pos.x + k, pos.y + i, pos.z - (self.width // 2), build_id)
                mc.setBlock(pos.x + k, pos.y + i, pos.z + w_ceil - 1, build_id)

        # roof

        tem_tall = (min(self.width, self.length) // 2)
        for i in range(1, tem_tall + 1):
            tem_width = self.width - 2 * i
            tem_length = self.length - 2 * i
            for j in range(-(tem_width // 2), math.ceil(tem_width / 2)):
                mc.setBlock(pos.x - (self.length // 2) + i, pos.y + self.height + i - 1, pos.z + j, roof_id)
                mc.setBlock(pos.x + l_ceil - 1 - i, pos.y + self.height + i - 1, pos.z + j, roof_id)
            for j in range(-(tem_length // 2), math.ceil(tem_length / 2)):
                mc.setBlock(pos.x + j, pos.y + self.height + i - 1, pos.z - (self.width // 2) + i, roof_id)
                mc.setBlock(pos.x + j, pos.y + self.height + i - 1, pos.z + w_ceil - 1 - i, roof_id)

    def creat_door(self):
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 1, pos.z, 0)
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 2, pos.z, 0)
        mc.setBlock(pos.x + math.ceil(self.length / 2) - 1, pos.y + 1, pos.z, 324)

    def creat_window(self, window_id=102):
        l_ceil = math.ceil(self.length / 2)
        w_ceil = math.ceil(self.width / 2)
        for k in range(self.width // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(pos.x + l_ceil - 1, pos.y + 2 + i, pos.z + 2 + 4 * k + j, window_id)
                    mc.setBlock(pos.x + l_ceil - 1, pos.y + 2 + i, pos.z - 2 - 4 * k - j, window_id)
                    mc.setBlock(pos.x - (self.length // 2), pos.y + 2 + i, pos.z + 2 + 4 * k + j, window_id)
                    mc.setBlock(pos.x - (self.length // 2), pos.y + 2 + i, pos.z - 2 - 4 * k - j, window_id)
        for k in range(self.length // 8):
            for i in range(2):
                for j in range(2):
                    mc.setBlock(pos.x + 2 + 4 * k + j, pos.y + 2 + i, pos.z + w_ceil - 1, window_id)
                    mc.setBlock(pos.x - 2 - 4 * k - j, pos.y + 2 + i, pos.z + w_ceil - 1, window_id)
                    mc.setBlock(pos.x + 2 + 4 * k + j, pos.y + 2 + i, pos.z - (self.width // 2), window_id)
                    mc.setBlock(pos.x - 2 - 4 * k - j, pos.y + 2 + i, pos.z - (self.width // 2), window_id)

    def creat_whole_house(self):
        self.clear()
        self.creat_floor()
        self.creat_wall()
        self.creat_door()
        self.creat_window()

    def creat_floor_from_csv(self, build_id_1=41, build_id_2=89):
        if self.file == '':
            print("WRONG: not find the file")
        else:
            l_ceil = math.ceil(self.length / 2)
            w_ceil = math.ceil(self.width / 2)
            for i in range(-(self.length // 2), l_ceil):
                for j in range(-(self.width // 2), w_ceil):
                    if self.store[i+(self.length // 2)][j+(self.width // 2)] == '1':
                        mc.setBlock(pos.x + i, pos.y, pos.z + j, build_id_2)
                    else:
                        mc.setBlock(pos.x + i, pos.y, pos.z + j, build_id_1)

    def creat_whole_house_from_csv(self, build_id_1=41, build_id_2=89, roof_id=20, window_id=102):
        self.clear()
        self.creat_floor_from_csv(build_id_1, build_id_2)
        self.creat_wall(build_id_1, roof_id)
        self.creat_door()
        self.creat_window(window_id)

    def play_music(self, COM='COM7'):
        ser = serial.Serial(COM)
        mf = open(self.musicfile)
        songs = []
        song_num = 0
        while True:
            line = mf.readline()
            if line == "":
                break
            linedata = line.strip().split(",")
            songs.append(linedata)
            song_num += 1

        songmenu = {}
        i = 0
        while i < song_num:
            songmenu[songs[i][0]] = songs[i][1:]
            i += 1

        time.sleep(2)
        pos_now = mc.player.getTilePos()
        while self.x - self.length // 2 <= pos_now.x <= self.x + self.length // 2 and self.y <= pos_now.y <= self.y + self.height // 2 and self.z - self.width // 2 <= pos_now.z <= self.z + self.width // 2:
            for i in range(len(songmenu[self.music])):
                if (songmenu[self.music][i] == ''):
                    break
                ser.write((songmenu[self.music][i] + 'a').encode())
                print(songmenu[self.music][i].encode())
                time.sleep(0.5)
            time.sleep(1)


house = House(pos.x, pos.y, pos.z, filename='input_floor.csv')
house.clear()
house.creat_whole_house_from_csv(roof_id=41)
