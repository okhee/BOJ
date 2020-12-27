import math

maxNum = 10000
isPrimeList = [True] * (maxNum - 1) # 2 ~ maxNum
for i in range(2, math.ceil(math.sqrt(maxNum))):
    for j in range(i+1, maxNum+1):
        if (j % i == 0):
            isPrimeList[j-2] = False
def isPrime(n):
    if(n < 2):
        return False
    return isPrimeList[n-2]

M = int(input())
N = int(input())

leastPrime = 0
sumPrime = 0

for i in range(M, N+1):
    if isPrime(i):
        leastPrime = i
        break

for i in range(M, N+1):
    if isPrime(i):
        sumPrime += i

if leastPrime == 0:
    print("-1", end="")
else:
    print(sumPrime)
    print(leastPrime, end="")
