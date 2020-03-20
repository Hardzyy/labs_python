a = [1,2,23,[2,5,[6,4,123,1], 1231, 123,3123,[123123,123,123,[1231,123,[123,2]]]],23,1,231,2]
print(a)


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
# print(flatten_it(a))

b = (12,3123,123,(123,123,123,123),12,31,3,(123,(31231,12312)))


def func(b):
    y = []
    y = list(b).copy()
    print(y)
    type_b = type(b)
    print(type_b)

    for i in range(len(y)):
        if type(y[i]) is type_b:
            z = list(y[i])
            print(z)
            del y[i]
            for k in range(len(z)):
                y.insert(i+k, z[i])
        count = 0
        for i in range(len(y)):
            if type(y[i]) is not type_b:
                count += 1
        print(count)
        print(len(y))
        if count == len(y):
            return y
    return func(y)
    
print(func(b))

# type_a = type(a)
# for i in range(len(a)):
#   if type(a[i]) is type_a:
#       b = a[i]
#       for k in range(len(b)):
#           a.insert(i+k, b[k])
# print(a)