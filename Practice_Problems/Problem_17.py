def better_than_average(class_points, your_points):
    return your_points > sum(class_points)/len(class_points)

print(better_than_average([2, 3], 5))


