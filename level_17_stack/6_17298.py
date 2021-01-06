
# A = [3, 2, 1, 3, 1, 9, 8]
"""
bottom
8, -1
9, -1
1, 9
3, 9
2, 3 -> 3 is leftmost bigger number than 2
        lost info about 9
3, -1 -> 9

stack
8
9
3

새 숫자가 같거나 크면 stack에서 계속 pop,
그 다음 새 숫자를 push

"""
N = int(input())
A = list(map(int, input().split()))

nge = []
stack = []

elem = A.pop()
stack.append(elem)
nge.append(-1)

while len(A) > 0:
    elem = A.pop()
    top = stack[-1]
    noNGE = False
    while top <= elem:
        stack.pop()
        if len(stack) == 0:
            noNGE = True
            break
        top = stack[-1]

    stack.append(elem)

    if noNGE:
        nge.append(-1)
    else:
        nge.append(top)

nge = [str(nge[i]) for i in reversed(range(len(nge)))]
print(" ".join(nge), end="")
