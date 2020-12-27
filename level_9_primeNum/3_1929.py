import math

[M, N] = list(map(int, input().split()))

maxNum = N

numList = [False, True] * (int(maxNum/2)+1)
numList[1] = False
numList[2] = True

maxIndex = math.ceil(math.sqrt(maxNum)) + 1
for i in range(3, maxIndex, 2):
    if not numList[i]:
        continue
    for j in range(i*i, maxNum+1, i):
        numList[j] = False


largestPrime = 0

for i in reversed(range(M, N+1)):
    if numList[i]:
        largestPrime = i
        break

for i in range(M, largestPrime):
    if(numList[i]):
        print(i)
print(largestPrime, end="")
