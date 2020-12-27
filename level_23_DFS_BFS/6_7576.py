import sys
import collections

input = sys.stdin.readline

[M, N] = list(map(int, input().split()))

grid = [list(map(int, input().split())) for i in range(N)]
visit = [[0 for j in range(M)] for i in range(N)]
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

bfsQueue = collections.deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            bfsQueue.append((i, j))
            visit[i][j] = 1

while len(bfsQueue) > 0:
    cur_i, cur_j = bfsQueue.popleft()
    for di, dj in direc:
        ni, nj = cur_i + di, cur_j + dj
        if (ni < 0) or (ni >= N) or (nj < 0) or (nj >= M):
            continue
        if grid[ni][nj] != 0 or visit[ni][nj] > 0:
            continue
        bfsQueue.append((ni, nj))
        visit[ni][nj] = visit[cur_i][cur_j] + 1

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and visit[i][j] == 0:
            print(-1, end="")
            exit()

print(max(map(max, visit)) - 1, end="")
