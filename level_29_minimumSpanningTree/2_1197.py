import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

adj = [set() for _ in range(V + 1)]
for e in range(E):
    A, B, C = map(int, input().split())
    adj[A].add((B, C))
    adj[B].add((A, C))

visit = [False for _ in range(V + 1)]
visit[0] = True
heap = [(0, 1)]
totalCost = 0

while not all(visit):
    cost, curNode = heapq.heappop(heap)
    if visit[curNode]:
        continue
    visit[curNode] = True
    totalCost += cost

    for nextNode, cost in adj[curNode]:
        if visit[nextNode]:
            continue
        heapq.heappush(heap, (cost, nextNode))
print(totalCost)
