class segTree:
    """
        Segment Tree Data Structure

        variables:
            N:    number of items, length of arr
            arr:  array of items
            H:    depth of tree
            tree: balanced binary tree where leaves are each item, respectively
                  value of internal node is (min, max) of value of its child nodes

        methods:
            __init__: Constructor
            minMax:   return (min, max) of specified range

        N = 8, H = 3
        root (level 0) --->              1
            (level 1) --->       2             3
            (level 2) --->   4       5      6      7
        leaf (level H) ---> 0, 1,  2,  3,  4,  5,  6,  7   arrIdx
                            8, 9,  10, 11, 12, 13, 14, 15  nodeId
        
    """ 
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.H = 1
        while self.N > 2**self.H:
            self.H += 1
        
        self.tree = [[1<<30, 0] for _ in range(2**(self.H + 1))]
        self.initTree(nodeId=1, start=0, end=N-1)

    # start, end are index from arr, not tree
    def initTree(self, nodeId, start, end):
        if start == end:
            self.tree[nodeId] = (self.arr[start], ) * 2
        else:
            mid = (start + end) // 2
            leftRes = self.initTree(nodeId * 2, start, mid)
            rightRes = self.initTree(nodeId * 2 + 1, mid + 1, end)
            self.tree[nodeId] = (min(leftRes[0], rightRes[0]), max(leftRes[1], rightRes[1]))
        return self.tree[nodeId]

    def minMax(self, rangeStart, rangeEnd):
        """Wrapper function of __minMax"""
        return self.__minMax(1, 0, self.N-1, rangeStart, rangeEnd)

    def __minMax(self, nodeId, start, end, rangeStart, rangeEnd):
        # range and [start, end] matches, return its value
        if start == rangeStart and end == rangeEnd:
            return self.tree[nodeId]
        
        mid = (start + end) // 2
        if rangeEnd <= mid:
            return self.__minMax(nodeId * 2, start, mid, rangeStart, rangeEnd)
        elif rangeStart >= mid + 1:
            return self.__minMax(nodeId * 2 + 1, mid + 1, end, rangeStart, rangeEnd)
        else:
            leftRes =  self.__minMax(nodeId * 2,     start,   mid, rangeStart, mid)
            rightRes = self.__minMax(nodeId * 2 + 1, mid + 1, end, mid + 1,    rangeEnd)
            return (min(leftRes[0], rightRes[0]), max(leftRes[1], rightRes[1]))

import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]

a = segTree(N, arr)

for _ in range(M):
    cmd = list(map(int, input().split()))
    res = a.minMax(cmd[0] - 1, cmd[1] - 1)
    print(f'{res[0]} {res[1]}')
