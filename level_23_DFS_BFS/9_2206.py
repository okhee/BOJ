"""
i) Conduct BFS from start (0, 0), end (N-1, M-1) respectively.
   Calculate path from start to end

ii) Find 'breakable point'

X X X (Wall)
0 1 0
1 1 1

1) 1 zero
0 1 1   1 0 1      
1 1 1   1 1 1
1 1 1   1 1 1      
(xxx)   (xxx)

2) 2 zeros
0 0 1   0 1 1   0 1 1  
1 1 1   1 1 0   1 1 1  
1 1 1   1 1 1   1 1 0  
(xxx)   (xxx)   (xxx)

1 0 1   1 0 1   1 0 1   1 0 1   0 0 1
0 1 1   1 1 1   0 1 1   0 1 0   0 1 1
1 1 1   1 0 1   1 0 1   1 0 1   1 0 1
(ooo)   (ooo)   (ooo)   (ooo)   (ooo)

0 0 1   0 1 1   0 0 1
0 1 1   0 1 1   0 1 1    ----> meaningless case, but just include it
1 1 1   0 0 0   0 0 1
(xxx)   (xxx)   (xxx)

iii) for each 'breakable', since breaking guarantees that possible path exists,
    calculate shortest path length of (visit[0][0] ~ visit[brk][brk]) and 
                                      (visit[N-1][M-1] ~ visit[brk][brk])
    calculate new path length using this

iv) compare, output
"""

import collections

# [N, M] = [4, 6]
# grid = [[0, 1, 0, 0, 0, 0], \
#         [0, 0, 0, 1, 1, 0], \
#         [1, 0, 0, 1, 0, 1], \
#         [1, 1, 1, 1, 1, 0]]
[N, M] = list(map(int, input().split()))
grid = [list(map(int, input())) for _ in range(N)]

visitFromStart = [[0 for j in range(M)] for i in range(N)]
visitFromEnd = [[0 for j in range(M)] for i in range(N)]

direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# input: coordinate of wall (grid value 1)
# output: is this wall worth breaking? -> True, False
# if two or more zeros adjacent to wall, wall is worth breaking
# while ignoring out of boundary.
def isBreakable(coor):
    i, j = coor
    zeros = 0
    for di, dj in direc:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if grid[ni][nj] == 0:
            zeros += 1
    return True if zeros >= 2 else False

def bfs():
    global visitFromStart
    global visitFromEnd

    startQueue = collections.deque()
    startQueue.append((0, 0))
    visitFromStart[0][0] = 1

    while len(startQueue) > 0:
        cur_i, cur_j = startQueue.popleft()
        for di, dj in direc:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if grid[ni][nj] == 1 or visitFromStart[ni][nj] > 0:
                continue
            startQueue.append((ni, nj))
            visitFromStart[ni][nj] = visitFromStart[cur_i][cur_j] + 1
        
    endQueue = collections.deque()
    endQueue.append((N-1, M-1))
    visitFromEnd[N-1][M-1] = 1

    while len(endQueue) > 0:
        cur_i, cur_j = endQueue.popleft()
        for di, dj in direc:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if grid[ni][nj] == 1 or visitFromEnd[ni][nj] > 0:
                continue
            endQueue.append((ni, nj))
            visitFromEnd[ni][nj] = visitFromEnd[cur_i][cur_j] + 1

def getPath(brk=()):
    # if end is reachable from start
    end = (N-1, M-1)
    isConnected = (visitFromStart[end[0]][end[1]] > 0)
    
    # No wall breaking
    if len(brk) == 0:
        return visitFromStart[end[0]][end[1]] if isConnected else -1
    # breaking wall
    else:
        # considering additional bfs where end is starting point
        # -> no difference between isConnected or not cases
        # __ToBrk: length of shortest path from __ to break point
        #          1000**2 if cannot reach to break point
        startToBrk = 1000**2
        endToBrk = 1000**2
        i, j = brk
        for di, dj in direc:
            ni, nj = i + di, j + dj
                
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            if grid[ni][nj] == 0:
                valFromStart = visitFromStart[ni][nj]
                if valFromStart > 0 and valFromStart < startToBrk:
                    startToBrk = valFromStart

                valFromEnd = visitFromEnd[ni][nj]
                if valFromEnd > 0 and valFromEnd < endToBrk:
                    endToBrk = valFromEnd

        if startToBrk == 1000**2 or endToBrk == 1000**2:
            return -1
        # new path through broken wall
        return startToBrk + endToBrk + 1

bfs()

isValid = False
answer = 1000**2
val = getPath()
if val > 0:
    isValid = True
    answer = val

for i in range(N):
    for j in range(M):
        # for each wall,
        if grid[i][j] == 1:
            brkCoor = (i, j)
            if isBreakable(brkCoor):
                val = getPath(brkCoor)
                if val > 0:
                    isValid = True
                    if val < answer:
                        answer = val
if isValid:
    print(answer, end="")
else:
    print(-1, end="")
