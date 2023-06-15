def unique_in_order(sequence):
    sequence = list(sequence)
    i = len(sequence) - 1
    while i > 0:
        if sequence[i] == sequence[i - 1]:
            sequence.pop(i)
        i -= 1
    return sequence


print(unique_in_order("AAAABBBCCDAABBB"))