"""
https://py.checkio.org/ru/mission/the-stone-wall/

В качестве входных данных вы получите многострочную строку, состоящую из '0' и '#' - вид стены сверху.
'#' будут показывать каменную часть стены, а '0' - пустоты.
Относительное расположение вас и стены следующее: вы смотрите на массив с нижней его части.
Ваша задача - найти координаты места, где стена наиболее узкая (как показано на рисунке ниже).
Ширина стены - это высота столбцов массива (многострочной строки).
Если таких мест несколько - выберите самое левое из них и верните его индекс по-горизонтали
(самый левый столбец имеет индекс 0).
"""


def stone_wall(wall):
    wall_seq = wall.strip().split('\n')
    rocks = [item.count('0') for item in zip(*wall_seq)]

    return rocks.index(max(rocks))


if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
