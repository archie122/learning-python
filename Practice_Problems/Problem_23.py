def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:
        if flower2 % 2 == 0:
            return True
        else:
            return False
    else:
        return False

print(lovefunc(2,2))