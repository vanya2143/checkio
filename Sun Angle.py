"""
https://py.checkio.org/ru/mission/sun-angle/

Ваша задача - определить угол солнца над горизонтом,
зная время суток. Исходные данные: солнце встает на востоке в 6:00,
что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов.
В 18:00 солнце садится за горизонт и угол равен 180 градусов. В случае,
если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".

"""


def sun_angle(time):
    start = 21600  # 6:00 in seconds
    finish = 64800  # 18:00 in seconds

    one_degree = (finish - start) / 180  # one degree in seconds
    h, m = time.split(':')
    time_in_seconds = (int(h) * 60 ** 2) + (int(m) * 60)

    if time_in_seconds < start or time_in_seconds > finish:
        return "I don't see the sun!"

    return (time_in_seconds - start) / one_degree


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
