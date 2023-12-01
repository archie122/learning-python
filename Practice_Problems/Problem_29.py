def eliminate_unset_bits(number):
    if number.count('1') == 0:
        return 0
    return int(number.replace('0', ''), 2)


print(eliminate_unset_bits('1100')
