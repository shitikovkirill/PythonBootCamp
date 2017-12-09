import argparse
from pbc_app.fibonacci import fibonacci_list
from pbc_app.numbers_pairs import contain_10


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Ran CLI application")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--fib", "-f", action='store_true', help="Run fibonacci function")
    group.add_argument("--contain", "-c", action='store_true', help="Run contain_10 function")
    group.add_argument(
        "--numbers", "-n",
        action='store', help="There are list numbers",
        nargs='+', type=int, required=True)
    args = parser.parse_args()

    if not args.fib and not args.contain:
        print ('Select one of the following flags: --fib or --contain')
    elif args.fib and args.contain:
        print ('You can not select this flags together: --fib with --contain')
    elif args.fib:
        if len(args.numbers) > 1:
            print('For run fibonacci function you mast use only one number in argument --numbers')
        else:
            print(fibonacci_list(args.numbers[0]))
    elif args.contain:
        print(contain_10(*args.numbers))
