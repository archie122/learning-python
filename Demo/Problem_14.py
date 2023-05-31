def problem(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in n.lower():
            return False
    return True


print(problem("abcdefghijklmnopqrstuvwxyz"))
print(problem("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(problem("0123456789"))
print(problem("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
print(problem("the quick brown fox jumps over the lazy dog"))
