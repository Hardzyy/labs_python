a = [1,2,23,[2,5,[6,4,123,1], 1231, 123,3123,[123123,123,123,[1231,123,[123,2]]]],23,1,231,2]
print(a)


def flatten_it(a):
	type_a = type(a)
	for i in range(len(a)):
		if type(a[i]) is type_a:
			b = a[i]
			del a[i]
			for k in range(len(b)):
				a.insert(i+k, b[k])
		count = 0
		for i in range(len(a)):
			if type(a[i]) is not type_a:
				count += 1
		if count == len(a):
			return a
	print(a)
	return flatten_it(a)

print(flatten_it(a))

# type_a = type(a)
# for i in range(len(a)):
# 	if type(a[i]) is type_a:
# 		b = a[i]
# 		for k in range(len(b)):
# 			a.insert(i+k, b[k])
# print(a)