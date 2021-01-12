class segTree:
    """
        Segment Tree Data Structure

        variables:
            N:    number of items, length of arr
            arr:  array of items
            tree: balanced binary tree where leaves are each item, respectively
                  value of internal node is product of value of its child nodes

        methods:
            __init__:   Constructor
            updateTree: update a tree according to updated item value
            product:   return product of specified range

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

        self.tree = [1 for _ in range(4 * self.N)]
        self.zeroTree = [0 for _ in range(4 * self.N)]
        self.initTree(nodeId=1, start=0, end=N-1)

    # start, end are index of arr, not tree
    def initTree(self, nodeId, start, end):
        if start == end:
            if self.arr[start] > 0:
                self.tree[nodeId] = self.arr[start]
            else:
                # zero is stored as 0 in arr and 1 in tree
                self.zeroTree[nodeId] = 1
        else:
            mid = (start + end) // 2
            leftVal = self.initTree(nodeId * 2, start, mid)
            rightVal = self.initTree(nodeId * 2 + 1, mid + 1, end)

            self.tree[nodeId] = (leftVal * rightVal) % 1000000007
            self.zeroTree[nodeId] = self.zeroTree[nodeId * 2] + \
                                    self.zeroTree[nodeId * 2 + 1]
        return self.tree[nodeId]

    def updateTree(self, targetIdx, newVal):
        """Wrapper function of __updateTree"""
        self.__updateTree(1, 0, self.N-1, targetIdx, self.arr[targetIdx], newVal)

    def __updateTree(self, nodeId, start, end, targetIdx, originVal, newVal):
        # targetIdx not included in [start, end]
        if targetIdx < start or end < targetIdx:
            return
         
        # current leaf is target, targetIdx == start == end
        if start == end:
            self.arr[targetIdx] = newVal
            if newVal > 0:
                self.tree[nodeId] = newVal
                self.zeroTree[nodeId] = 0
            else:
                self.tree[nodeId] = 1
                self.zeroTree[nodeId] = 1

        # [start, end] includes targetIdx but is not leaf
        else:
            mid = (start + end) // 2
            # only call sub-function on either of its child (788ms -> 724ms)
            if targetIdx <= mid:
                self.__updateTree(nodeId * 2,     start,   mid, targetIdx, originVal, newVal)
            else:
                self.__updateTree(nodeId * 2 + 1, mid + 1, end, targetIdx, originVal, newVal)

            self.tree[nodeId] = (self.tree[nodeId * 2] * self.tree[nodeId * 2 + 1]) % 1000000007
            if originVal > 0 and newVal == 0:
                self.zeroTree[nodeId] += 1
            elif originVal == 0 and newVal > 0:
                self.zeroTree[nodeId] -= 1

    def product(self, rangeStart, rangeEnd):
        """Wrapper function of __product"""
        return self.__product(1, 0, self.N-1, rangeStart, rangeEnd)

    def __product(self, nodeId, start, end, rangeStart, rangeEnd):
        if rangeEnd < start or end < rangeStart:
            return 1

        if rangeStart <= start and end <= rangeEnd:
            if self.zeroTree[nodeId] > 0:
                return 0
            return self.tree[nodeId]
        
        mid = (start + end) // 2
        return (self.__product(nodeId * 2, start, mid, rangeStart, rangeEnd) * \
               self.__product(nodeId * 2 + 1, mid + 1, end, rangeStart, rangeEnd)) % 1000000007

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

a = segTree(N, arr)

for _ in range(M+K):
    cmd = list(map(int, input().split()))

    # change value
    if cmd[0] == 1:
        targetIdx = cmd[1] - 1
        newVal = cmd[2]
        a.updateTree(targetIdx, newVal)

    # print range product
    elif cmd[0] == 2:
        print(a.product(cmd[1] - 1, cmd[2] - 1) % 1000000007)
