import collections
import sys
input = sys.stdin.readline

T = int(input())
for iter in range(T):
    N = int(input())

    inward = [0 for _ in range(N+1)]
    outward = [set() for _ in range(N+1)]

    prevRank = list(map(int, input().split()))

    switch = set()
    M = int(input())
    for m in range(M):
        start, end = map(int, input().split())
        switch.add((start, end))

    for idx, start in enumerate(prevRank):
        for eidx in range(idx+1, len(prevRank)):
            end = prevRank[eidx]
            inward[end] += 1
            outward[start].add(end)

    for a, b in switch:
        if b in outward[a]:
            outward[a].remove(b)
            inward[b] -= 1

            outward[b].add(a)
            inward[a] += 1

        elif a in outward[b]:
            outward[b].remove(a)
            inward[a] -= 1

            outward[a].add(b)
            inward[b] += 1

    queue = collections.deque()
    for i in range(1, N+1):
        if inward[i] == 0:
            queue.append(i)

    answer = []
    definiteAnswer = True
    while queue:
        curNode = queue.popleft()
        answer.append(str(curNode))
        for nextNode in outward[curNode]:
            inward[nextNode] -= 1
            if inward[nextNode] == 0:
                queue.append(nextNode)
        if len(queue) > 1:
            definiteAnswer = False
            break
    
    # cycle exists, inconsistency in data input
    dataConsistency = True
    for i in inward:
        if i > 0:
            dataConsistency = False
            break

    if not dataConsistency:
        print("IMPOSSIBLE")
    elif not definiteAnswer or len(answer) != N:
        print("?")
    else:
        print(" ".join(answer))
