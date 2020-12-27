import math

maxNum = 10000

primeList = [False, True] * (int(maxNum/2)+1)
primeList[1] = False
primeList[2] = True

maxIndex = math.ceil(math.sqrt(maxNum)) + 1
for i in range(3, maxIndex, 2):
    if not primeList[i]:
        continue
    for j in range(i*i, maxNum+1, i):
        primeList[j] = False

# for each target,
rpt = int(input())
for iteration in range(rpt):
    targetNum = int(input())
    diff = targetNum
    result = [0]

    i = 2
    while i <= int(targetNum/2):
        if primeList[i] and primeList[targetNum - i]:   # if two partition numbers are prime,
            if (targetNum - 2*i) < diff:                # if diff is smaller,
                diff = (targetNum - 2*i)
                result = (i, targetNum - i)
        i += 1

    print("{0} {1}".format(result[0], result[1]), end="")
    if iteration != (rpt-1):
        print()
