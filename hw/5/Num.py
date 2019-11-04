class Num():
    "Track numbers seen in a column"

    def __init__(self, inits=[]):
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = 10 ** 32, -1 * 10 ** 32
        [self + x for x in inits]

    def delta(self):
        return self.sd()

    def expect(self):
        return self.mu

    def variety(i):
        return i.sd()

    def sd(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1 + 10 ** -32)) ** 0.5

    def __add__(self, x):
        if x < self.lo:
            self.lo = x
        if x > self.hi:
            self.hi = x

        self.n += 1
        d = x - self.mu
        self.mu += d / self.n
        self.m2 += d * (x - self.mu)

    def __sub__(self, x):
        if self.n < 2:
            self.n, self.mu, self.m2 = 0, 0, 0
        else:
            self.n -= 1
            d = x - self.mu
            self.mu -= d / self.n
            self.m2 -= d * (x - self.mu)

    def NumLike(self, x):
        print("SD" + str(self.sd()) + "x" + str(x))
        var = self.sd() ** 2
        denom = (3.14159 * 2 * var) ** .5
        num = 2.71828 ** (-(x - self.mu) ** 2 / (2 * var + 0.0001))
        return num / (denom + 10 ** -64)

    def xpect(i, j):
        n = i.n + j.n
        return i.n / n * i.variety() + j.n / n * j.variety()