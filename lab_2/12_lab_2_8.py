num = int(input())

exponent = 0
while num:
	if num == 1:
		break
	if num % 2 == 0:
		num /= 2
	else: 
		break
