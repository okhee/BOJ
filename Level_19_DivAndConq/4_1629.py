# [A, B, C] = [10, 11, 12]
[A, B, C] = list(map(int, input().split()))

def mult(A, B):
    if B == 0:
        return 1 % C
    elif B == 1:
        return A % C
    
    tmp = mult(A, B // 2)
    if B % 2 == 0:
        return (tmp * tmp) % C
    else:
        return (tmp * tmp * A) % C

print(mult(A, B), end="")
