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
    bar = progressbar.ProgressBar(maxval=int(1024**2 * n + 1), widgets=[
        'Creating file...: ',
        progressbar.Bar(left='[', marker='*', right=']'),
        progressbar.Percentage(),
    ]).start()

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
        bar.update(size_in_bytes)

    bar.finish()
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


def file_name_check(file_name):
    if type(file_name) is str:
        return file_name+'.txt'
    else:
        return file_name.name


def create_file_name():
    get_info = datetime.datetime.now()
    get_data = str(get_info).split(' ')[0]
    get_minute = str(get_info.minute)
    get_second = str(get_info.second)
    name = get_data+'.'+get_minute+'.'+get_second
    return name


def count(file_name):
    f_name = file_name_check(file_name)
    file = open(f_name, 'r')
    count = 0
    for line in file:
        count += 1
    file.close()
    return count


def divide_file(file_name):
    f_name = file_name_check(file_name)
    count_file = count(f_name[:-4])
    bar = progressbar.ProgressBar(maxval=int(count_file + 1), widgets=[
        'Dividing file...: ',
        progressbar.Bar(left='[', marker='*', right=']'),
        progressbar.Percentage(),
    ]).start()
    file_size = (os.path.getsize(f_name)) / 1024**2 
    if file_size > 200:
        divided_count = int(count_file/2)
        file_1name = create_file_name()
        file_1 = open(file_1name+'.txt', 'w')
        file_origin = open(f_name, 'r')
        for i in range(divided_count):
            if i != divided_count - 1:
                file_1.write(file_origin.readline())
            else:
                file_1.write(file_origin.readline()[:-1])
            bar.update(i)
        file_1.close()
        file_2name = create_file_name()
        file_2 = open(file_2name+'.txt', 'w')
        for i in range(divided_count, count_file):
            file_2.write(file_origin.readline())
            bar.update(i)
        file_2.close()
        file_origin.close()
        name_array = []
        name_array.append(file_1name)
        name_array.append(file_2name)
        return name_array
    else:
        return file_name


def recurison(name_arr):
    new_name_arr = []
    namespace = []
    if type(name_arr) is str:
        return name_arr
    else:
        for i in range(len(name_arr)):
            new_name_arr.extend(divide_file(name_arr[i]))

    for i in range(len(name_arr)):
        os.remove(name_arr[i]+'.txt')
    namespace.extend(new_name_arr)
    if (os.path.getsize(new_name_arr[0]+'.txt')) / 1024**2 > 200:
        return recurison(new_name_arr)
    else:
        return namespace


def sort_file(file_name):
    file = open(file_name+'.txt', 'r')
    array_str = file.read().split('\n')
    file.close()
    sorted_array_str = mergesortStr(array_str)

    sorted_file = open(file_name+'_sorted'+'.txt', 'w')

    for i in range(len(sorted_array_str)):
        sorted_file.write(sorted_array_str[i])
        sorted_file.write('\n')
    sorted_file.close()
    os.remove(file_name+'.txt')
    return file_name+'_sorted'        


def merge_files(file_name1, file_name2):
    merged_file_name = create_file_name()+'_sorted'+'.txt'
    merged_file = open(merged_file_name,'w')
    file1 = open(file_name1+'.txt', 'r')
    str1 = file1.readline()
    file2 = open(file_name2+'.txt', 'r')
    str2 = file2.readline()
    count1 = count(file_name1)
    count2 = count(file_name2)
    counter = 0
    while counter < count1 + count2:
        if str1 == '' and str2 != '':
            merged_file.write(str2)
            str2 = file2.readline()
        if str2 == '' and str1 != '':
            merged_file.write(str1)
            str1 = file1.readline()
        if len(str1) < len(str2):
            merged_file.write(str1)
            str1 = file1.readline()
        else:
            merged_file.write(str2)
            str2 = file2.readline()
        counter  += 1
    merged_file.close()
    file1.close()
    file2.close()
    return merged_file_name[:-4]


def recursion_merge(sorted_namespace):
    if len(sorted_namespace) == 1:
        return sorted_namespace
    else:
        total_name = []
        arange = range(len(sorted_namespace))[::2]
        merged_space =[]
        for i in arange:
            merged_space.append(merge_files(sorted_namespace[i], sorted_namespace[i+1]))
        for i in range(len(sorted_namespace)):
            os.remove(sorted_namespace[i]+'.txt')
        return recursion_merge(merged_space)


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
        start_time = time.time()
        createFile(create, n, rand_for_word, rand_for_str)

        new_namespace = recurison(divide_file(create))
        if type(new_namespace) is str:
            sorted_file = sort_file(new_namespace)
        else:
            sorted_namespace = []
            for i in range(len(new_namespace)):
                sorted_namespace.append(sort_file(new_namespace[i]))
            sorted_file = recursion_merge(sorted_namespace)

        sort = open(sorted_file+'.txt', 'r')
        file = open(create+'.txt', 'w')
        counter = count(sorted_file)
        arange = range(counter)
        for i in arange:
            line = sort.readline()
            sorted_line = mergesortWord(line.split())
            sorted_line.append('')
            string_done = ' '.join(elem for elem in sorted_line)
            file.write(string_done)
            if i < counter - 1:
                file.write('\n')
        file.close()
        sort.close()
        os.remove(sorted_file+'.txt')
        print("Total time complexity", (time.time() - start_time))

    if name_sort is not None:
        new_namespace = recurison(divide_file(name_sort))
        if type(new_namespace) is str:
            sort_file(new_namespace)
        else:
            sorted_namespace = []
            for i in range(len(new_namespace)):
                sorted_namespace.append(sort_file(new_namespace[i]))
            recursion_merge(sorted_namespace)

if __name__ == "__main__":
    main()