import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
for _ in range(E):
    start, end, cost = map(int, input().split())
    heapq.heappush(edges, (cost, start, end))

parents = [i for i in range(V + 1)]
def ancestor(node):
    if parents[node] != node:
        parents[node] = ancestor(parents[node])
        return parents[node]
    else:
        return node

totalCost = 0
edgeCount = 0
while edges:
    cost, start, end = heapq.heappop(edges)
    if ancestor(start) == ancestor(end):
        continue

    parents[ancestor(start)] = end
    totalCost += cost
    edgeCount += 1

    if edgeCount == V-1:
        break
print(totalCost)
