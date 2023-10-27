def is_isogram(string):
    string = string.lower()

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    return True

print(is_isogram('isogram'))