import collections
import sys
input = sys.stdin.readline

iter = int(input())
for _ in range(iter):
    V, E = map(int, input().split())
    adj = [set() for i in range(V)]
    visit = [-1 for i in range(V)]
    
    for __ in range(E):
        start, end = map(int, input().split())
        adj[start-1].add(end-1)
        adj[end-1].add(start-1)
    
    bfsQueue = collections.deque()
    isBipartite = True
    for start in range(V):
        if visit[start] >= 0:
            continue
        bfsQueue.append(start)
        visit[start] = 0
        while bfsQueue:
            cur = bfsQueue.popleft()
            for next in adj[cur]:
                if visit[next] == -1:
                    bfsQueue.append(next)
                    visit[next] = (visit[cur] + 1) % 2
                elif visit[cur] == visit[next]:
                    isBipartite = False
            if not isBipartite:
                break
        if not isBipartite:
            break
    if isBipartite:
        print("YES")
    else:
        print("NO")
