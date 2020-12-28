import sys
input = sys.stdin.readline

N = int(input().rstrip())

# Queen can be placed on grid value >= 0
grid = [[0 for j in range(N)] for i in range(N)]
direc = [(1, -1), (1, 0), (1, 1)]
res = 0

def queenOnGrid(i, j, diff):
    global grid
    global direc

    for di, dj in direc:
        cur_i, cur_j = i + di, j + dj
        while 0 <= cur_i < N and 0 <= cur_j < N:
            grid[cur_i][cur_j] += diff
            cur_i, cur_j = cur_i + di, cur_j + dj

def func(n):
    global res
    global grid

    if n == N:
        res += 1
        return

    i = n
    for j in range(N):
        if grid[i][j] >= 0:
            queenOnGrid(i, j, -1)
            func(n+1)
            queenOnGrid(i, j, 1)
func(0)
print(res, end="")
