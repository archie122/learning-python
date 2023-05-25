def to_jaden_case(string):
    x = string.split(' ')
    result = ''
    for i in x:
        result += i.capitalize()
        result += ' '
    return result.rstrip()


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
