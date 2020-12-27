import collections

[N, M] = list(map(int, input().split()))

grid = [list(map(str, input())) for i in range(N)]
visit = [[0 for j in range(M)] for i in range(N)]
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

bfsQueue = collections.deque()

bfsQueue.append((0, 0))
visit[0][0] = 1

while len(bfsQueue) > 0:
    cur_i, cur_j = bfsQueue.popleft()
    for di, dj in direc:
        ni, nj = cur_i + di, cur_j + dj
        if (ni < 0) or (ni >= N) or (nj < 0) or (nj >= M):
            continue
        if grid[ni][nj] == '0' or visit[ni][nj] > 0:
            continue
        bfsQueue.append((ni, nj))
        visit[ni][nj] = visit[cur_i][cur_j] + 1

print(visit[N - 1][M - 1], end="")
