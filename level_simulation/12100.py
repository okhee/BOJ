import itertools

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# default: move to left
def rowMove(col):
    tmp = [0 for i in range(len(col))]
    canMerge = True
    lastNum = 0
    j = 0

    for i in range(len(col)):
        if col[i] == 0:
            continue

        # if number matches and can be merged, ...
        # lastNum > 0 guarantees tmp[j-1] is valid
        if lastNum == col[i] and canMerge:
            tmp[j-1] = 2 * col[i]
            # No consecutive merging
            canMerge = False

        # No match or no merging,
        else:
            tmp[j] = col[i]
            lastNum = col[i]
            # restore canMerge
            canMerge = True
            j += 1

    return tmp

def move(arr, direc):
    for i in range(len(arr)):
        # left
        if direc == 0:
            arr[i] = rowMove(arr[i])
        
        # right
        elif direc == 1:
            arr[i].reverse()
            arr[i] = rowMove(arr[i])
            arr[i].reverse()

        # up
        elif direc == 2:
            arrT = [arr[_][i] for _ in range(len(arr))]
            arrT = rowMove(arrT)
            for _ in range(len(arr)):
                arr[_][i] = arrT[_]

        # down
        elif direc == 3:
            arrT = [arr[_][i] for _ in range(len(arr))]

            arrT.reverse()
            arrT = rowMove(arrT)
            arrT.reverse()

            for _ in range(len(arr)):
                arr[_][i] = arrT[_]

for moves in itertools.product('0123', repeat=5):
    tmp = [grid[_][:] for _ in range(len(grid))]
    
    for i in map(int, moves):
        move(tmp, i)
    
    val = max(list(map(max, tmp)))
    if val > answer:
        answer = val

print(answer, end="")
