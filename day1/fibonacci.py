def fibonacci(number):
    """
    Gives fibonacci number by their position.
    This function use recursive method for getting fibonacci number.
    :param number:
    :return:
    """
    if number == 0:
        return 0
    elif number == 1 or number == -1:
        return 1
    elif number < 0:
        result = fibonacci(number + 2) - fibonacci(number + 1)
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)
    return result


def get_fibonacci_list(number):
    """
    Get list of fibonacci numbers
    This is slow method to get fibonacci list
    :param number:
    :return:
    """

    result = []
    if number >= 0:
        for i in range(number+1):
            result.append(fibonacci(i))
    else:
        for i in reversed(range((number-1)*-1)):
            result.append(fibonacci(i*-1))
    return result


def fibonacci_generator(negative=False):
    """
    Get fibonacci generator
    :return:
    """
    previous_value = 0
    current_value = 1
    yield previous_value
    yield current_value
    while True:
        tmp_current_value = int(current_value)
        if not negative:
            current_value = current_value + previous_value
        else:
            current_value = previous_value - current_value
        previous_value = tmp_current_value
        yield current_value


def get_fibonacci_xrange(number):
    """
    Get fibonacci list using generators
    :param number:
    :return:
    """
    counter = int(number)
    result = []
    if number >= 0:
        fg = fibonacci_generator()
    else:
        fg = fibonacci_generator(True)

    result.append(fg.next())

    while counter:
        result.append(fg.next())
        if counter > 0:
            counter -= 1
        elif counter < 0:
            counter += 1

    if number < 0:
        result.reverse()
    return result


if __name__ == '__main__':

    print(get_fibonacci_list(13))
    print(get_fibonacci_list(-13))

    print(get_fibonacci_xrange(13))
    print(get_fibonacci_xrange(-13))
