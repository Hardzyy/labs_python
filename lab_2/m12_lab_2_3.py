import os
import time
import random
import argparse
import datetime
import progressbar


def createFile(file_name, n, rand_for_word, rand_for_str):
    file = open(file_name +'.txt', 'w')

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    length = random.choice(rand_for_word)
    string_len = random.choice(rand_for_str)
    spaces = 0
    size_in_bytes = 0
    str_help = 0

    while size_in_bytes < int(1024**2 * n) - 1:
        if size_in_bytes != 0 and spaces != 0 and (spaces % (string_len) == 0):
            spaces = 0
            file.write('\n')
            size_in_bytes += 2
            string_len = random.choice(rand_for_str)
        file.write(random.choice(alphabet))
        size_in_bytes += 1
        str_help += 1
        if str_help % length == 0:
            spaces += 1
            file.write(' ')
            size_in_bytes += 1
            length = random.choice(rand_for_word)
            str_help = 0
    file.close()


def checkDimension(array):
    if len(array) != 2:
        print("Wrong tuple")
        print("Program is ended")
        quit()


def checkTuple(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid"
                                         "positive int value" % value)
    return ivalue


def checkSize(value):
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


def main():
    parser = argparse.ArgumentParser(description='Argument parser for lab')
    parser.add_argument(
        '--cr',
        help='Write here FILE NAME if you wanna create sorted file.' +
            '\n' + 'When you use it look for N,K,L argumnts.'
        )
    parser.add_argument(
        '--sort',
        help='Name of a file wich will be sorted.'
        )
    parser.add_argument(
        '-n',
        default=1,
        type=checkSize,
        help='Size of a file(default: 1Mb)'
    )
    parser.add_argument(
        '--k',
        nargs='+',
        type=checkTuple,
        default=(10, 100),
        help='Amount of words in a string(default: (10, 100))'
    )
    parser.add_argument(
        '--l',
        nargs='+',
        type=checkTuple,
        default=(3, 10),
        help='Length of a word(default: (3, 10))'
    )

    args = parser.parse_args()

    name_sort = args.sort
    n = args.n
    create = args.cr
    k = tuple(args.k)
    rand_for_str = []
    for i in range(k[0], k[1]+1):
        rand_for_str.append(i)
    checkDimension(k)

    l = tuple(args.l)
    rand_for_word = []
    for i in range(l[0], l[1]+1):
        rand_for_word.append(i)
    checkDimension(l)

    if create is not None:
        createFile(create, n, rand_for_word, rand_for_str)

        file = open(create+'.txt', 'r')
        ff = file.read().split('\n')
        file.close()
        sorted_ff = mergesortStr(ff)

        ffe = open(create+'.txt', 'w')
        for i in range(len(sorted_ff)):
            merge_and_split = mergesortWord(sorted_ff[i].split())
            merge_and_split.append('')
            string_done =  ' '.join(elem for elem in merge_and_split)
            ffe.write(string_done)
            if i < len(sorted_ff) - 1:
                ffe.write('\n')
        ffe.close()

    if name_sort is not None:
        file = open(name_sort+'.txt', 'r')
        ff = file.read().split('\n')
        file.close()
        sorted_ff = mergesortStr(ff)

        ffe = open(name_sort+'_sorted'+'.txt', 'w')

        for i in range(len(sorted_ff)):
            ffe.write(sorted_ff[i])
            if i < len(sorted_ff) - 1:
                ffe.write('\n')
        ffe.close()

if __name__ == "__main__":
    main()