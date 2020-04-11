import argparse


def exp_test(num):
    exponent = 0
    if num == 1:
        return 0
    while num:
        if num == 1:
            break
        if num % 2 == 0:
            exponent += 1
            num /= 2
        else:
            exponent = 0
            break
    if exponent != 0:
        return exponent
    else:
        return "not INTEGER"


def check_value(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid"
                                             "positive int value" % value)
        return ivalue


def without_arg():
    print("Enter INTEGER POSITIVE numbers one after one.")
    print("If you want stop print STOP.")
    while True:
        test_stop = input()
        if test_stop == 'stop' or test_stop == 'STOP':
            print("Work is over.")
            break
        try:
            num = int(test_stop)
            print("Integer exponent of 2 for", num, "is", exp_test(num))
        except:
            print("Number is wrong, please try again")


def main():
    parser = argparse.ArgumentParser(description='Created'
                                 'to get arguments from cmd')
    parser.add_argument(
        '--num',
        type=check_value,
        help='Enter a number to check the exp of 2.')

    args = parser.parse_args()
    number = args.num

    if number is None:
        without_arg()
    else:
        print("Integer exponent of 2 for", number, "is", exp_test(number))


if __name__ = "__main__":
    main()