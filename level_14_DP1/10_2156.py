"""
N = 6
numList = [6, 10, 13, 9, 8, 1]

Goal: minimize amount of excluded wine
Condition: x o o x o o x o x
           there can be at most two included wine glasses
           between each pair of excluded wine glasses

exclude[i]
minimum amount of excluded wine (1~i) when we exclude ith glass
"""

N = int(input())
numList = [0] + [int(input()) for _ in range(N)]

exclude = []
# obvious case
for i in range(4):
    if i > N:
        continue
    exclude.append(numList[i])

# If ith wine is excluded, one of (i-3), (i-2), (i-1)th wine must be excluded
for i in range(4, N+1):
    exclude.append(min(exclude[i-1], exclude[i-2], exclude[i-3]) + numList[i])

print(sum(numList) - min(exclude[N-2], exclude[N-1], exclude[N]), end="")
