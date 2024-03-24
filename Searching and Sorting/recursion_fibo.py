def get_fib(position):
    if position < 0 or isinstance(position, int) == False:
        return "'Position' must be an integer"
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print(get_fib(9))