import time
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

for i in range(10000):
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



