"""
0 ~ N-1 city
d[0] = distance between 0~1
d[N-2] = distance between (N-2)~(N-1)

"""
N = int(input())

dist = list(map(int, input().split()))
price = list(map(int, input().split()))

totalPrice = 0
currPrice = price[0]
currLoc = 0
for i in range(1, N):
    if price[i] < currPrice or (i == N-1):
        totalPrice += currPrice * sum(dist[currLoc:i])
        currPrice = price[i]
        currLoc = i
print(totalPrice, end="")
