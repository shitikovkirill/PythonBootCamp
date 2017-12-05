def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1 or number == -1:
        return 1
    elif number < 0:
        result = fibonacci(number + 2) - fibonacci(number + 1)
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)
    return result


def get_fibonacci_range(number):
    result = []
    if number >= 0:
        for i in range(number):
            result.append(fibonacci(i))
    else:
        for i in reversed(range(number*-1)):
            result.append(fibonacci(i*-1))
    return result


if __name__ == '__main__':
    print(get_fibonacci_range(13))
    print(get_fibonacci_range(-13))
