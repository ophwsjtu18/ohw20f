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
