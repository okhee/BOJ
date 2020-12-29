[N, M] = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

direcList = [(0, 1), (-1, 0), (0, -1), (1, 0)]
answer = N*M

# elem of cctvList: [n, (i, j), [0, 1, ...]]
#                    n: type of cctv
#               (i, j): location of cctv
#          [0, 1, ...]: possible direction of cctv viewpoint,
#                       represented as index of direcList
# cctv5List contains location of cctv type 5
cctvList = list()
cctv5List = list()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            cctvList.append([1, (i, j), [0]])
        elif grid[i][j] == 2:
            cctvList.append([2, (i, j), [0, 2]])
        elif grid[i][j] == 3:
            cctvList.append([3, (i, j), [0, 1]])
        elif grid[i][j] == 4:
            cctvList.append([4, (i, j), [0, 1, 2]])

        # cctv 5 list
        elif grid[i][j] == 5:
            cctv5List.append((i, j))

# rotate cctv (cctvList[idx]) by degree. (1 = 90 degrees counterclockwise)
def rotate(idx, degree):
    global cctvList

    direcList = cctvList[idx][2]
    for i in range(len(direcList)):
        direcList[i] = (direcList[i] + degree) % 4

# input: location of cctv, view angle, amount of grid val change
# During function: change value of grid which is in range of view angle
# output: None
def watch(loc, rot, diff):
    global grid

    di, dj = direcList[rot]
    cur_i, cur_j = loc[0] + di, loc[1] + dj
    while 0 <= cur_i < N and 0 <= cur_j < M:
        # wall
        if grid[cur_i][cur_j] == 6:
            break
        # Ignore CCTV
        if grid[cur_i][cur_j] <= 0:
            grid[cur_i][cur_j] += diff

        cur_i, cur_j = cur_i + di, cur_j + dj

# return area of blind spot
def blindArea():
    ret = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                ret += 1
    return ret

# nth cctv handled
def func(n):
    global grid
    global cctvList
    global answer

    if n == len(cctvList):
        val = blindArea()
        if val < answer:
            answer = val
        return
    
    for _ in range(4 if cctvList[n][0] != 2 else 2):
        location = cctvList[n][1]
        viewpointList = cctvList[n][2]

        for viewpoint in viewpointList:
            watch(location, viewpoint, -1)
        
        func(n+1)
        
        for viewpoint in viewpointList:
            watch(location, viewpoint, 1)

        rotate(n, 1)

for cctv5 in cctv5List:
    watch(cctv5, 0, -1)
    watch(cctv5, 1, -1)
    watch(cctv5, 2, -1)
    watch(cctv5, 3, -1)

func(0)

print(answer, end="")
