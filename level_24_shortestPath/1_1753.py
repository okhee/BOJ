import heapq
import math
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
init = int(input()) - 1

distList = [math.inf for i in range(V)]
distList[init] = 0
distHeap = [(math.inf, i) for i in range(V)]
prev = [None for _ in range(V)]

adj = [set() for _ in range(V)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    adj[start-1].add((end-1, cost))

heapq.heappush(distHeap, (0, init))
nodes = {i for i in range(V)}

while nodes:
    curDist, curNode = heapq.heappop(distHeap)
    if curNode not in nodes:
        continue
    nodes.remove(curNode)

    for nextNode, nextDist in adj[curNode]:
        newDist = curDist + nextDist
        if newDist < distList[nextNode]:
            distList[nextNode] = newDist
            heapq.heappush(distHeap, (newDist, nextNode))
            prev[nextNode] = curNode

res = []
for i in range(V):
    if distList[i] < math.inf:
        res.append(str(distList[i]))
    else:
        res.append("INF")
print("\n".join(res), end="")
