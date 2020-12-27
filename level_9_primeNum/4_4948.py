import math

maxNum = 123456*2

numList = [False, True] * (int(maxNum/2)+1)
numList[1] = False
numList[2] = True

maxIndex = math.ceil(math.sqrt(maxNum)) + 1
for i in range(3, maxIndex, 2):
    if not numList[i]:
        continue
    for j in range(i*i, maxNum+1, i):
        numList[j] = False

subSumList = [0] * (maxNum+1)
for i in range(2, len(subSumList)):
    subSumList[i] += subSumList[i-1] + (1 if numList[i] else 0)

N = int(input())
initFlag = True
while N != 0:
    if initFlag:
        print(subSumList[2*N] - subSumList[N], end="")
        initFlag = False
    else:
        print("\n" + str(subSumList[2*N] - subSumList[N]), end="")
    N = int(input())
    