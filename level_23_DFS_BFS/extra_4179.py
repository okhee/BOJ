import sys
import collections

input = sys.stdin.readline
[R, C] = list(map(int, input().split()))

fireQueue   = collections.deque()
# -1: fire never been
#  0: initial fire
#  n: after (n) minute, fire exist
fireGrid    = [[-1 for c in range(C)] for r in range(R)]
playerQueue = collections.deque()
playerGrid  = [[-1 for c in range(C)] for r in range(R)]

grid = []
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for r in range(R):
    line = list(map(str, input().rstrip()))
    for c in range(C):
        if line[c] == "F":
            fireQueue.append((r, c))
            fireGrid[r][c] = 0
        elif line[c] == "J":
            playerQueue.append((r, c))
            playerGrid[r][c] = 0
    grid.append(line)

while len(fireQueue) > 0:
    cur_y, cur_x = fireQueue.popleft()
    for dy, dx in direc:
        nxt_y, nxt_x = cur_y + dy, cur_x + dx
        if nxt_y < 0 or nxt_y >= R or nxt_x < 0 or nxt_x >= C:
            continue
        if grid[nxt_y][nxt_x] == "#" or fireGrid[nxt_y][nxt_x] >= 0:
            continue
        fireQueue.append((nxt_y, nxt_x))
        fireGrid[nxt_y][nxt_x] = fireGrid[cur_y][cur_x] + 1

while len(playerQueue) > 0:
    cur_y, cur_x = playerQueue.popleft()
    for dy, dx in direc:
        nxt_y, nxt_x = cur_y + dy, cur_x + dx
        if nxt_y < 0 or nxt_y >= R or nxt_x < 0 or nxt_x >= C:
            # since exiting is our goal,
            # right after exit, print and terminate
            print(playerGrid[cur_y][cur_x] + 1, end="")
            exit()
        if grid[nxt_y][nxt_x] == "#" or playerGrid[nxt_y][nxt_x] >= 0:
            continue

        elapsed = playerGrid[cur_y][cur_x] + 1
        # Debug:
        # fire is valid only if fireGrid value is >= 0
        # no need to check fire & player if fire is invalid
        if fireGrid[nxt_y][nxt_x] >= 0 and elapsed >= fireGrid[nxt_y][nxt_x]:
            continue

        playerQueue.append((nxt_y, nxt_x))
        playerGrid[nxt_y][nxt_x] = elapsed

print("IMPOSSIBLE", end="")




