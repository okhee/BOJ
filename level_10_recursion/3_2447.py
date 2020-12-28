N = int(input())

# starList = []
# for j in range(N):
#     starList.append([])
#     for i in range(N):
#         starList[-1].append(" ")
starList = [[" " for i in range(N)] for j in range(N)]

for j in range(3):
    for i in range(3):
        starList[i][j] = "*"
starList[1][1] = " "

def star(n):
    if n == 3:
        return

    next_n = int(n/3)
    star(next_n)

    for i_offset in range(0, 3*next_n, next_n):
        for j_offset in range(0, 3*next_n, next_n):
            if (j_offset == 0 and i_offset == 0) or \
                (j_offset == next_n and i_offset == next_n):
                continue
            else:
                for i in range(i_offset, i_offset+next_n):
                    for j in range(j_offset, j_offset+next_n):
                        starList[i][j] = starList[i - i_offset][j - j_offset]

star(N)
for i in range(N):
    print("".join(starList[i]))
    