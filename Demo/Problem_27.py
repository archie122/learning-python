def expanded_form(num):
    x = [int(i) for i in str(num)]
    result = ""
    for i in range(len(x)):
        if x[i] != 0:  # Check if the current digit is zero
            if result != "":
                result += " + "
            result += str(x[i] * pow(10, len(x) - i - 1))
    return result


print(expanded_form(658610))