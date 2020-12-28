def idx(r, c, N):
    if N == 1:
        return 2 * r + c
    
    next_n = N - 1
    next_side_len = 1 << next_n

    r_off = 0 if r < next_side_len else 1
    c_off = 0 if c < next_side_len else 1

    idx_off = (2 * r_off + c_off) * (next_side_len ** 2)
    return idx_off + idx(r - r_off * next_side_len, c - c_off * next_side_len, next_n)


[N, R, C] = list(map(int, input().split()))
print(idx(R, C, N), end="")

'''
    N = 2
    L = 4

    0 ~ 15  (L**2)

    0  1  2  3  
    0  1  4  5

    4  5  6  7  
    2  3  6  7

    8   9   10  11
    8   9   12  13

    12  13  14  15
    10  11  14  15

    idx(i, N)
        if N == 1:
            return i
        next_n = N // 2
        # next_n = 1

        local_index?
        i 로 사분면 파악 가능?
        r >, <= next_n
        c


        return (x-1) 사분면 * next_n ** 2 + idx(local_index, next_n)
     
    N = 1
    L = 2

    0 ~ 3 (L**2)

    0   1
    0   1

    2   3 
    2   3

    idx(i, N)
        if N == 1:
            return i

'''
