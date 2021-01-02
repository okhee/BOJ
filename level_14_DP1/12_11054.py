# N = 6
# numList = [10, 20, 10, 30, 20, 50]

# N = 10
# numList = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]

N = int(input())
numList = list(map(int, input().split()))

forwardArr = [0 for _ in range(N)]
backwardArr = [0 for _ in range(N)]

for i in range(N):
    prev = 0
    for j in range(i):
        if numList[i] > numList[j]:
            if forwardArr[j] > prev:
                prev = forwardArr[j]
    forwardArr[i] = prev + 1

for i in reversed(range(N)):
    prev = 0
    for j in reversed(range(i, N)):
        if numList[i] > numList[j]:
            if backwardArr[j] > prev:
                prev = backwardArr[j]
    backwardArr[i] = prev + 1

biArr = [forwardArr[i] + backwardArr[i] for i in range(N)]

print(max(max(forwardArr), max(backwardArr), (max(biArr) - 1)), end="")
