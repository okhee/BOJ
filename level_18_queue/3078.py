import collections
import sys
input = sys.stdin.readline

# N persons, pair students at most K far away
N, K = map(int, input().split())

answer = 0
# At most K recent students information
window = collections.deque()
# For faster searching
windowDict = {k:0 for k in range(2, 21)}

for _ in range(N):
    nameLen = len(input().rstrip())
    # There are windowDict[nameLen] number of good friends
    answer += windowDict[nameLen]

    # window size at most K
    if len(window) == K:
        windowDict[window.popleft()] -= 1
    window.append(nameLen)
    windowDict[nameLen] += 1

print(answer, end="")
