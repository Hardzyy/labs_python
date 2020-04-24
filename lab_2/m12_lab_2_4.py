import argparse


def for_check(arr_type, types):
    return any([(arr_type is elem) for elem in types])



def check(a):
    type_a = type(a)
    list_a = list(a)
    types = [type(a), int, str, float, bool]
    for i in range(len(list_a)):
        if for_check(type(list_a[i]), types):
            pass
        else:
            raise ValueError('Your object cotsists of several types of structures.')            


def flatten_list(a):
    check(a)
    for i in range(len(a)):
        if type(a[i]) is list:
            b = a[i]
            del a[i]
            for k in range(len(b)):
                a.insert(i+k, b[k])
        count = 0
        for i in range(len(a)):
            if type(a[i]) is not list:
                count += 1
        if count == len(a):
            return a
    return flatten_it(a)


def flatten_tuple(a):
    check(a)
    list_a = list(a)
    for i in range(len(list_a)):
        if type(list_a[i]) is tuple:
            helper = list(list_a[i])
            del list_a[i]
            for k in range(len(helper)):
                list_a.insert(i+k, helper[k])
        count = 0
        for i in range(len(list_a)):
            if type(list_a[i]) is not tuple:
                count += 1
        if count == len(list_a):
            return tuple(list_a)
    return flat_tuple(tuple(list_a))


def flatten_it(a):
    if type(a) is list:
        return flatten_list(a)
    if type(a) is tuple:
        return flatten_tuple(a)
    else:
        print('Only lists and tuple are used')


def main():
    parser = argparse.ArgumentParser(description='Created to add objects')
    parser.add_argument('--obj',
        default='[1,2,[3,4,5],[6,[7,8]]]',
        type=str,
        help="Enter an object to flatten."
        )

    args = parser.parse_args()
    array = eval(args.obj)
    print('Original object', array)
    print('Flattened object', flatten_it(array))


if __name__ == "__main__":
    main()