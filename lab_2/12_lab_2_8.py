def exp_test(num):
    exponent = 0
    if num == 1:
        return 0
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
        return "indefinite"

for i in range(20):
    print("For", i, "exponent is", exp_test(i))
