import math

maxNum = 1000
isPrimeList = [True] * (maxNum - 1) # 2 ~ maxNum
for i in range(2, math.ceil(math.sqrt(maxNum))):
    for j in range(i+1, maxNum+1):
        if (j % i == 0):
            isPrimeList[j-2] = False
def isPrime(n):
    if(n < 2):
        return False
    return isPrimeList[n-2]

dummy = input()
numList = list(map(int, input().split()))
totalPrime = 0

for i in range(len(numList)):
    if isPrime(numList[i]):
        totalPrime += 1

print(totalPrime, end="")
