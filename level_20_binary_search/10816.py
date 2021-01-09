hashArrLen = 10007
hashArr = [[] for _ in range(hashArrLen)]

def hashVal(num):
    return num % hashArrLen

N = int(input())
inputList = list(map(int, input().split()))

for num in inputList:
    loc = hashArr[hashVal(num)]
    isNew = True
    for i in range(len(loc)):
        if loc[i][0] == num:
            loc[i][1] += 1
            isNew = False
            break
    if isNew:
        loc.append([num, 1])

M = int(input())
queryList = list(map(int, input().split()))

for query in queryList:
    loc = hashArr[hashVal(query)]
    exist = False
    for i in range(len(loc)):
        if loc[i][0] == query:
            print(f'{loc[i][1]} ', end="")
            exist = True
            break
    if not exist:
        print('0 ', end="")
