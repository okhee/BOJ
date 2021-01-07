# N = 8
# arr = [[1, 1, 0, 0, 0, 0, 1, 1], \
#        [1, 1, 0, 0, 0, 0, 1, 1], \
#        [0, 0, 0, 0, 1, 1, 0, 0], \
#        [0, 0, 0, 0, 1, 1, 0, 0], \
#        [1, 0, 0, 0, 1, 1, 1, 1], \
#        [0, 1, 0, 0, 1, 1, 1, 1], \
#        [0, 0, 1, 1, 1, 1, 1, 1], \
#        [0, 0, 1, 1, 1, 1, 1, 1]]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def func(r, c, n):
    if n == 1:
        if arr[r][c] == 0:
            return (1, 0)
        else:
            return (0, 1)

    next_n = n//2
    subResult = list(zip(func(r, c, next_n), func(r, c + next_n, next_n), \
                         func(r + next_n, c, next_n), func(r + next_n, c + next_n, next_n)))
    res = (sum(subResult[0]), sum(subResult[1]))

    if res == (4, 0):
        return (1, 0)
    elif res == (0, 4):
        return (0, 1)
    else:
        return res

# ans = func(0, 0, 8)
ans = func(0, 0, N)
print(f'{ans[0]}\n{ans[1]}', end="")

