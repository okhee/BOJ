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
  
print(visit[K] - 1, end="")
