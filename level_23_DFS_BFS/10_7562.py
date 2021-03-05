import collections
import sys
input = sys.stdin.readline

nextMove = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]

iter = int(input())
for _ in range(iter):
    N = int(input())
    init = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    board = [[-1 for j in range(N)] for i in range(N)]

    bfsQueue = collections.deque()
    bfsQueue.append(init)
    board[init[0]][init[1]] = 0
    while bfsQueue:
        ci, cj = bfsQueue.popleft()

        for di, dj in nextMove:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if board[ni][nj] >= 0:
                continue
            bfsQueue.append((ni, nj))
            board[ni][nj] = board[ci][cj] + 1
        if board[end[0]][end[1]] >= 0:
            print(board[end[0]][end[1]])
            break
