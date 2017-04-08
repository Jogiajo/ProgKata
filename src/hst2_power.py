def power(a, b):
    if b == 0:
        return 1;
    elif b == 1:
        return a;
    elif (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Argument must be integer or float")
    else:
        return a * power(a, b - 1)

print (power(2, 3))