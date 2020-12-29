N = int(input())
arr = [int(input()) for _ in range(N)]

def merge(s, e):
    global arr

    if s >= e:
        return
    if e == s+1:
        if arr[s] > arr[e]:
            arr[s], arr[e] = arr[e], arr[s]
        return

    mid = (s + e) // 2
    merge(s, mid - 1)
    merge(mid, e)
    
    larr, rarr = arr[s:mid], arr[mid:e+1]
    lidx, ridx = 0, 0
    idx = s

    while (lidx < len(larr) and ridx < len(rarr)):
        if larr[lidx] <= rarr[ridx]:
            arr[idx] = larr[lidx]
            lidx += 1
        else:
            arr[idx] = rarr[ridx]
            ridx += 1
        idx += 1

    while lidx < len(larr):
        arr[idx] = larr[lidx]
        lidx += 1
        idx += 1

    while ridx < len(rarr):
        arr[idx] = rarr[ridx]
        ridx += 1
        idx += 1

merge(0, len(arr) - 1)
print("\n".join(list(map(str, arr))), end="")
