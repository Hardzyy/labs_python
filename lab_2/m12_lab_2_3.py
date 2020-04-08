import argparse


def check_dimension(array):
    if len(array) != 2:
        print("Wrong tuple")
        print("Program is ended")
        quit()


def check_tuple(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid"
                                         "positive int value" % value)
    return ivalue


def check_size(value):
    fvalue = float(value)
    if fvalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid"
                                         "positive float value" % value)
    return fvalue


def mergeStr(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result

 
def mergesortStr(list):
    if len(list) < 2:
        return list
 
    middle = int(len(list)/2)
    left = mergesortStr(list[:middle])
    right = mergesortStr(list[middle:])
 
    return mergeStr(left, right)


def mergeWord(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def mergesortWord(list):
    if len(list) < 2:
        return list
 
    middle = int(len(list)/2)
    left = mergesortWord(list[:middle])
    right = mergesortWord(list[middle:])
 
    return mergeWord(left, right)


parser = argparse.ArgumentParser(description='Argument parser for lab')
parser.add_argument(
    '--cr',
    default='file',
    help='Write here FILE NAME if you wanna create sorted file.'
    )
parser.add_argument(
    '--sort',
    help='Name of a file wich will be sorted.'
    )
parser.add_argument(
    '-n',
    default=1,
    type=check_size,
    help='Size of a file(default: 1Mb)'
)
parser.add_argument(
    '--k',
    nargs='+',
    type=check_tuple,
    default=(10, 100),
    help='Amount of words in a string(default: (10, 100))'
)
parser.add_argument(
    '--l',
    nargs='+',
    type=check_tuple,
    default=(3, 10),
    help='Length of a word(default: (3, 10))'
)

args = parser.parse_args()

k = tuple(args.k)
kk = []
for i in range(k[0], k[1]+1):
    kk.append(i)
check_dimension(k)

l = tuple(args.l)
ll = []
for i in range(l[0], l[1]+1):
    ll.append(i)
check_dimension(l)
create = args.cr
if create is not None:


    file = open('output.txt', 'r')
    ff = file.read().split('\n')
    file.close()
    sorted_ff = mergesortStr(ff)

    ffe = open(create+'.txt', 'w')
    for i in range(len(sorted_ff)):
        merge_and_split = mergesortWord(sorted_ff[i].split(' '))
        string_done =  ' '.join(elem for elem in merge_and_split)
        ffe.write(sorted_ff[i])
        if i < len(sorted_ff) - 1:
            ffe.write('\n')
    ffe.close()