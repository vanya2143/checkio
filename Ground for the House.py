"""
https://py.checkio.org/ru/mission/ground-for-the-house/

На входе ваша функция получит многострочную строку, состоящую из '0' и '#', где '0' обозначают пустые участки земли,
а '#' - часть вашего дома. Ваша задача - определить площадь прямоугольного участка земли, который вам необходим,
чтобы его хватило для постройки дома.
"""


def house(plan):
    if '#' not in plan:
        return 0

    plan_list = plan.strip().split('\n')
    data = [[], [], []]

    _ = [
        [data[0].insert(-1, index), data[1].insert(-1, row.find('#')), data[2].insert(-1, row.rfind('#'))]
        for index, row in enumerate(plan_list) if '#' in row
    ]

    plan_len = len(plan_list[min(data[0]):max(data[0]) + 1])
    rows_len = max(data[2]) - min(data[1]) + 1

    return plan_len * rows_len


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
