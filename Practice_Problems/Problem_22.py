def points(games):
    result = 0
    for game in games:
        if game[0] > game[2]:
            result += 3
        elif game[0] < game[2]:
            result += 0
        else:
            result += 1
    return result

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))