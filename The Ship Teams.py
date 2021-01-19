"""
https://py.checkio.org/ru/mission/the-ship-teams/

Вам необходимо поделить всех нанятых матросов на 2 команды,
согласно следующим правилам: те, чей возраст меньше 20 лет или больше 40 - отправляются на первый корабль,
все остальные - на второй. Это позволит молодым матросам перенять опыт более старших коллег.
В качестве исходных данных вы получите словарь, где ключами будут выступать фамилии матросов, а значениями - их возраст.
После того, как все матросы будут поделены между кораблями,
вам необходимо отсортировать их внутри каждого из списков в алфавитном порядке.
"""


def two_teams(sailors):
    return [
        sorted([key for key, value in sailors.items() if value < 20 or value > 40]),
        sorted([key for key, value in sailors.items() if 20 <= value <= 40])
    ]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
               ['Abrahams', 'Coleman'],
               ['Smith', 'Wesson']
           ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
               ['Fernandes', 'Kale', 'McCortney'],
               ['Johnson']
           ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
