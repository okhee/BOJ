"""
arr[i] -> (r, g, b)
minimum value of cost when ith house chose r, g, b, respectively

arr = [(26, 40, 83), ()]
arr[i].r = min(arr[i-1].g, arr[i-1].b) + cost[i].r
"""
N = int(input())
# cost = [[], [26, 40, 83], [49, 60, 57], [13, 89, 99]]
cost = [[]] + [list(map(int, input().split())) for _ in range(N)]

arr = [(0, 0, 0)]

for i in range(1, N+1):
    redCost =   min(arr[i-1][1], arr[i-1][2]) + cost[i][0]
    greenCost = min(arr[i-1][2], arr[i-1][0]) + cost[i][1]
    blueCost =  min(arr[i-1][0], arr[i-1][1]) + cost[i][2]

    arr.append((redCost, greenCost, blueCost))

print(min(arr[N]), end="")
