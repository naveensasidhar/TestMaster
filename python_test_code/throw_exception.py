def remainder_division(a, b):
    if b == 0:
        raise ZeroDivisionError
    # To Generate customized exception error.
    # if b == 0:
    # raise Exception("Divisor cannot be 0")
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remainder", remainder)

    #Main program
    remainder_division(10, 3)