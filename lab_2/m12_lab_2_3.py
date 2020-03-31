import argparse


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


file = open('Test.txt', 'r')
ff = file.read().split('\n')
file.close()
sorted_ff = mergesortStr(ff)

ffe = open('text.txt', 'w')
for i in range(len(sorted_ff)):
	ffe.write(sorted_ff[i])
	if i < len(sorted_ff) - 1:
		ffe.write('\n')

ffe.close()
