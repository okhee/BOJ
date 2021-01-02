"""
numList = [10, 20, 10, 30, 20, 50]
arr = [0: [0], 1: [10], 2: [20], 3: [30], 4: [50]]

numList = [10, 20, 15, 30, 21, 32, 50]
arr = [0: [0], 1: [min(10, 15)], 2: [20], 3: [min(21, 30)], 4: [32], 5:[50]]
"""

N = int(input())
numList = list(map(int, input().split()))

arr = [0]

# return maximum index value where arr[idx] value is smaller than key 
# O(logN)
def binSearch(start, end, key):
    global arr

    if start == end:
        return start if arr[start] < key else (start - 1)
            
    mid = (start + end) // 2

    if arr[mid] >= key:
        return binSearch(start, mid, key)
    else:
        return binSearch(mid + 1, end, key)

for i in range(N):
    # append numList[i] item to previous array
    # to make longest array possible
    maxIdx = binSearch(0, len(arr) - 1, numList[i])
    
    # update arr
    if maxIdx == len(arr) - 1:
        arr.append(numList[i])
    else:
        arr[maxIdx + 1] = min(arr[maxIdx + 1], numList[i])

print(len(arr) - 1, end="")
