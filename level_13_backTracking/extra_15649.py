[N, M] = list(map(int, input().split()))

resList = []
isUsed = [False for i in range(N+1)]

def func(m):
    if m == M:
        print(" ".join(resList))
        return
    
    for i in range(1, len(isUsed)):
        if not isUsed[i]:
            isUsed[i] = True
            resList.append(str(i))
            func(m+1)
            resList.pop()
            isUsed[i] = False
func(0)
