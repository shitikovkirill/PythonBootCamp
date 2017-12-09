import argparse
from log import arguments_log


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


@arguments_log
def fibonacci_list(number):
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
    parser = argparse.ArgumentParser(description="This script print fibonacci numbers")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--number", "-n", action='store', help="A number to print", type=int, required=True)
    args = parser.parse_args()
    print(fibonacci_list(args.number))
