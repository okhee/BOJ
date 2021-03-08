import math
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

adj = [[math.inf for j in range(V)] for i in range(V)]

for i in range(V):
    adj[i][i] = 0

for _ in range(E):
    start, end, cost = map(int, input().split())
    if cost < adj[start-1][end-1]:
        adj[start-1][end-1] = cost

for k in range(V):
    for i in range(V):
        for j in range(V):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

ans = math.inf
for i in range(V):
    for j in range(i+1, V):
        cost = adj[i][j] + adj[j][i]
        if cost < ans:
            ans = cost
if ans < math.inf:
    print(ans)
else:
    print(-1)
