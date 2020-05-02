file = open('file.txt', 'r')
aa = file.readline()
file.close()
print(aa)

def json_to_object(string):
	string = string.strip()
	if string[0] == "'" and string[-1] == "'":
		return json_to_str(string)
	if string.count('.') == 1 and string.count(' ') == 0:
		return float(string)
	if string[0] == "[" and string[-1] == "]":
		return json_to_list(string)



def json_to_str(obj):
	return obj[1:-1]


def json_to_list(obj):
	string = obj[1:-1].split(', ')
	array = []
	for i in range(len(string)):
		array.extend(json_to_object(string))
	return array