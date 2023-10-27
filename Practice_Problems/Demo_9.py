from collections import Counter

def find_it(seq):
    x = Counter(seq)
    for keys, values in x.items():
        if values % 2 == 1:
            return keys

print(find_it([0,1,0,1,0]))