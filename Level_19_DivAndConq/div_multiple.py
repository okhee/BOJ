[A, B, C] = [10, 11, 12]

def mult(A, B):
    alen, blen = len(str(A)), len(str(B))
    if alen == 1 and blen == 1:
        return A*B

    a1, a2 = 0, A
    b1, b2 = 0, B

    if alen > 1:
        a1 = int(str(A)[:alen//2])
        a2 = int(str(A)[alen//2:])
    
    if blen > 1:
        b1 = int(str(B)[:blen//2])
        b2 = int(str(B)[blen//2:])

    return mult(a1, b1) * 10**((alen+1)//2 + (blen+1)//2) + \
           mult(a1, b2) * 10**((alen+1)//2) + \
           mult(a2, b1) * 10**((blen+1)//2) + \
           mult(a2, b2)

print(mult(A, B) % C, end="")
