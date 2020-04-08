import argparse


def flatten_it(a):
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

# parser = argparse.ArgumentParser(description='It helps me to do lab')
# parser.add_argument('--f',
#     help ="Enter JSON file name"
#     )
# args = parser.parse_args()
# array = args.a
# print(a)

array = [array, 12,312, array]
