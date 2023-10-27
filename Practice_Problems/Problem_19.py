def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(char for char in string_ if char not in vowels)


print(disemvowel("This website is for losers LOL!"))
