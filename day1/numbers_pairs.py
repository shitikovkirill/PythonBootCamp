def contain_10(*args):
    list_args = sorted(list(args), reverse=True)
    result = []
    while list_args:
        first_number = list_args.pop()
        for second_number in list_args:
            if first_number + second_number == 10 and (first_number, second_number) not in result:
                result.append((first_number, second_number))

    return result


if __name__ == '__main__':
    print(contain_10(1, 2, 3, 4, 5, 5, 6))
