import random
import math

def sqrtSum(left, right):
    sum = 0
    i = left
    while i < right:
        if  (i % sqrt_len == 0) and (i + sqrt_len - 1 < right):
            sum += b[int(i / sqrt_len)]
            i += sqrt_len
        else: 
            sum += a[i]
            i += 1  
    return sum

def elementSum(index1, index2):
    sum = 0
    for i in range(index1, index2):
        sum += a[i]
    return sum

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
            print("Sorry, but you enter wrong one, plese try again or enter STOP")

print('Well done! Your array:', a)

sqrt_len = math.ceil(len(a) ** 0.5)
b = []
for i in range(0,math.ceil(len(a) / sqrt_len)):
    b.append(0)

for i in range(len(a)):
    n = int(i / sqrt_len)
    b[n] += a[i]

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
            print("Sum of elements from ",left1," till ", right1, "is equal", sqrtSum(left1,right1))
        else: print("Borders are wrong! Please try again!")
    except:
            print("Sorry, but you enter wrong one, plese try again or enter STOP")
print('Work is over, thanks for watching :)')


# for i in range(10000):
#     rightBorder = random.randint(0,len(a)-1)
#     leftBorder = random.randint(0,rightBorder)
#     print("leftBorder:", leftBorder)
#     print("rightBorder:", rightBorder)
#     print("elementSum:", elementSum(leftBorder,rightBorder))
#     print("sqrtSum:", sqrtSum(leftBorder,rightBorder))
#     if elementSum(leftBorder, rightBorder) == sqrtSum(leftBorder, rightBorder): 
#         print("good")
#     else: break 
#     print("Step:", i)


# for i in range(10000):
#     rightBorder = random.randint(0,len(a)-1)
#     leftBorder = random.randint(0,rightBorder)
#     print("sqrtSum:", sqrtSum(leftBorder,rightBorder))

# for i in range(10000):
#     rightBorder = random.randint(0,len(a)-1)
#     leftBorder = random.randint(0,rightBorder)
#     print("sqrtSum:", elementSum(leftBorder,rightBorder))







