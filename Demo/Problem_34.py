def double_char(s):
    double = ""
    for i in range(len(s)):
        double += s[i] + s[i]
    return double


print(double_char("Hello"))
