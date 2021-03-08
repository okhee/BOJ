import math
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[math.inf for j in range(N)] for i in range(N)]

for i in range(N):
    adj[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    if cost < adj[start-1][end-1]:
        adj[start-1][end-1] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

res = []
for i in range(N):
    subRes = []
    for j in range(N):
        if adj[i][j] < math.inf:
            subRes.append(str(adj[i][j]))
        else:
            subRes.append(str(0))
    res.append(" ".join(subRes))
print("\n".join(res), end="")
