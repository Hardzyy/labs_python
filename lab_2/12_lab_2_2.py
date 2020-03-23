import random

k = (10, 100)
kk = []
for i in range(k[0],k[1]):
    kk.append(i)

b = (3, 10)
bb = []
for i in range(b[0],b[1]):
    bb.append(i)
    
file = open("12_lab_2_2_output.txt", "w" )

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Enter size')
n = int(input())
length = random.choice(bb)
string_len = random.choice(kk)
spaces = 0
x = 0
str_help = 0

while x <= 1024**2 * n:
    if x != 0 and spaces !=0 and (spaces % (string_len) == 0):
        spaces = 0 
        file.write('\n')
        x += 1
        string_len = random.choice(kk)
    file.write(random.choice(alphabet))
    str_help += 1
    if str_help % length == 0:
        spaces += 1
        file.write(' ')
        x += 1
        length = random.choice(bb)
        str_help = 0
    x += 1  

file.close()

