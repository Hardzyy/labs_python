import math 

# def to_json(obj):
#     if isinstance(obj, int):

def int_to_str(integer):
    string = ''
    while True:
        remainder = integer%10
        string = chr(ord('0')+remainder)+string
        integer //= 10
        if integer == 0:
            break
    return string

def str_to_str(string):
    return "\"" + string + "\""


def list_to_str(li):
    string = ','.join(str(elem) for elem in li)
    return '[{}]'.format(string)

aa = [1,1,1]
print(list_to_str(aa))