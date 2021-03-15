import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

inward = [set() for _ in range(N+1)]
outward = [set() for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    inward[end].add(start)
    outward[start].add(end)

heap = []
for i in range(1, N+1):
    if len(inward[i]) == 0:
        heap.append(i)

answer = []
while heap:
    curNode = heapq.heappop(heap)
    answer.append(str(curNode))

    for outNode in outward[curNode]:
        # outward[curNode].remove(outNode)
        inward[outNode].remove(curNode)
        if outNode not in heap and len(inward[outNode]) == 0:
            heap.append(outNode)
print(" ".join(answer))
