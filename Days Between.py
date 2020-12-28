"""
https://py.checkio.org/ru/mission/days-diff/

Сколько вам лет в днях? Это легко вычислить - достаточно вычесть свой день рождения от сегодняшнего дня.
Мы имеем реальную задачу - посчитать разницу между любыми датами.

У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например, 19 апреля 1982 будет (1982, 4, 19).
Вы должны найти разницу в днях между имеющимися датами. Например, между сегодня и вчера = 1 день.
Разница между днями всегда будет положительной или нулем, не забывайте про абсолютное значение.

Входные данные: Две даты, как кортежи целых чисел.

Выходные данные: Разница между датами в днях, как целое число.
"""
from datetime import date


def days_diff(date1: tuple, date2: tuple) -> int:
    return abs((date(*date1) - date(*date2)).days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
