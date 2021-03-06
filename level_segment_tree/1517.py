class segTree:
    """
        Segment Tree Data Structure

        variables:
            N:    number of items, length of array of items
            tree: balanced binary tree where leaves are each item, respectively
                  value of internal node is sum of value of its child nodes

        methods:
            __init__:   Constructor
            updateTree: update a tree according to updated item value
            rangeSum:   return sum of specified range

        N = 8, H = 3
        root (level 0) --->              1
            (level 1) --->       2             3
            (level 2) --->   4       5      6      7
        leaf (level H) ---> 0, 1,  2,  3,  4,  5,  6,  7   arrIdx
                            8, 9,  10, 11, 12, 13, 14, 15  nodeId
        
    """ 
    def __init__(self, N):
        self.N = N
        self.tree = [0 for _ in range(4 * self.N)]

    def updateTree(self, targetIdx):
        """Wrapper function of __updateTree"""
        self.__updateTree(1, 0, self.N-1, targetIdx)

    def __updateTree(self, nodeId, start, end, targetIdx):
        # targetIdx not included in [start, end]
        if targetIdx < start or end < targetIdx:
            return

        if start != end:
            mid = (start + end) // 2
            if targetIdx <= mid:
                self.__updateTree(nodeId * 2,     start,   mid, targetIdx)
            else:
                self.__updateTree(nodeId * 2 + 1, mid + 1, end, targetIdx)
        self.tree[nodeId] += 1

    def rangeSum(self, rangeStart, rangeEnd):
        """Wrapper function of __rangeSum"""
        return self.__rangeSum(1, 0, self.N-1, rangeStart, rangeEnd)

    def __rangeSum(self, nodeId, start, end, rangeStart, rangeEnd):
        if rangeEnd < start or end < rangeStart:
            return 0

        if rangeStart <= start and end <= rangeEnd:
            return self.tree[nodeId]

        mid = (start + end) // 2
        return self.__rangeSum(nodeId * 2, start, mid, rangeStart, rangeEnd) + \
               self.__rangeSum(nodeId * 2 + 1, mid + 1, end, rangeStart, rangeEnd)

import sys
input = sys.stdin.readline

N = int(input())
numList = list(zip( list(map(int, input().split())), list(range(N)) ))
numList.sort(key=lambda x: x[0])

ans = 0
seg = segTree(N)
for num, idx in numList:
    seg.updateTree(idx - 1)
    ans += seg.rangeSum(idx, N - 1)
print(ans, end="")
