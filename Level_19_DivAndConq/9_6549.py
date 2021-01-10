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
                returns [A, D] where A = [(h1_a, w1_a), ...],  D = [(h1_d, w1_d), ...]
                'A' contains every rectangle informations tuple(height, (largest possible) width)
                    which starts from leftmost location of range of interest
                Similarly for 'D', rightmost.

            func divides range of interest as (start, mid) & (mid, end)
            and calls two recursive sub-functions.
            let each result be [A, B] and [C, D]
            Each A, B, C, D can be considered as 'entrance door' of either ranges.

            i) Updating self.maxRectArea
                We suppose rectangles which are only located in either [A, B] or [C, D]
                are already checked if it is largest rectangle during base case or sub-functions.
                So, We can only consider cases between B and C, where largest rectangle is
                located on 'mid', divided point. Calculate area, if it is largest, update.
            
            ii) Extend A and D
                If rectangle in A can reach (mid, end) range, we must update its information since
                it can be extended by appending possible rectangle from C ('left' entrance door of (mid, end))
                Similarly with D and B, too. 

            iii) Return
                Every information related to B and C are used after i) and ii).
                So, B and C are no longer needed.
                We then return [(extended) A, (extended) D]
        """

        # Base case when there is only one item
        if start + 1 == end:
            val = self.arr[start]
            if val > self.maxRectArea:
                self.maxRectArea = val
            return [[(val, 1)], [(val, 1)]]

        # Split range and call recursive sub-functions
        # firstRes = [A, B], secondRes = [C, D]
        mid = (end + start) // 2
        firstRes = self.func(start, mid)
        firstLen = mid - start
        secondRes = self.func(mid, end)
        secondLen = end - mid

        # i) Updating self.maxRectArea
        for left in firstRes[1]:
            for right in secondRes[0]:
                height = min(left[0], right[0])
                width = left[1] + right[1]
                val = height * width
                if val > self.maxRectArea:
                    self.maxRectArea = val

        # ii-1) Extend A where firstRes = [A, B]
        tmp = dict()
        for firstDoor in firstRes[0]:
            # for firstDoor = (7, 2) as an example,
            # if we start from leftmost entrance,
            # we can find rectangle height of 7, width of 2

            # for each rectangle, if it can reach 'mid',
            # we can attach it to rectangle from C where secondRes = [C, D]
            if firstDoor[1] == firstLen:
                for secondDoor in secondRes[0]:
                    height = min(firstDoor[0], secondDoor[0])
                    width = (firstLen + secondDoor[1])
                    try:
                        tmp[height] = max(width, tmp[height])
                    except KeyError:
                        tmp[height] = width
            # Add rectangle that has not been extended to new A list
            height, width = firstDoor[0], firstDoor[1]
            try:
                tmp[height] = max(width, tmp[height])
            except KeyError:
                tmp[height] = width
        nextLeftRes = list(zip(tmp.keys(), tmp.values()))

        # ii-2) Extend D where secondRes = [C, D]
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

        # iii) Return extended [A, D]
        return [nextLeftRes, nextRightRes]

# N = 10000
# inputStr = " ".join(list(map(str, list(range(N)))))
# arr = list(map(int, inputStr.split()))

import sys
input = sys.stdin.readline

while True:
    inputNumList = list(map(int, input().split()))
    if inputNumList[0] == 0:
        break
    a = largeRectSolver(inputNumList[0], inputNumList[1:])
    print(a.getMaxRectArea())
