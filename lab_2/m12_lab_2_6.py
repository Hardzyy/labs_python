def json_to_object(string):
    string = string.strip()
    if string == 'null':
        return None
    if string == 'false':
        return False
    if string == 'true':
        return True
    if string.isdigit() or (string[0] == '-' and string[1:].isdigit()):
        return json_to_int(string)
    if string.count('.') == 1 and string.count(' ') == 0:
        return float(string)
    if string[0] == "'" and string[-1] == "'":
        return json_to_str(string)
    if string[0] == "[" and string[-1] == "]":
        return json_to_list(string)
    if string[0] == '{' and string[-1] == '}':
        return json_to_dict(string)


def json_to_int(obj):
    if obj.isdigit():
        result = 0
        for num in obj:
            result += ord(num)-48
            result *= 10
        result //= 10
        return result
    if obj[0] == '-' and obj[1:].isdigit():
        return json_to_int(obj[1:]) * (-1)
    

def json_to_str(obj):
    return obj[1:-1]


def json_to_list(obj):
    if obj.count('[') == 1 and obj[0] == '[':
        string = obj[1:-1].split(', ')
        array = []
        for i in range(len(string)):
            array.append(json_to_object(string[i]))
        return array
    else:
        a = obj.split('[')
        left = []
        array = []
        right = []
        for i in range(len(a)):
            test = a[i].split(']')
            if type(test) is list and len(test) == 1:
                left.append(test)
            else:
                for x in range(len(test)):
                    if x == 0:
                        array.append(test[x])
                    else:
                        right.append(test[x])
        #------left---------------------------------------------
        left_final = []
        for i in range(len(left)):
            if left[i] != ['']:
                left_final.extend(left[i])
        felt = []
        for i in range(len(left_final)):
            felt.extend(left_final[i].split(', '))
        left_array = []
        for i in range(len(felt)):
            if felt[i] != '':
                left_array.append(json_to_object(felt[i]))
        #------left---------------------------------------------
        #------center---------------------------------------------
        new_array = []
        new_array = array[0].split(', ')
        last_array = []
        for i in range(len(new_array)):
            if new_array[i] != '':
                last_array.append(json_to_object(new_array[i]))
        #------center---------------------------------------------
        #------right---------------------------------------------
        end = []
        for i in range(len(right)):
            if right[i] != '':
                end.extend(right[i].split(', '))
        end_array = []
        for i in range(len(end)):
            if end[i] != '':
                end_array.append(json_to_object(end[i]))
        #------right---------------------------------------------
        result = []
        result.extend(left_array)
        result.append(last_array)
        result.extend(end_array)
        return result




def json_to_dict(dic):
    r = dic.find(':')
    t = json_to_object(dic[r+1:-1])
    fin_dict = {json_to_str(dic[1:r]): t}
    return fin_dict


d = 

print(json_to_object(d))
