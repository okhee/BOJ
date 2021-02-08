import collections
import sys
input = sys.stdin.readline

# Length of square board
N = int(input())
# Number of apples
K = int(input())

# Moving distance in i-axis, j-axis for each direction
# direc is in counter-clockwise order
direcList = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# Location of apple
apple = [[False for j in range(N)] for i in range(N)]
# Rotation direction and timing
rotateList = collections.deque()

for _ in range(K):
    i, j = map(int, input().split())
    apple[i - 1][j - 1] = True

L = int(input())
for _ in range(L):
    time, rotate = input().split()
    rotate = 1 if rotate == "L" else -1
    rotateList.append((int(time), rotate))

# Location of snake body
# index 0: tail, index length-1: head
snake = collections.deque()
snake.append((0, 0))
direc = 0

globalTime = 0
while True:
    di, dj = direcList[direc]

    # Move head
    head = snake[-1]
    head = (head[0] + di, head[1] + dj)
    # If collision, terminate
    if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
        break
    if head in snake:
        break

    snake.append(head)

    # Ate apple
    if apple[head[0]][head[1]]:
        apple[head[0]][head[1]] = False
    # Move tail
    else:
        snake.popleft()

    globalTime += 1
    
    # After moving process, rotate
    if len(rotateList) > 0 and rotateList[0][0] == globalTime:
        rotate = rotateList.popleft()[1]
        direc = (direc + rotate) % 4

print(globalTime + 1)
