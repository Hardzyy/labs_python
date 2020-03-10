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
    for i in range(index1, index2+1):
        sum += a[i]
    return sum

# print("Time",time.time()-start_time,"secs")
# n = int(input())
# for i in range(1):
#     rightBorder = random.randint(0,nArray-1)
#     leftBorder = random.randint(0,rightBorder)
#     print("leftBorder: ", leftBorder, "rightBorder:", rightBorder)
#     print(elementSum(leftBorder, rightBorder)==1)
#     print("Step:", i)
# print("Time",time.time()-start_time,"secs")

def sqrtSum(left, right):
    sum = 0
    sqrt_len = int(nArray**0.5 + 1)
    b = []
    for i in range(0,int(nArray/sqrt_len + 1)):
        b.append(0)

    for i in range(nArray):
        n = int(i / sqrt_len)
        b[n] += a[i]
    block_left = left/sqrt_len
    block_right = right/sqrt_len
    if block_left == block_right:
        for i in range(left, right+1):
            sum += a[i]
    else: for i in range(left, (block_right + 1)*(sqrt_len - 1)):
              sum += a[i]
          for i in range(block_left+1, block_right-1)
              sum += b[i]
          for i in range(block_right, right):
              sum += a[i]
    return sum
print(sqrtSum(1,2))