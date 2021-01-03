class w:
    def __init__(self):
        self.arr = [[[0 for c_ in range(21)] for b_ in range(21)] for a_ in range(21)]
        
        for a in range(1, 21):
            for b in range(1, 21):
                for c in range(1, 21):
                    if a < b and b < c:
                        self.arr[a][b][c] = self.val(a, b, c-1) + self.val(a, b-1, c-1) - \
                                            self.val(a, b-1, c)
                    else:
                        self.arr[a][b][c] = self.val(a-1, b, c) + self.val(a-1, b-1, c) + \
                                            self.val(a-1, b, c-1) - self.val(a-1, b-1, c-1)

    def val(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return self.arr[20][20][20]

        return self.arr[a][b][c]

w_ = w()

abc = list(map(int, input().split()))
while abc != [-1, -1, -1]:
    a, b, c = abc
    print("w({}, {}, {}) = {}".format(a, b, c, w_.val(a, b, c)))

    abc = list(map(int, input().split()))
