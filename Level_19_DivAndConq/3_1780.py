

# N = 9
# arr = [[0,  0,  0,  1,  1,  1, -1, -1, -1], \
#        [0,  0,  0,  1,  1,  1, -1, -1, -1], \
#        [0,  0,  0,  1,  1,  1, -1, -1, -1], \
#        [1,  1,  1,  0,  0,  0,  0,  0,  0], \
#        [1,  1,  1,  0,  0,  0,  0,  0,  0], \
#        [1,  1,  1,  0,  0,  0,  0,  0,  0], \
#        [0,  1, -1,  0,  1, -1,  0,  1, -1], \
#        [0, -1,  1,  0,  1, -1,  0,  1, -1], \
#        [0,  1, -1,  1,  0, -1,  0,  1, -1]]
import itertools
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def func(r, c, n):
    if n == 1:
        if arr[r][c] == -1:
            return (1, 0, 0)
        elif arr[r][c] == 0:
            return (0, 1, 0)
        elif arr[r][c] == 1:
            return (0, 0, 1)

    next_n = n//3
    subResult = [func(r + dr, c + dc, next_n) for dr, dc in itertools.product(range(0, n, next_n), repeat=2)]
    subResult = list(zip(subResult[0], subResult[1], subResult[2], subResult[3], subResult[4], \
                         subResult[5], subResult[6], subResult[7], subResult[8]))
    res = tuple(map(sum, subResult))

    if res == (9, 0, 0):
        return (1, 0, 0)
    elif res == (0, 9, 0):
        return (0, 1, 0)
    elif res == (0, 0, 9):
        return (0, 0, 1)
    else:
        return res

res = func(0, 0, N)
print(f'{res[0]}\n{res[1]}\n{res[2]}', end="")
