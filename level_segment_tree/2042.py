class segTree:
    """
        Segment Tree Data Structure

        variables:
            N:    number of items, length of arr
            arr:  array of items
            H:    depth of tree
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
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.H = 1
        while self.N > 2**self.H:
            self.H += 1
        
        self.tree = [0 for _ in range(2**(self.H + 1))]
        self.initTree(nodeId=1, start=0, end=N-1)

    # start, end are index from arr, not tree
    def initTree(self, nodeId, start, end):
        if start == end:
            self.tree[nodeId] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.tree[nodeId] = self.initTree(nodeId * 2, start, mid) + \
                                self.initTree(nodeId * 2 + 1, mid + 1, end)
        return self.tree[nodeId]

    def updateTree(self, targetIdx, valDiff):
        """Wrapper function of __updateTree"""
        self.__updateTree(1, 0, self.N-1, targetIdx, valDiff)

    def __updateTree(self, nodeId, start, end, targetIdx, valDiff):
        # targetIdx not included in [start, end]
        if targetIdx < start or end < targetIdx:
            return
        # current leaf is target, targetIdx == start == end
        elif start == end:
            self.arr[targetIdx] += valDiff
            self.tree[nodeId] += valDiff
        # [start, end] includes targetIdx
        else:
            mid = (start + end) // 2
            self.__updateTree(nodeId * 2,     start,   mid, targetIdx, valDiff)
            self.__updateTree(nodeId * 2 + 1, mid + 1, end, targetIdx, valDiff)
            self.tree[nodeId] += valDiff

    def rangeSum(self, rangeStart, rangeEnd):
        """Wrapper function of __rangeSum"""
        return self.__rangeSum(1, 0, self.N-1, rangeStart, rangeEnd)

    def __rangeSum(self, nodeId, start, end, rangeStart, rangeEnd):
        # range and [start, end] matches, return its value
        if start == rangeStart and end == rangeEnd:
            return self.tree[nodeId]
        
        mid = (start + end) // 2
        if rangeEnd <= mid:
            return self.__rangeSum(nodeId * 2, start, mid, rangeStart, rangeEnd)
        elif rangeStart >= mid + 1:
            return self.__rangeSum(nodeId * 2 + 1, mid + 1, end, rangeStart, rangeEnd)
        else:
            return self.__rangeSum(nodeId * 2,     start,   mid, rangeStart, mid) + \
                   self.__rangeSum(nodeId * 2 + 1, mid + 1, end, mid + 1,    rangeEnd)

[N, M, K] = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]

a = segTree(N, arr)

for _ in range(M+K):
    cmd = list(map(int, input().split()))

    # change value
    if cmd[0] == 1:
        targetIdx = cmd[1] - 1
        valDiff = cmd[2] - a.arr[targetIdx]
        a.updateTree(targetIdx, valDiff)

    # print range sum
    elif cmd[0] == 2:
        print(a.rangeSum(cmd[1] - 1, cmd[2] - 1))
