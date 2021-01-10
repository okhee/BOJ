class largeRectSolver:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr
        self.maxRectArea = 0
        self.func(0, N)

    def getMaxRectArea(self):
        return self.maxRectArea

    def func(self, start, end):
        """
            Recursive function that separates range of interest and calls two sub-functions 

            param:
                start, end = index value of self.arr that specifies range of interest
                             which includes start point and 'excludes' end point, [start, end)

            returns:
                returns [A, B] where A = [(h1_a, w1_a), ...],  B = [(h1_b, w1_b), ...]
                'A' contains every rectangle informations tuple(height, (largest possible) width)
                    which starts from leftmost location of range of interest
                Similarly for 'B', rightmost.

            func divides range of interest as (start, mid) & (mid, end)
            and calls two recursive sub-functions.
            let each result be [A, B] and [C, D]
            Each A, B, C, D can be considered as 'entrance door' of either ranges.

            i) Updating self.maxRectArea
                We suppose rectangles which are located in either [A, B] or [C, D]
                are already checked if it is self.maxRectArea at base case, or sub-functions.
                So, We can only consider cases between B and C, where largest rectangle is
                located on 'mid', divided point. Calculate area, if it is largest, update.
            
            ii) Extend A and D
                After i), B and C are no longer needed.
        """
        if start + 1 == end:
            val = self.arr[start]
            if val > self.maxRectArea:
                self.maxRectArea = val
            return [[(val, 1)], [(val, 1)]]

        mid = (end + start) // 2
        firstRes = self.func(start, mid)
        firstLen = mid - start
        secondRes = self.func(mid, end)
        secondLen = end - mid

        # update maxRectArea
        for left in firstRes[1]:
            for right in secondRes[0]:
                height = min(left[0], right[0])
                width = left[1] + right[1]
                val = height * width
                if val > self.maxRectArea:
                    self.maxRectArea = val

        tmp = dict()
        for firstDoor in firstRes[0]:
            # firstDoor = (7, 2)
            # if we start from leftmost entrance,
            # we can find rectangle height of 7, width of 2

            # for each rectangle, if it can reach firstRes's end,
            # we can attach it to secondRes.
            if firstDoor[1] == firstLen:
                for secondDoor in secondRes[0]:
                    height = min(firstDoor[0], secondDoor[0])
                    width = (firstLen + secondDoor[1])
                    try:
                        tmp[height] = max(width, tmp[height])
                    except KeyError:
                        tmp[height] = width
            
            height, width = firstDoor[0], firstDoor[1]
            try:
                tmp[height] = max(width, tmp[height])
            except KeyError:
                tmp[height] = width
        nextLeftRes = list(zip(tmp.keys(), tmp.values()))

        tmp.clear()
        for firstDoor in secondRes[1]:
            if firstDoor[1] == secondLen:
                for secondDoor in firstRes[1]:
                    height = min(firstDoor[0], secondDoor[0])
                    width = (secondLen + secondDoor[1])
                    try:
                        tmp[height] = max(width, tmp[height])
                    except KeyError:
                        tmp[height] = width
            
            height, width = firstDoor[0], firstDoor[1]
            try:
                tmp[height] = max(width, tmp[height])
            except KeyError:
                tmp[height] = width

        nextRightRes = list(zip(tmp.keys(), tmp.values()))

        return [nextLeftRes, nextRightRes]

# N = 10000
# inputStr = " ".join(list(map(str, list(range(N)))))
# # # arr = list(map(int, "2 1 4 5 1 3 3".split()))
# arr = list(map(int, inputStr.split()))

import sys
input = sys.stdin.readline

while True:
    inputNumList = list(map(int, input().split()))
    if inputNumList[0] == 0:
        break
    a = largeRectSolver(inputNumList[0], inputNumList[1:])
    print(a.getMaxRectArea())
