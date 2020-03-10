import time
import random
import math


print("Enter array size")
nArray = int(input())
start_time = time.time()
# a = [random.randint(0, nArray) for i in range(nArray)]
#print(a)


a = []
for i in range(0, nArray):
    a.append(i)
print(a)

def elementSum(index1, index2):
    sum = 0
    for i in range(index1, index2+1):
        sum += a[i]
    return sum

#print("Time",time.time()-start_time,"secs")
#n = int(input())
#for i in range(1):
#    rightBorder = random.randint(0,nArray-1)
#    leftBorder = random.randint(0,rightBorder)
#    print("leftBorder: ", leftBorder, "rightBorder:", rightBorder)
#    print(elementSum(leftBorder, rightBorder)==1)
#    print("Step:", i)
#print("Time",time.time()-start_time,"secs")

sqrt_len = int(nArray**0.5 + 1)
print(sqrt_len)

b = []
for i in range(0,int(nArray/sqrt_len)):
    b.append(0)

for i in range(nArray):
    n = int(i / sqrt_len)
    b[n] += a[i]

print(b)