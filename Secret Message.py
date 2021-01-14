"""
https://py.checkio.org/ru/mission/secret-message/

Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

Например: текст = " H ow are you? E h, ok. L ow or L ower? O hhh.",
если мы соберем все заглавные буквы, то получим сообщение "HELLO".
"""


def find_message(message: str) -> str:
    return ''.join(letter for letter in message if letter.isupper())


if __name__ == '__main__':
    print("Example:")
    print(find_message('How are you? Eh, ok. Low or Lower? Ohhh.'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message('How are you? Eh, ok. Low or Lower? Ohhh.') == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
