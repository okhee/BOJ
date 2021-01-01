# N = 6
# score = [0, 10, 20, 15, 25, 10, 20]
N = int(input())
score = [0] + [int(input()) for _ in range(N)]

step = [(0, 0)]
step.append((score[1], score[1]))
"""
reached ith step,
step[i] = (a, b)
        a: if ith step is reached with one step size
        b: two step size

a = step[i-1].b + score[i]
b = max(step[i-2].a, step[i-2].b) + score[i]
"""

for i in range(2, N+1):
    step.append((step[i-1][1] + score[i], max(step[i-2]) + score[i]))

print(max(step[N]), end="")
