import serial
import time

ser = serial.Serial("COM3")

f = open('./songs.csv', 'r')

songs = []
songs_menu = {}
while True:
    line = f.readline()
    if line == '':
        break
    line_data = line.strip().split(',')
    songs.append(line_data)
    songs_menu[line_data[0]] = line_data[1:]

# tinkle_star = ["1", "1", "5", "5", "6", "6",
#                "5", "4", "4", "3", "3", "2", "2", "1"]
# two_tigers = ['1', '2', '3', '1', '1', '2', '3', '1', '3', '4', '5']

# song_menu = {}
# song_menu['tinkle_star'] = tinkle_star
# song_menu['two_tigers'] = two_tigers


print('Which song do you like? Enter the number:')
for i in range(len(songs)):
    print('{}. {}'.format(i + 1, songs[i][0]))
option = int(input('>> '))
song = songs_menu[songs[option - 1][0]]

time.sleep(2)
for i in song:
    ser.write((i+'$').encode())
    print(i)
    time.sleep(0.5)
