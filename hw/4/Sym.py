from collections import Counter, defaultdict
class Sym:

    def __init__(self):
        self.mode = ""
        self.most, self.c = 0, 0
        self.cnt = defaultdict(int)

    def __add__(self, x):
        self.c += 1
        self.cnt[x] += 1
        tmp = self.cnt[x]
        if tmp > self.most:
            self.most = tmp
            self.mode = x

    def SymLike(self, x, prior, m):
        f = self.cnt[x]
        # print(f)
        return (f + m * prior) / (self.c + m)
