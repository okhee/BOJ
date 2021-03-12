import math
import sys
input = sys.stdin.readline

T = int(input())
for iter in range(T):
    K = int(input())
    numList = [[] for _ in range(K+1)]
    costList = [[] for _ in range(K+1)]
    numList[1] = list(map(int, input().split()))
    costList[1] = [0] * K

    for curLen in range(2, K+1):
        for j in range(K - curLen + 1):
            numList[curLen].append(numList[curLen-1][j] + numList[1][j + curLen - 1])
            costList[curLen].append(math.inf)

            for joint in range(curLen - 1):
                costsum = numList[curLen][j] + costList[joint+1][j] + costList[curLen - joint - 1][j + joint + 1]
                if costsum < costList[curLen][j]:
                    costList[curLen][j] = costsum

    # print(numList)
    print(costList[-1][0])

    # curLen = 4
    # j = 0
    # # for joint in range(curLen - 1):
    # joint = 0
    #     numList[1][0] + numList[3][1]
    # joint = 1
    #     numList[2][0] + numList[2][2]
    # joint = 2
    #     numList[3][0] + numList[1][3]


