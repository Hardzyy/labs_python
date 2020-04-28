import os
import random
import datetime


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
    file_size = (os.path.getsize(f_name)) / 1024**2 
    count_file = count(f_name[:-4])
    if file_size > 100:
        divided_count = int(count_file/2)
        file_1name = create_file_name()
        file_1 = open(file_1name+'.txt', 'w')
        file_origin = open(f_name, 'r')
        for i in range(divided_count):
            if i != divided_count - 1:
                file_1.write(file_origin.readline())
            else:
                file_1.write(file_origin.readline()[:-1])            
        file_1.close()
        file_2name = create_file_name()
        file_2 = open(file_2name+'.txt', 'w')
        for i in range(divided_count, count_file):
            file_2.write(file_origin.readline())    
        file_2.close()
        file_origin.close()
        name_array = []
        name_array.append(file_1name)
        name_array.append(file_2name)
        return name_array
    else:
        return None


def recurison(name_arr):
    new_name_arr = []
    namespace = []
    for i in range(len(name_arr)):
        new_name_arr.extend(divide_file(name_arr[i]))
    for i in range(len(name_arr)):
        os.remove(name_arr[i]+'.txt')
    namespace.extend(new_name_arr)
    if (os.path.getsize(new_name_arr[0]+'.txt')) / 1024**2 > 100:
        return recurison(new_name_arr)
    else:
        return namespace


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


new_namespace = recurison(divide_file('Test'))

sorted_namespace = []
for i in range(len(new_namespace)):
    sorted_namespace.append(sort_file(new_namespace[i]))

recursion_merge(sorted_namespace)
    