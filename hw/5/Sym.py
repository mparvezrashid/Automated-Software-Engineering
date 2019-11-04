import math
from collections import Counter, defaultdict
class Sym:

    def __init__(i, inits=[]):

        i.n=0

        i.rank, i.like = 1, 1
        i.mode = None
        i.most = 0
        i.cnt = {}
        [i + x for x in inits]

    def add(i, x):
        new = i.cnt.get(x, 0) + 1
        i.cnt[x] = new
        if new > i.most:
            i.mode, i.most = x, new

    def sub(i, x):
        old = i.cnt.get(x, 0)
        if old > 0:
            i.cnt[x] = old - 1

    def xpect(i, j):
        n = i.n + j.n
        return i.n / n * i.variety() + j.n / n * j.variety()

    def __add__(i, x):
        y = x
        if y != '?':
            i.n += 1
            i.add(y)
        return x

    def __sub__(i, x):
        y = x
        if y != '?':
            i.n -= 1
            i.sub(y)
        return x

    def variety(i):
        return i.ent()

    def ent(i):
        e = 0
        for v in i.cnt.values():
            if v > 0:
                p = v / i.n
                e += -1 * p * math.log(p, 2)
        return e


