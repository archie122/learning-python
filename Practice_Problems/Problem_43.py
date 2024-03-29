str_numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'ten': 10,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000
}


def parse_int(string):
    if string is None:
        return 0

    number = 0
    temp = 0
    word_list = string.lower().replace('-', ' ').split()

    if 'and' in word_list:
        word_list.remove('and')

    for word in word_list:
        value = str_numbers.get(word)

        if value == 1000 or value == 1000000:
            number += value * temp
            temp = 0
        elif value == 100:
            temp *= value
        else:
            temp += value
    number += temp

    return number


print(parse_int(None))