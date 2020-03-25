import random
import progressbar
import argparse

class GenerateFile: 

    parser = argparse.ArgumentParser(description='Interactive input')
    parser.add_argument(
        '-n',
        default = 0.1,
        type = float,
        help = 'Size of a file(default: 0.1Mb)'
    )
    parser.add_argument(
        '--k',
        nargs='+',
        type = int,
        default = (10, 100),
        help = 'Amount of words in a string(default: (10, 100))'
    )
    
    parser.add_argument(
        '--l',
        nargs='+',
        type = int,
        default = (3, 10),
        help = 'Length of a word(default: (3, 10))'
    )

    args = parser.parse_args()
    k = tuple(args.k)
    kk = []
    for i in range(k[0],k[1]+1):
        kk.append(i)

    l = tuple(args.l)
    ll = []
    for i in range(l[0],l[1]+1):
        ll.append(i)
    
    file = open("12_lab_2_2_output.txt", "w")

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Enter size')
    n = args.n
    length = random.choice(ll)
    string_len = random.choice(kk)
    spaces = 0
    x = 0
    str_help = 0

    bar = progressbar.ProgressBar(maxval=int(1024**2 * n), widgets=[
        'Working...: ',
        progressbar.Bar(left='[', marker='|', right=']'),
       progressbar.SimpleProgress(),
    ]).start()

    while x <= int(1024**2 * n):
        if x != 0 and spaces !=0 and (spaces % (string_len) == 0):
            spaces = 0 
            file.write('\n')
            x += 2
            string_len = random.choice(kk)
        file.write(random.choice(alphabet))
        str_help += 1
        if str_help % length == 0:
            spaces += 1
            file.write(' ')
            x += 1
            length = random.choice(ll)
            str_help = 0
        x += 1
        bar.update(x)

    bar.finish()
    file.close()
    
GenerateFile()