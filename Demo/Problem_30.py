def tribonacci(signature, n):
    x, y, z = signature[0], signature[1], signature[2]

    if n == 0:
        return []
    if n == 1:
        return [x]
    if n == 2:
        return [x, y]

    for i in range(3, n):
        temp = x + y + z
        x = y
        y = z
        z = temp
        signature.append(temp)

    return signature


print(tribonacci([1, 1, 1], 2))
