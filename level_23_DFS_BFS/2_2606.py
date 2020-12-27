import collections

N = int(input())
M = int(input())

visit = [0 for i in range(N + 1)]
edgeList = [set() for i in range(N + 1)]

bfsQueue = collections.deque()

for m in range(M):
    edge = list(map(int, input().split()))
    edgeList[edge[0]].add(edge[1])
    edgeList[edge[1]].add(edge[0])

for n in range(len(edgeList)):
    edgeList[n] = sorted(list(edgeList[n]))

# BFS-----------------
# init Queue
bfsQueue.append(1)
visit[1] = 1

while len(bfsQueue) > 0:
    cur = bfsQueue.popleft()
    for nxt in edgeList[cur]:
        if visit[nxt] > 0:
            continue
        bfsQueue.append(nxt)
        visit[nxt] = 1

print(sum(visit) - 1, end="")
