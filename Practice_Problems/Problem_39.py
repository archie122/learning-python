import re

def alphabet_position(text):
    text = re.sub(r'[^A-Za-z]', '', text).strip().replace(' ', '').lower()
    n = []

    for x in text:
        n.append(ord(x) - 96)
    return ' '.join([str(x) for x in n])


print(alphabet_position("The sunset is at twelve o'clock"))
