import time
import random

print("Enter array size")
nArray = int(input())
start_time = time.time()
a = []
for i in range(0, nArray):
    a.append(i)
print(a)

def elementSum(index1, index2):
    sum = 0
    for i in range(index1, index2):
        sum += a[i]
    return sum

# n = int(input())
# for i in range(1):
#     rightBorder = random.randint(0,nArray-1)
#     leftBorder = random.randint(0,rightBorder)
#     print("leftBorder: ", leftBorder, "rightBorder:", rightBorder)
#     print(elementSum(leftBorder, rightBorder)==1)
#     print("Step:", i)
# print("Time",time.time()-start_time,"secs")
b = []
sqrt_len = int(nArray**0.5 + 1)
print("sqrt lem:", sqrt_len)
for i in range(0,int(nArray/sqrt_len + 1)):
    b.append(0)

for i in range(nArray):
    n = int(i / sqrt_len)
    b[n] += a[i]
print(b)


def sqrtSum(left, right):
    sum = 0
    block_left = int(left/sqrt_len)
    print("block left:", block_left)
    block_right = int(right/sqrt_len)
    print("block right:", block_right)
    if block_left == block_right:
        for i in range(left, right):
            sum += a[i]
    else: 
        for i in range(left, (sqrt_len - block_left) * (block_right) ):
            sum += a[i]
        for i in range(block_left+1, block_right-1):
            sum += b[i]
        for i in range(block_right*sqrt_len, right):
            sum += a[i]
    return sum
while 1:
    left = int(input())
    r = int(input())
    print("elementSum:", elementSum(left,r))
    print("sqrtSum:", sqrtSum(left,r))
    if sqrtSum(left,r)==elementSum(left,r):
       print(sqrtSum(left,r)==elementSum(left,r))    
    else: break