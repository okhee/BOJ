import math
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numList = list(map(int, input().split()))

answer = math.inf
s, e = 0, 0
subsum = 0
while True:
    if subsum >= S:
        subsum -= numList[s]
        s += 1
    elif e == N:
        break
    else:
        subsum += numList[e]
        e += 1

    if subsum >= S:
        if (e - s) < answer:
            answer = (e - s)
if answer < math.inf:
    print(answer)
else:
    print(0)
