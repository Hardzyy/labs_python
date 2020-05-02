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


def bool_to_str(bl):
    if bl:
        return 'true'
    else:
        return 'false'


def float_to_str(fl):
    return str(fl)


def list_to_str(li):
    string = ''
    for i in range(len(li)):
        if type(li[i]) in (list, tuple):
            string += list_to_str(li[i]) + ', '
        if type(li[i]) is int:
            string += int_to_str(li[i]) + ', '
        if type(li[i]) is str:
            string += str_to_str(li[i]) + ', '
        if type(li[i]) is float:
            string += str(li[i]) + ', '
        if type(li[i]) is type(None):
            string += "null" + ', '
        if type(li[i]) is bool:
            string += bool_to_str(li[i]) + ', '
    return '[' + string[:-2] + ']'


def dict_to_str(di):


aa = [1,2.2,'ass', True, None, False, [1,1]]
print(list_to_str(aa))