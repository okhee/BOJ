"""
0 <= i < N

sum(W_i) <= K
maximize sum(V_i)

arr[i][k] = maximum total value when ith item is considered (~included~ -> nope!)
            where total weight is no greater than k

arr[i+1][k_2] = max(arr[i][k_2 - weight[i+1]], ) + value[i+1]

arr[i+1][k] -> 

1) if k >= weight[i+1]
    = max(arr[i][k - weight[i+1]] + value[i+1], \\
          arr[i][k])

2) if k < weight[i+1]
    = arr[i][k]

0 <= k <= K

arr -> 40,000,000 bytes

item sorted??

"""

# N = 4
# K = 7

# itemList = [(6, 13), (4, 8), (3, 6), (5, 12)]

[N, K] = list(map(int, input().split()))
itemList = [tuple(map(int, input().split())) for i in range(N)]

itemList.sort()

weight = [itemList[i][0] for i in range(len(itemList))]
value =  [itemList[i][1] for i in range(len(itemList))]

"""
itemList = [(3, 6), (4, 8), (5, 12), (6, 13)]

weight = [3, 4, 5, 6]
value =  [6, 8, 12, 13]

arr
i/k	0	1	2	3	4	5	6	7	8	9	10	11	12
0	0	0	0	6	6	6	6	6	6	6	6	6	6
1	0	0	0	6	8	8	8	14	14	14	14	14	14
2	0	0	0	6	8	12	12	14	18	20	20	20	20
3	0	0	0	6	8	12	13	14	18	20	21	25	25
"""

arr = [[0 for k in range(K + 1)] for i in range(N)]

for k in range(K + 1):
    if k >= weight[0]:
        arr[0][k] = value[0]

for i in range(1, N):
    for k in range(K + 1):
        if k >= weight[i]:
            arr[i][k] = max(arr[i - 1][k - weight[i]] + value[i],
                            arr[i - 1][k])
        else:
            arr[i][k] = arr[i - 1][k]

print(arr[N - 1][K], end="")
