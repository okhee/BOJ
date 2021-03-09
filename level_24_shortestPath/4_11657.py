import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges.append((start-1, end-1, cost))

dist = [math.inf for _ in range(N)]
dist[0] = 0
for i in range(1, N):
    for start, end, cost in edges:
        if dist[end] > dist[start] + cost:
            dist[end] = dist[start] + cost

negativeCycle = False
for start, end, cost in edges:
    if dist[end] > dist[start] + cost:
        negativeCycle = True
        break

if negativeCycle:
    print(-1)
else:
    for i in range(1, N):
        if dist[i] < math.inf:
            print(dist[i])
        else:
            print(-1)
