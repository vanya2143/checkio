"""
https://py.checkio.org/ru/mission/morse-decoder/

Ваша задача - расшифровать сообщение используя азбуку Морзе.
В шифровке будет использован 1 пробел между буквами одого слова и 3 пробела между отдельными словами.
Если расшифрованный текст начинается со слова, первая буква этого слова должна быть заглавной.
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    return ' '.join([''.join([MORSE.get(elem) for elem in word.split()]) for word in code.split('   ')]).capitalize()


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
