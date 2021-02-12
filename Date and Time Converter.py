"""
https://py.checkio.org/ru/mission/date-and-time-converter/

Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
"""

mouth = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}


# Show digit without leading zero
def remove_leading_zero(digit: str):
    if digit.startswith('0'):
        return digit[1]
    return digit


def one_many(time_digit: str, time_elem: str):
    return time_elem if time_digit == "1" else time_elem + "s"


def date_time(time: str) -> str:
    date, time = time.split()
    time = [remove_leading_zero(x) for x in time.split(':')]
    date = date.split('.')

    time_string = f'{time[0]} {one_many(time[0], "hour")} ' \
                  f'{time[1]} {one_many(time[1], "minute")}'

    return f'{remove_leading_zero(date[0])} {mouth.get(date[1])} {date[2]} year {time_string}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    assert date_time("20.11.1990 01:01") == "20 November 1990 year 1 hour 1 minute", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
