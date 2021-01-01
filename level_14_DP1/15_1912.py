"""
num[i]

arr[i] -> maximum sub sum where we include i
if arr[i] < 0, we set as 0

10, 6, 9, 10, 15, 21, -14, -2, 19, 18
10, 6, 9, 10, 15, 21, 

"""
# N = 10
# num = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
N = int(input())
numList = list(map(int, input().split()))

arr = [numList[0]]
for i in range(1, N):
    arr.append(max(0, arr[i-1]) + numList[i])
        
print(max(arr), end="")
