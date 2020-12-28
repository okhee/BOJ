import collections

# get input
[N, M, V] = list(map(int, input().split()))

# To remove duplicated vertices, use set
edgeList = [set() for i in range(N + 1)]

for m in range(M):
    edge = list(map(int, input().split()))
    edgeList[edge[0]].add(edge[1])
    edgeList[edge[1]].add(edge[0])

# using sorted list, since we visit smaller # vertex first
for n in range(len(edgeList)):
    edgeList[n] = sorted(list(edgeList[n]))

# i) --------------------DFS------------------------
# init Stack
visit = [-1 for i in range(N + 1)]

dfsStack = []
dfsTourList = []

dfsStack.append(V)

# Visiting # vertex is delayed until we pop this out of stack
# Since there might be shorter path while traversing down the depth
while len(dfsStack) > 0:
    cur = dfsStack.pop()
    if visit[cur] > 0:
        continue
    visit[cur] = 1
    dfsTourList.append(str(cur))

    # small # vertex has higher priority
    for nxt in reversed(edgeList[cur]):
        if visit[nxt] > 0:
            continue
        dfsStack.append(nxt)

# ii) ---------------------BFS-------------------------
# init Queue
visit = [-1 for i in range(N + 1)]

bfsQueue = collections.deque()
bfsTourList = []

bfsQueue.append(V)
bfsTourList.append(str(V))
visit[V] = 1

while len(bfsQueue) > 0:
    cur = bfsQueue.popleft()
    for nxt in edgeList[cur]:
        if visit[nxt] > 0:
            continue
        bfsQueue.append(nxt)
        bfsTourList.append(str(nxt))
        visit[nxt] = visit[cur] + 1


print(" ".join(dfsTourList))
print(" ".join(bfsTourList), end="")
