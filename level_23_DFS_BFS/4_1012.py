import collections

T = int(input())
worm = [0 for rpt in range(T)]

for rpt in range(T):
    [M, N, K] = list(map(int, input().split()))

    grid = [[0 for j in range(M)] for i in range(N)]
    visit = [[False for j in range(M)] for i in range(N)]
    direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for k in range(K):
        cabbage = list(map(int, input().split()))
        grid[cabbage[1]][cabbage[0]] = 1

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visit[i][j]:
                worm[rpt] += 1

                bfsQueue = collections.deque()
                bfsQueue.append((i, j))
                visit[i][j] = True

                while len(bfsQueue) > 0:
                    cur_i, cur_j = bfsQueue.popleft()
                    for di, dj in direc:
                        ni, nj = cur_i + di, cur_j + dj
                        if (ni < 0) or (ni >= N) or (nj < 0) or (nj >= M):
                            continue
                        if grid[ni][nj] == 0 or visit[ni][nj]:
                            continue
                        bfsQueue.append((ni, nj))
                        visit[ni][nj] = True

print("\n".join(list(map(str, worm))), end="")
