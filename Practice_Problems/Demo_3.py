def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case

print(to_camel_case(""))
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case("The_Stealth_Warrior"))