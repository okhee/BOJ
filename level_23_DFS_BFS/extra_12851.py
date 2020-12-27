import sys
import collections

input = sys.stdin.readline

[N, K] = list(map(int, input().split()))
visit = [0 for _ in range(100001)]

bfsQueue = collections.deque()
bfsQueue.append(N)
visit[N] = 1

while len(bfsQueue) > 0:
    cur = bfsQueue.popleft()
    for nxt in (cur-1, cur+1, 2*cur):
        if nxt < 0 or nxt > 100000:
            continue
        if visit[nxt] > 0:
            continue
        bfsQueue.append(nxt)
        visit[nxt] = visit[cur] + 1

degree = visit[K]
candidate = [K]
nextCandidate = []
while degree > 1:
    nextCandidate.clear()
    for i in candidate:
        if i % 2 == 0:
            nextCandidate.append(i//2)
        if i > 0:
            nextCandidate.append(i - 1)
        if i < 100000:
            nextCandidate.append(i + 1)

    candidate.clear()
    for i in nextCandidate:
        if visit[i] == degree - 1:
            candidate.append(i)

    degree -= 1

print(visit[K] - 1)
print(len(candidate), end="")
