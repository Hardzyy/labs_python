a = [1,2,23,[2,5,[6,4,123,1,23,1,231,2]],1,[12,31,12312,[12,123,123,3]],1]


def flatten_it(a):
	for i in range(len(a)):
		if type(a[i]) is list:
			b = a[i]
			del a[i]
			for k in range(len(b)):
				a.insert(i+k, b[k])
		count = 0
		if type(a[i]) is not list:
			count += 1
		if count == len(a):
			return a
	return a

print(flatten_it(a))
aa = flatten_it(a)
print(flatten_it(aa), len(aa))		