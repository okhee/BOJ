import collections
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

inward = [0 for _ in range(N+1)]
outward = [set() for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    inward[end] += 1
    outward[start].add(end)

queue = collections.deque()
for i in range(1, N+1):
    if inward[i] == 0:
        queue.append(i)

answer = []
while queue:
    curNode = queue.popleft()
    answer.append(str(curNode))
    for nextNode in outward[curNode]:
        inward[nextNode] -= 1
        if inward[nextNode] == 0:
            queue.append(nextNode)

print(" ".join(answer))
