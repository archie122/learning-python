def divisions(n, divisor):
    count = 0
    x = n
    for i in range(n):
        x = x / divisor
        if x >= 1:
            count += 1

    return count


print(divisions(100, 2))