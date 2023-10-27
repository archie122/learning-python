def generate_hashtag(s):
    if s == '':
        return False

    s = s.lower().title().strip().replace(' ', '')
    result = '#' + s

    if len(s) > 140:
        return False
    return result

print(generate_hashtag("Hello World"))