def find_outlier(integers):
    x, y = [], []
    for i in integers:
        if i % 2 == 0:
            x.append(i)
        else:
            y.append(i)

    if len(x) < len(y):
        return x[0]
    else:
        return y[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
