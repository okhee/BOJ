import sys
input = sys.stdin.readline

dummy = input()
A = list(map(int, input().split()))
operNumList = list(map(int, input().split()))

operChar = ['+', '-', '*', '/']
maxRes = -10**10
minRes =  10**10

def calc(op):
    global A

    res = A[0]
    for i in range(len(op)):
        if op[i] == "+":
            res += A[i+1]
        elif op[i] == "-":
            res -= A[i+1]
        elif op[i] == "*":
            res *= A[i+1]
        elif op[i] == "/":
            if res >= 0:
                res //= A[i+1]
            else:
                res = -((-res) // A[i+1])
        
    return res

def record(op, operList, m):
    global operChar
    global maxRes
    global minRes

    if m == 0:
        val = calc(op)
        if val > maxRes:
            maxRes = val
        if val < minRes:
            minRes = val
        return
    
    for idx, operNum in enumerate(operList):
        if operNum > 0:
            newOp = op[:]
            newOp.append(operChar[idx])

            newOperList = operList[:]
            newOperList[idx] -= 1

            record(newOp, newOperList, m - 1)

record([], operNumList, sum(operNumList))

print(maxRes)
print(minRes, end="")
