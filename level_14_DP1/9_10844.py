"""
0 -> 1
1 -> 0, 2
2 -> 1, 3

arr[i] -> 
arr[1] = 9
((0), (1), (2), 3, 4, 5, 6, 7, 8, 9)
(1, 1, 1, 1, 1, 1, 1, 1, 1, 1) - 1


arr[2] = 17
((01), (10, 12), (21, 23), (32, 34), ..., 87, 89, 98)
(1, 2, 2, 2, 2, 2, 2, 2, 2, 1) - 1

arr[3]
((010, 012), (101, 121, 123), (210, 212, 232, 234), ())
(2, 3, 4, 4, 4, 4, 4, 4, 3, 2) - 2
"""
N = int(input())

arr = [1 for _ in range(10)]

for _ in range(2, N+1):
    tmp = []
    for j in range(10):
        if j == 0:
            tmp.append(arr[1])
        elif j == 9:
            tmp.append(arr[8])
        else:
            tmp.append(arr[j-1] + arr[j+1])
    arr = tmp
print((sum(arr) - arr[0])%1000000000, end="")
