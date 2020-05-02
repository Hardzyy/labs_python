import argparse


def to_json(obj):
    if type(obj) is int:
        return int_to_str(obj)
    if type(obj) is float:
        return float_to_str(obj)
    if type(obj) in (list, tuple):
        return list_to_str(obj)
    if type(obj) is dict:
        return dict_to_str(obj)
    if type(obj) is bool:
        return bool_to_str(obj)
    if type(obj) is str:
        return str_to_str(obj)
    if type(obj) is type(None):
        return none_to_str(obj)


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
    return "\'" + string + "\'"


def bool_to_str(bl):
    if bl:
        return 'true'
    else:
        return 'false'


def none_to_str(obj):
    return 'null'


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
            string += none_to_str(obj) + ', '
        if type(li[i]) is bool:
            string += bool_to_str(li[i]) + ', '
        if type(li[i]) is dict:
            string += dict_to_str(li[i]) + ', '
    return '[' + string[:-2] + ']'


def dict_to_str(di):
    string = ''
    for key, value in di.items():
        if type(key) in (str, int, float, type(None), bool):
            string += to_json(key) + ': '
        else:
            raise ValueError
        string += to_json(value) + ', '
    return '{' + string[:-2] + '}'


def main():
    parser = argparse.ArgumentParser(description='Argument parser for lab')
    parser.add_argument(
        '--file',
        default='file.txt',
        help='Enter a file name in witch to write a json string. With extension(file.txt)'
        )
    args = parser.parse_args()

    file_name = args.file
    file = open(file_name, 'w')
    obj = 
    file.write(to_json(obj))
    file.write('\n')
    file.close()


if __name__ == '__main__':
    main()