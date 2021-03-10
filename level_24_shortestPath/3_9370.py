import heapq
import math
import sys

input = sys.stdin.readline

T = int(input())
for iteration in range(T):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())

    gh = math.inf
    adj = [set() for _ in range(N+1)]
    destination = []
    for _ in range(M):
        a, b, d = map(int, input().split())
        adj[a].add((d, b))
        adj[b].add((d, a))
        if (a, b) in [(G, H), (H, G)]:
            gh = d
    for _ in range(T):
        heapq.heappush(destination, int(input()))

    def dijkstra(start):
        dist = [math.inf for _ in range(N+1)]
        dist[start] = 0
        prev = [None for _ in range(N+1)]
        heap = [(0, start)]
        while heap:
            curDist, curNode = heapq.heappop(heap)

            if dist[curNode] < curDist:
                continue

            for nextDist, nextNode in adj[curNode]:
                nextDist += curDist
                if nextDist < dist[nextNode]:
                    dist[nextNode] = nextDist
                    prev[nextNode] = curNode
                    heapq.heappush(heap, (nextDist, nextNode))
        return dist
        
    fromS, fromG, fromH = dijkstra(S), dijkstra(G), dijkstra(H)
    res = []
    while destination:
        destNode = heapq.heappop(destination)
        if fromS[destNode] >= math.inf:
            continue

        # Attention!
        # We have confidence of existence of route only on edge (g, h)
        # For (s -> g), (h -> destination), (s -> h), (g -> destination),
        # we must ensure that we can reach one node from another first!
        route = []
        if fromS[G] < math.inf and fromH[destNode] < math.inf:
            route.append(fromS[G] + gh + fromH[destNode])
        if fromS[H] < math.inf and  fromG[destNode] < math.inf:
            route.append(fromS[H] + gh + fromG[destNode])

        if fromS[destNode] in route:
            res.append(str(destNode))
    print(" ".join(res))
