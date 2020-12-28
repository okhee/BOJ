[N, M] = list(map(int, input().split()))

resList = []

def record(prev, m):
    global resList

    if m == 0:
        resList.append(prev)
        return

    for i in range(1, N+1):
        if len(prev) > 0 and i < int(prev[-1]):
            continue
        record(prev + [str(i)], m-1)

record([], M)
for i in range(len(resList)):
    resList[i] = " ".join(resList[i])
print("\n".join(resList), end="")
