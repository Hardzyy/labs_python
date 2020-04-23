import argparse


def flatten_list(a):
    type_a = type(a)
    for i in range(len(a)):
        if type(a[i]) is type_a:
            b = a[i]
            del a[i]
            for k in range(len(b)):
                a.insert(i+k, b[k])
        count = 0
        for i in range(len(a)):
            if type(a[i]) is not type_a:
                count += 1
        if count == len(a):
            return a
    return flatten_it(a)


def flatten_tuple(a):
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


def main():
    parser = argparse.ArgumentParser(description='It helps me to do lab')
    parser.add_argument('--obj',
        type=str,
        help="Enter an object to flatten."
        )
    
    args = parser.parse_args()
    array = eval(args.obj)
    print(flatten_it(array))

if __name__ == "__main__":
    main()
