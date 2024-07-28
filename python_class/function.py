def my_abs(x):
    """
    return absolute value of x
    :param x: input number, must be number
    :return: return absolute value of x
    """
    if x < 0:
        return -x

    return x


def new_abs(x: int) -> int:
    """
    return absolute value of x
    :param x: input number, must be number
    :return: return absolute value of x
    """
    if x < 0:
        return -x

    return x


print(my_abs(-5))
print(new_abs(-5))
