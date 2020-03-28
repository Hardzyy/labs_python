import argparse


def without_arg():
    print("Enter INTEGER POSITIVE numbers one after one.")
    print("If you want stop print STOP.")
    while True:
        test_stop = input()
        if test_stop == 'stop' or test_stop == 'STOP':
            print("Work is over.")
            break
        try:
            num = int(test_stop)
            print("Leonardo number for", num, "is", leonardo_num(num))
        except:
            print("Number is wrong, please try again")


def check_value(value):
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue


def leonardo_num(n):
    if n == 0 or n == 1:
        return 1
    fi = (1 + 5**0.5)*0.5
    phi = (1 - 5**0.5)*0.5
    leo = (2 / 5**0.5) * (fi**(n+1) - phi**(n-1)) - 1 
    return round(leo)

parser = argparse.ArgumentParser(description="Created to gets args from cmd")
parser.add_argument(
	'--num',
	type = check_value,
	help = 'Enter a number to calculate Leonardo'
	)

args = parser.parse_args()
number = args.num

if number is None:
	without_arg()	
else: 
	print('Leonardo number for', number, 'is', leonardo_num(number))