# A = "ACAYKP"
# B = "CAPCAK"

A = input()
B = input()

# arr[a][b] -> maximum LCS length when at most ath char of A (A[a-1])
# and bth char of B (B[b-1]) are checked
arr = [[0 for b in range(len(B)+1)] for a in range(len(A)+1)]

for a in range(1, len(A)+1):
    for b in range(1, len(B)+1):
        if A[a-1] == B[b-1]:
            arr[a][b] = arr[a-1][b-1] + 1
        else:
            arr[a][b] = max(arr[a-1][b], arr[a][b-1])

print(max(list(map(max, arr))), end="")
