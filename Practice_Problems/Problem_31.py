def find_short(s):
    s = s.split()
    return min(len(i) for i in s)

print(find_short("bitcoin take over the world maybe who knows perhaps"))
