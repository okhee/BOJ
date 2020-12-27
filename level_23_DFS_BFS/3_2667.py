import collections

N = int(input())

grid = [list(map(str, input())) for i in range(N)]
visit = [[0 for j in range(N)] for i in range(N)]
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
buildingID = 0
buildingNum = [-1]

# BFS-----------------
# init Queue
for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and visit[i][j] == 0:
            bfsQueue = collections.deque()
            bfsQueue.append((i, j))

            buildingID += 1
            visit[i][j] = buildingID
            buildingNum.append(1)

            while len(bfsQueue) > 0:
                cur_i, cur_j = bfsQueue.popleft()
                for di, dj in direc:
                    ni, nj = cur_i + di, cur_j + dj
                    if (ni < 0) or (ni >= N) or (nj < 0) or (nj >= N):
                        continue
                    if grid[ni][nj] == '0' or visit[ni][nj] > 0:
                        continue
                    bfsQueue.append((ni, nj))
                    visit[ni][nj] = buildingID
                    buildingNum[buildingID] += 1
print(buildingID)
print("\n".join(list(map(str, sorted(buildingNum)[1:]))), end="")
