import collections
import sys
input = sys.stdin.readline

N = int(input())
adj = [set() for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].add(end)
    adj[end].add(start)

visit = [-1 for _ in range(N+1)]
bfsQueue = collections.deque()
bfsQueue.append(1)
visit[1] = 0

while bfsQueue:
    cur = bfsQueue.popleft()
    for next in adj[cur]:
        if visit[next] >= 0:
            continue
        bfsQueue.append(next)
        visit[next] = cur

for idx, parent in enumerate(visit):
    if idx in (0, 1):
        continue
    print(parent)

