from itertools import combinations

[N, M] = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

# 0 = empty, 1 = customer, 2 = chicken store
# grid = [[0, 2, 0, 1, 0], \
#         [1, 0, 1, 0, 0], \
#         [0, 0, 0, 0, 0], \
#         [0, 0, 0, 1, 1], \
#         [0, 0, 0, 1, 2]]

# storeList[i] = location of ith store
# storeList = [(0, 1), (4, 4)]

# ith element (list) contains location of customer whose closest store is storeList[i]
# customerList = [[(0, 3), (1, 0), (1, 2)], [(3, 3), (3, 4), (4, 3)]]

# distList[i] = sum of distance from customers (in customerList[i]) to nearest store (storeList[i])
# distList = [6, 4]

def nearChicken(loc, maskIdxList = ()):
    global storeList
    global storeNum

    closestIndex = 0
    closestDist = 2*N

    mask = [True for _ in range(storeNum)]
    for idx in maskIdxList:
        mask[idx] = False
    
    for idx, store in enumerate(storeList):
        if not mask[idx]:
            continue
        dist = abs(loc[0] - store[0]) + abs(loc[1] - store[1])
        if dist < closestDist:
            closestIndex = idx
            closestDist = dist

    return closestIndex, closestDist

storeList = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            storeList.append((i, j))
storeNum = len(storeList)

customerList = [[] for _ in range(storeNum)]
distList = [0 for _ in range(storeNum)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            # find nearest chicken store for customer located in (i, j)
            idx, dist = nearChicken((i, j))
            customerList[idx].append((i, j))
            distList[idx] += dist

# max distance : 2*N
# # of store   : storeNum
# # of customer: no greater than 2*N
answer = (2 * N) * storeNum * (2 * N)

# choosing store that will be closed
for storeComb in combinations(range(storeNum), storeNum - M):
    customerTmp = [customerList[_][:] for _ in range(storeNum)]
    distTmp = distList[:]

    # Close each store, allocate customer(s) to other store
    for store in storeComb:
        distTmp[store] = 0
        for customer in customerTmp[store]:
            idx, dist = nearChicken(customer, maskIdxList=storeComb)
            customerTmp[idx].append(customer)
            distTmp[idx] += dist

    val = sum(distTmp)
    if val < answer:
        answer = val
    
print(answer, end="")
