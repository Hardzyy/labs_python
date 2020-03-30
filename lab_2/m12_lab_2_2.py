import random
import progressbar
import argparse
import time

def check_dimension(array):
    if len(array) != 2:
        print("Wrong tuple")
        print("Program is ended")
        quit()


def check_tuple(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def check_size(value):
    fvalue = float(value)
    if fvalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive float value" % value)
    return fvalue


parser = argparse.ArgumentParser(description='Interactive input')
parser.add_argument(
    '-n',
    default = 1,
    type = check_size,
    help = 'Size of a file(default: 1Mb)'
)
parser.add_argument(
    '--k',
    nargs='+',
    type = check_tuple,
    default = (10, 100),
    help = 'Amount of words in a string(default: (10, 100))'
)
    
parser.add_argument(
    '--l',
    nargs='+',
    type = check_tuple,
    default = (3, 10),
    help = 'Length of a word(default: (3, 10))'
)

args = parser.parse_args()
k = tuple(args.k)
kk = []
for i in range(k[0],k[1]+1):
    kk.append(i)
check_dimension(k)

l = tuple(args.l)
ll = []
for i in range(l[0],l[1]+1):
    ll.append(i)
check_dimension(l)
    
file = open("12_lab_2_2_output.txt", "w")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = args.n
length = random.choice(ll)
string_len = random.choice(kk)
spaces = 0
x = 0
str_help = 0

bar = progressbar.ProgressBar(maxval=int(1024**2 * n + 1), widgets=[
    'Working...: ',
    progressbar.Bar(left='[', marker='*', right=']'),
    progressbar.Percentage(),
]).start()

start_time = time.time()

while x <= int(1024**2 * n - 1):
    if x != 0 and spaces !=0 and (spaces % (string_len) == 0):
        spaces = 0 
        file.write('\n')
        x += 2
        string_len = random.choice(kk)
    file.write(random.choice(alphabet))
    x += 1        
    str_help += 1
    if str_help % length == 0:
        spaces += 1
        file.write(' ')
        x += 1
        length = random.choice(ll)
        str_help = 0
    bar.update(x)

bar.finish()
file.close() 
print("Total time complexity", (time.time() - start_time))