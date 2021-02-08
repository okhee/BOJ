import collections
import sys
input = sys.stdin.readline

# NxM Board, P Players (1, 2, ..., P)
N, M, P = map(int, input().split())

# ith player can extend his/her castle by S[i] far in each turn.
S = {(i+1):val for i, val in enumerate(list(map(int, input().split())))}

# BFS Queue for each player
queue = {(i+1):collections.deque() for i in range(P)}
# Number of castles for each player
answer = {(i+1):0 for i in range(P)}

grid = [list(map(str, input().rstrip())) for _ in range(N)]
direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# Enqueue player's initial position
for i in range(N):
    for j in range(M):
        if grid[i][j].isdecimal():
            queue[int(grid[i][j])].append((i, j))
            answer[int(grid[i][j])] += 1

while sum(map(len, queue.values())) > 0:
    # For each player,
    for i in range(1, P+1):
        # ith player can move at most S[i] far in one turn
        # repeat unit distance movement s time
        for s in range(S[i]):
            if len(queue[i]) == 0:
                break
            # Next (adjacent) position queue (unit distance far)
            newQueue = collections.deque()
            while len(queue[i]) > 0:
                ci, cj = queue[i].popleft()
                for di, dj in direc:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    if grid[ni][nj] != ".":
                        continue
                    newQueue.append((ni, nj))
                    grid[ni][nj] = str(i)
                    answer[i] += 1
            queue[i] = newQueue
            
print(" ".join(list(map(str, answer.values()))), end="")
