resultList = []
resultNum = 0

def hanoi(start, end, n):
    global resultList
    global resultNum

    if n == 1:
        resultList.append([start, end])
        resultNum += 1
        return
    
    hanoi(start, 6-start-end, n-1)
    resultList.append([start, end])
    resultNum += 1
    hanoi(6-start-end, end, n-1)

K = int(input())
hanoi(1, 3, K)

print(resultNum)
for i in range(len(resultList)):
    print(str(resultList[i][0]) + " " + str(resultList[i][1]), end="")
    if i < len(resultList) - 1:
        print()
