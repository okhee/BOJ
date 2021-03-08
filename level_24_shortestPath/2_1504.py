import heapq
import math
import sys
input = sys.stdin.readline

N, E = map(int, input().split())

adj = [set() for _ in range(N)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    adj[start-1].add((cost, end-1))
    adj[end-1].add((cost, start-1))

midNode1, midNode2 = map(int, input().split())
midNode1 -= 1
midNode2 -= 1

def dijkstra(startNode, endNode):
    global adj

    distList = [math.inf for _ in range(N)]
    distHeap = [(math.inf, i) for i in range(N)]
    prev = [None for i in range(N)]
    nodes = {i for i in range(N)}

    distList[startNode] = 0
    heapq.heappush(distHeap, (0, startNode))

    while nodes:
        curDist, curNode = heapq.heappop(distHeap)
        if curNode not in nodes:
            continue
        nodes.remove(curNode)

        for nextDist, nextNode in adj[curNode]:
            newDist = curDist + nextDist
            if newDist < distList[nextNode]:
                distList[nextNode] = newDist
                heapq.heappush(distHeap, (newDist, nextNode))
                prev[nextNode] = curNode
    return distList[endNode]

ans1 = dijkstra(0, midNode1) + dijkstra(midNode1, midNode2) + dijkstra(midNode2, N-1)
ans2 = dijkstra(0, midNode2) + dijkstra(midNode2, midNode1) + dijkstra(midNode1, N-1)
ans = min(ans1, ans2)
if ans < math.inf:
    print(ans)
else:
    print(-1)
