
def json_to_object(string):
	string = string.strip()
	if string = 'null':
		return None
	if string = 'false':
		return False
	if string = 'true':
		return True
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
		array.append(json_to_object(string[i]))
	return array


f = open('111.txt', 'r')
for i in range(3):
	obj = json_to_object(f.readline())
	print(obj, type(obj))
