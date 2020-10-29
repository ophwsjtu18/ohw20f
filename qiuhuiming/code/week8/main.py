from CsvUtils import read_house_csv, read_songs_csv
from House import House
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

if __name__ == "__main__":
    house_name, song_name, house_floor = read_house_csv('./house.csv')
    song_menu = read_songs_csv('./songs.csv')

    pos = mc.player.getTilePos()
    house = House()
    house.set_name('米奇妙妙屋')
    house.set_song(song_menu[song_name][1:])
    house.set_position(pos.x + 5, pos.y, pos.z + 5)
    house.set_size(len(house_floor), len(house_floor[0]), 20)
    house.set_floor(house_floor)
    house.build()

    while True:
        pos = mc.player.getTilePos()
        house.print_position()
        mc.postToChat('Your position: x: {}, y: {}, z: {}'.format(
            pos.x, pos.y, pos.z))
        if house.is_comtain_tile(pos):
            mc.postToChat('Welcome to {}!'.format(house.name))
            break
        time.sleep(2)
