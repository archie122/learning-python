def digitize(n):
    reversed_num = str(n)[::-1]
    return [int(i) for i in str(reversed_num)]


print(digitize(356))
