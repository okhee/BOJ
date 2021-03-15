import collections
import sys
input = sys.stdin.readline

N = int(input())
outward = [set() for _ in range(N+1)]
inward = [set() for _ in range(N+1)]
build = [0 for _ in range(N+1)]
total = [0 for _ in range(N+1)]

for i in range(1, N+1):
    time, *reqList = map(int, input().split())
    build[i] = time
    for req in reqList:
        if req < 0:
            continue
        inward[i].add(req)
        outward[req].add(i)

queue = collections.deque()
for i in range(1, N+1):
    if len(inward[i]) == 0:
        queue.append(i)

while queue:
    curNode = queue.popleft()
    total[curNode] += build[curNode]

    for nextNode in outward[curNode]:
        if total[curNode] > total[nextNode]:
            total[nextNode] = total[curNode]
        inward[nextNode].remove(curNode)

        if nextNode not in queue and len(inward[nextNode]) == 0:
            queue.append(nextNode)

for i in range(1, N+1):
    print(total[i])
