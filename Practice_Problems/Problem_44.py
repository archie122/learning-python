def filter_list(l):
    x = []
    for i in l:
        if type(i) == int:
            x.append(i)

    return x


x = filter_list([1, 2, 'a', 'b'])
print(x)