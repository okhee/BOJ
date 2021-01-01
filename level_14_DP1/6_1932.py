N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

arr = [grid[0][0]]

for i in range(1, N):
    tmp = []
    for j in range(i+1):
        if j == 0:
            val = arr[j]
        elif j == i:
            val = arr[j-1]
        else:
            val = max(arr[j], arr[j-1])
        tmp.append(grid[i][j] + val)
    arr = tmp
print(max(arr), end="")
