import time
import random
import math

def sqrtSum(left, right):
    sum = 0
    block_left = int(left/sqrt_len)
    block_right = int(right/sqrt_len)
    if block_left == block_right:
        for i in range(left, right):
            sum += a[i]
    else: 
        for i in range(left, (block_left + 1)*sqrt_len-1 ):
            sum += a[i]
        for i in range(block_left+1, block_right-1):
            sum += b[i]
        for i in range(block_right*sqrt_len, right):
            sum += a[i]
    return sum

def elementSum(index1, index2):
    sum = 0
    for i in range(index1, index2):
        sum += a[i]
    return sum

print("Enter array size")
nArray = int(input())
start_time = time.time()
a = []
for i in range(0, nArray):
    a.append(i)
print(a)

b = []
sqrt_len = math.ceil(nArray**0.5)
print(sqrt_len)
for i in range(0,math.ceil(nArray/sqrt_len)):
    b.append(0)

for i in range(nArray):
    n = int(i / sqrt_len)
    b[n] += a[i]
print(b)

for i in range(0,10):
    rightBorder = random.randint(0,nArray-1)
    leftBorder = random.randint(0,rightBorder)
    print("leftBorder:", leftBorder)
    print("rightBorder:", rightBorder)
    print("elementSum:", elementSum(leftBorder,rightBorder))
    print("sqrtSum:", sqrtSum(leftBorder,rightBorder))
    if elementSum(leftBorder, rightBorder) == sqrtSum(leftBorder, rightBorder): 
        print("good")
    else: break 
    print("Step:", i)
print("Time",time.time()-start_time,"secs")



