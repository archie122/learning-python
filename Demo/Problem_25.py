def number(lines):
    numbered_lines = []
    for i in range(len(lines)):
        numbered_lines.append(str(i + 1) + ": " + lines[i])
    return numbered_lines

print(number(['a', 'b', 'c']))