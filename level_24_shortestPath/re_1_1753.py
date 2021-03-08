import heapq
import math
V, E = map(int, input().split())
init = int(input())

adj = [set() for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    adj[start].add((cost, end))

dist = [math.inf for _ in range(V+1)]
dist[init] = 0
heap = [(0, init)]
while heap:
    curDist, curNode = heapq.heappop(heap)
    if dist[curNode] < curDist:
        continue

    for nextDist, nextNode in adj[curNode]:
        nextDist = curDist + nextDist
        if nextDist < dist[nextNode]:
            dist[nextNode] = nextDist
            heapq.heappush(heap, (nextDist, nextNode))

res = []
for i in range(1, V+1):
    if dist[i] < math.inf:
        res.append(str(dist[i]))
    else:
        res.append("INF")
print("\n".join(res), end="")
