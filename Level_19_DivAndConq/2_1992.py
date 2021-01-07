# N = 8
# arr = [[1, 1, 1, 1, 0, 0, 0, 0], \
#        [1, 1, 1, 1, 0, 0, 0, 0], \
#        [0, 0, 0, 1, 1, 1, 0, 0], \
#        [0, 0, 0, 1, 1, 1, 0, 0], \
#        [1, 1, 1, 1, 0, 0, 0, 0], \
#        [1, 1, 1, 1, 0, 0, 0, 0], \
#        [1, 1, 1, 1, 0, 0, 1, 1], \
#        [1, 1, 1, 1, 0, 0, 1, 1]]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def func(r, c, n):
    if n == 1:
        return str(arr[r][c])

    next_n = n//2
    subResult = [func(r, c, next_n), func(r, c + next_n, next_n), \
                 func(r + next_n, c, next_n), func(r + next_n, c + next_n, next_n)]
    if subResult == ["1", "1", "1", "1"]:
        return "1"
    elif subResult == ["0", "0", "0", "0"]:
        return "0"
    else:
        return "(" + "".join(subResult) + ")"

print(func(0, 0, N), end="")
