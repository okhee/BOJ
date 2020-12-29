[N, S] = list(map(int, input().split()))

numList = list(map(int, input().split()))
numList.sort()
isChecked = [False for _ in range(len(numList))]

answer = 0

# n numbers checked,
def func(n, sum_):
    global answer

    if n == N:
        if sum_ == S and True in isChecked:
            answer += 1
        return
    # ----------FALSE----------
    # since numList is sorted,
    # whenever sum_ + next number exceeds S,
    # future sum_ will be no smaller than current val
    # if sum_ + numList[n] <= S:
    #------------------------------
    # sum_ + next number <= S can be possible
    # [-7, -6, -5], target = -18
    isChecked[n] = True
    func(n+1, sum_ + numList[n])
    isChecked[n] = False

    func(n+1, sum_)

func(0, 0)
print(answer, end="")
