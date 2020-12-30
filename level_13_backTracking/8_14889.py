"""
N = 4
Player #0 ~ #(N-1)

0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

한 팀당 N/2 = 2명
Player #0이 포함된 팀을 A, 아닌 팀을 팀 B라 하면 (pivoting)

A -> Player #0 + ((N - 1)명 중 (N/2 - 1)명 뽑기)
"""
import itertools

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# N = 6
# grid = [[0, 1, 2, 3, 4, 5], \
#         [1, 0, 2, 3, 4, 5], \
#         [1, 2, 0, 3, 4, 5], \
#         [1, 2, 3, 0, 4, 5], \
#         [1, 2, 3, 4, 0, 5], \
#         [1, 2, 3, 4, 5, 0]]
      
for i in range(N):
    for j in range(i):
        grid[j][i] += grid[i][j]
        grid[i][j] = 0

answer = 1 << 30
for members in itertools.combinations(range(1, N), N//2 - 1):
    teamAList = [0] + list(members)
    teamAStat = 0
    for i, j in itertools.combinations(teamAList, 2):
        teamAStat += grid[i][j]

    teamBList = []
    teamBStat = 0
    for member in range(N):
        if member not in teamAList:
            teamBList.append(member)
    for i, j in itertools.combinations(teamBList, 2):
        teamBStat += grid[i][j]

    val = abs(teamAStat - teamBStat)
    if val < answer:
        answer = val

print(answer, end="")
