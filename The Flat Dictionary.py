"""
https://py.checkio.org/ru/mission/flatten-dict/

 Дан словарь, в котором в качестве ключей используются строки, а в качестве значений строки или словари.
 Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах.
 Результатом будет словарь без вложенных словарей. Ключи должны содержать путь,
 составленный из родительских ключей из начального словаря, разделенных "/".
 Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой ("").
"""


def flatten(dictionary):
    items = list(dictionary.items())
    flat_dict = {}

    while items:
        item = items.pop()

        if isinstance(item[1], dict) and len(item[1]):
            for i in item[1]:
                items.append((item[0] + '/' + i, item[1].get(i)))
        elif len(item[1]) == 0:
            flat_dict[item[0]] = ""
        else:
            flat_dict[item[0]] = item[1]

    return flat_dict


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
