import argparse


def contain_10(*args):
    """
    This script prints pairs of numbers which sum is = 10 for a given collection of numbers
    :param args:
    :return:
    """
    args = [number for number in args if number < 10]
    list_args = sorted(args, reverse=True)
    result = []
    while list_args:
        first_number = list_args.pop()
        for second_number in list_args:
            if first_number + second_number == 10 and (first_number, second_number) not in result:
                result.append((first_number, second_number))

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This script prints pairs of numbers which sum is = 10 for a given collection of numbers")
    group = parser.add_argument_group("Parameters")
    group.add_argument(
        "--numbers", "-n",
        action='store', help="There are list numbers",
        nargs='+', type=int, required=True)
    args = parser.parse_args()
    print(contain_10(*args.numbers))
