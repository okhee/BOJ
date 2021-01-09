N = int(input())
numList = list(map(int, input().split()))

M = int(input())
qList = list(map(int, input().split()))

def binSearch(start, end, key):
    global numList

    if start > end:
        return -1
    elif start == end:
        return start if numList[start] == key else -1
            
    mid = (start + end) // 2

    if numList[mid] == key:
        return mid
    elif numList[mid] > key:
        return binSearch(start, mid, key)
    else:
        return binSearch(mid + 1, end, key)

numList.sort()

for q in qList:
    print(1) if binSearch(0, N-1, q) >= 0 else print(0)
