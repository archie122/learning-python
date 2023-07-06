def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(find_average([1, 2, 3, 4, 5]))



