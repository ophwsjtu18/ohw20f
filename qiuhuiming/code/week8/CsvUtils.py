# house.csv文件内容格式：
# 第一行:${house_name},${song_name}
# 第二行到最后: 地板花纹矩阵

def read_house_csv(file_name):
    file = open(file=file_name)
    first_line = file.readline()
    first_line = first_line.strip().split(',')
    print(first_line)
    house_name = first_line[0]
    song_name = first_line[1]
    house_flour = []
    index = 0
    while True:
        line = file.readline()
        if line == '':
            break
        house_flour.append(line.strip().split(','))
        if index > 0 and len(house_flour[index]) != len(house_flour[index - 1]):
            raise Exception('Error: invalid config at csv file.')
        index = index + 1

    return house_name, song_name, house_flour


def read_songs_csv(file_name):
    file = open('./songs.csv', 'r')
    # songs = []
    songs_menu = {}
    while True:
        line = file.readline()
        if line == '':
            break
        line_data = line.strip().split(',')
        # songs.append(line_data)
        songs_menu[line_data[0]] = line_data[1:]
    return songs_menu


if __name__ == "__main__":
    print(read_songs_csv('./songs.csv'))
