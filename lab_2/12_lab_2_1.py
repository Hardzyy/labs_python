#Работа Корбовского Никиты Андреевича
#        karbovskiyma@gmail.com
#1)чтобы программа отработала в интерактивном режиме
#  следует ее поросто выполнить
#2) чтобы программа отработала в режиме работы 
#   с файлом нужно: в командной стороке добавить 
#   аргумент --f ИМЯ ФАЙЛА 
#   пример файла привиден на GitHub
#   под названием 12_lab_2_1_file.txt
#   структура файла проста: 
#   1-ая сторока - массив
#   остальные - границы
#   также предусмотрен контроль ввода границ
import math
import argparse


def sqrtSum(a, left, right):
    sqrt_len = math.ceil(len(a) ** 0.5)
    help_array = []
    for i in range(0, math.ceil(len(a) / sqrt_len)):
        help_array.append(0)

    for i in range(len(a)):
        n = int(i / sqrt_len)
        help_array[n] += a[i]

    sum = 0
    i = left
    while i < right:
        if (i % sqrt_len == 0) and (i + sqrt_len - 1 < right):
            sum += help_array[int(i / sqrt_len)]
            i += sqrt_len
        else:
            sum += a[i]
            i += 1
    return sum


def without_file():
    print('To stop array print STOP.')
    print("Enter array:")
    a = []
    truth = 1
    while truth:
        c = input()
        if c == "stop" or c == "STOP":
            truth = 0
        else:
            try:
                a.append(int(c))
            except:
                print("Sorry, but you enter wrong one,"
                      "plese try again or enter STOP")

    print('Well done! Your array:', a)
    print("Now enter left and right borders! And remember: left < right !")
    print("To stop print STOP.")
    truth = 1
    while truth:
        print("Left:")
        left = input()
        if left == 'stop' or left == "STOP":
            break
        print("Right:")
        right = input()
        if right == 'stop' or right == 'STOP':
            break
        try:
            left1 = int(left)
            right1 = int(right)
            if right1 >= left1 and left1 >= 0:
                print("Sum of elements from ", left1, " till ",
                      right1, "is equal", sqrtSum(a, left1, right1))
            else:
                print("Borders are wrong! Please try again!")
        except:
                print("Sorry, but you enter wrong one,"
                      "plese try again or enter STOP")


def with_file():
    file = open(name_file, 'r')
    str_amoung = file.read().strip().count('\n')
    file.close()
    file = open(name_file, 'r')
    a = [int(elem) for elem in file.readline().strip().split(' ')]
    print(a)
    for i in range(str_amoung):
        b = [int(elem) for elem in file.readline().strip().split(' ')]
        print(b)
        if len(a) >= b[1] >= b[0] >= 0:
            print("Elemet sum:", sqrtSum(a, b[0], b[1]))
        else:
            print("Sorry but it's wrong!")
    file.close()

parser = argparse.ArgumentParser(description='It helps me to do lab')
parser.add_argument('--f')
args = parser.parse_args()
name_file = args.f

if name_file is None:
    without_file()
else:
    with_file()

print('Work is over, thanks for watching :)')
