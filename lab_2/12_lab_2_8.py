def exp_test(num):
	exponent = 0
	while num:
		if num == 1:
			break
		if num % 2 == 0:
			exponent += 1
			num /= 2
		else: 
			exponent = 0
			break
	if exponent != 0:
		return exponent
	else: 
		return "undefinite"

print("Exponent is", exp_test(17))