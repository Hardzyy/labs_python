import random
import progressbar
import argparse
import time


def checkDimension(array):
    if len(array) != 2:
        print("Wrong tuple")
        print("Program is ended")
        quit()


def checkTuple(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid"
                                         "positive int value" % value)
    return ivalue


def checkSize(value):
    fvalue = float(value)
    if fvalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid"
                                         "positive float value" % value)
    return fvalue


parser = argparse.ArgumentParser(description='Interactive input')
parser.add_argument(
    '-n',
    default=1,
    type=checkSize,
    help='Size of a file(default: 1Mb)'
)
parser.add_argument(
    '--k',
    nargs='+',
    type=checkTuple,
    default=(10, 100),
    help='Amount of words in a string(default: (10, 100))'
)

parser.add_argument(
    '--l',
    nargs='+',
    type=checkTuple,
    default=(3, 10),
    help='Length of a word(default: (3, 10))'
)

args = parser.parse_args()
k = tuple(args.k)
rand_for_str = []
for i in range(k[0], k[1]+1):
    rand_for_str.append(i)
checkDimension(k)

l = tuple(args.l)
rand_for_word = []
for i in range(l[0], l[1]+1):
    rand_for_word.append(i)
checkDimension(l)

file = open("output.txt", "w")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = args.n
length = random.choice(rand_for_word)
string_len = random.choice(rand_for_str)
spaces = 0
size_in_bytes = 0
str_help = 0

bar = progressbar.ProgressBar(maxval=int(1024**2 * n + 1), widgets=[
    'Working...: ',
    progressbar.Bar(left='[', marker='*', right=']'),
    progressbar.Percentage(),
]).start()

start_time = time.time()

while size_in_bytes < int(1024**2 * n):
    if size_in_bytes != 0 and spaces != 0 and (spaces % (string_len) == 0):
        spaces = 0
        file.write('\n')
        size_in_bytes += 2
        string_len = random.choice(rand_for_str)
    file.write(random.choice(alphabet))
    size_in_bytes += 1
    str_help += 1
    if str_help % length == 0:
        spaces += 1
        file.write(' ')
        size_in_bytes += 1
        length = random.choice(rand_for_word)
        str_help = 0
    bar.update(size_in_bytes)

bar.finish()
file.close()
print("Total time complexity", (time.time() - start_time))
