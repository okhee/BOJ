import sys
import collections

input = sys.stdin.readline

[M, N, H] = list(map(int, input().split()))

# grid = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]
grid = [[input().split() for n in range(N)] for h in range(H)]
visit = [[[0 for m in range(M)] for n in range(N)] for h in range(H)]
direc = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

bfsQueue = collections.deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == "1":
                bfsQueue.append((i, j, k))
                visit[i][j][k] = 1

while len(bfsQueue) > 0:
    cur_i, cur_j, cur_k = bfsQueue.popleft()
    for di, dj, dk in direc:
        ni, nj, nk = cur_i + di, cur_j + dj, cur_k + dk
        if (ni < 0) or (ni >= H) or (nj < 0) or (nj >= N) or (nk < 0) or (nk >= M):
            continue
        if visit[ni][nj][nk] > 0:
            continue
        # if grid[ni][nj][nk] == "1" or grid[ni][nj][nk] == "-1":
        #     continue
        if grid[ni][nj][nk] == "0":
            bfsQueue.append((ni, nj, nk))
            visit[ni][nj][nk] = visit[cur_i][cur_j][cur_k] + 1

ans = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visit[i][j][k] == 0 and grid[i][j][k] == "0":
                print(-1, end="")
                exit()
            if visit[i][j][k] > ans:
                ans = visit[i][j][k]

print(ans - 1, end="")

