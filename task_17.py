"""
https://py.checkio.org/ru/mission/compass-map-and-spyglass/

Ваша задача - посчитать суммарное количество шагов которое потребуется,
чтобы подобрать все 3 предмета - ('C' - compass), ('M' - map), ('S' - spyglass),
считая от вашей стартовой позиции. Таким образом,
итоговый результат будет суммой трех дистанций: от Y к C, от Y к M и от Y к S (не Y-C-M-S).
Учтите, что вы можете ходить в 8 направлениях - влево, вправо, вверх,
вниз и по диагонали в любую сторону. Ваша стартовая позиция - 'Y'.
"""


def navigation(seaside):
    dst = []
    src = []

    for row_index, row in enumerate(seaside):
        for elem_index, elem in enumerate(row):
            if elem == 'Y':
                src.extend([elem_index, row_index])
            elif elem:
                dst.append([elem_index, row_index])

    return sum(map(abs, [max([src[0] - dst_elem[0], src[1] - dst_elem[1]], key=abs) for dst_elem in dst]))


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      ['M', 0, 0, 0, 'S']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[0, 0, 'C'],
                       [0, 'S', 0],
                       ['M', 'Y', 0]]) == 4

    assert navigation([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'M', 0, 'S', 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'C', 0, 0, 0],
                       [0, 'Y', 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
