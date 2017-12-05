def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)
        return result
