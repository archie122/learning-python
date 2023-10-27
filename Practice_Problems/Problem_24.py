def to_acronym(inp):
    x = inp.split(" ")
    for i in range(len(x)):
        x[i] = x[i][0].upper()
    return "".join(x)

print(to_acronym("PHP: Hypertext Preprocessor"))