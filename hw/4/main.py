import re, sys, math
from collections import Counter, defaultdict
from statistics import mode


# from Num import Num

class ZeroR():

    def __init__(self, rows):
        self.got = ''
        self.want = ''
        self.true = []
        self.rows = rows
        abcd = ABCD()
        count = 0
        for val in self.rows:
            count += 1
            # md=self.findmode(val[(len(val)-1)])
            # print(val[(len(val)-1)])
            if count <= 2:
                self.true.append(val[(len(val) - 1)])

            if count > 2:
                self.got = max(self.true, key=self.true.count)
                self.want = val[(len(val) - 1)]
                self.true.append(val[(len(val) - 1)])
                # print(self.got)
                abcd.Abcd1(self.want, self.got)

        abcd.AbcdReport()

        # def findmode(self, m):

    # print(m)
    # print(self.predict.append(m))

    def classify(self):
        for val in self.rows:
            findmode(val[(len(val) - 1)])


class NB:

    def __init__(self, tbl):
        self.tbl = tbl
        self.rows = tbl.rows
        self.prior = {}
        self.num = {}
        self.deno = 0
        self.like = {}
        self.want = ""
        self.got = ""

    def classify(self):
        abcd = ABCD()
        nm = {}
        for n, row in enumerate(self.rows):
            self.deno += 1
            self.want = row[len(row) - 1]
            if row[len(row) - 1] not in self.prior:

                self.num[row[len(row) - 1]] = 1
                self.prior[row[len(row) - 1]] = self.num[row[len(row) - 1]] / (self.deno)
            else:
                self.num[row[len(row) - 1]] += 1
                self.prior[row[len(row) - 1]] = self.num[row[len(row) - 1]] / (self.deno)
            # I have prior upto n justt add them now

            self.like[row[len(row) - 1]] = math.log(self.prior[row[len(row) - 1]])
            # print(self.num)
            if n >= 3:
                # print(n)
                for i, val in enumerate(row):
                    if i in self.tbl.cols:
                        if i in self.tbl.sym:
                            # print(val)
                            tmp = Sym(self.tbl, n, val, self.num, self.deno, i).symlike()
                            for key in tmp:
                                self.like[key] = self.like[key] + math.log((tmp[key] + (self.prior[key] * 2) / (n + 2)))
                        elif i in self.tbl.num:
                            for key in self.num:
                                nm[key] = Num()
                                for k, v in enumerate(self.tbl.rows):
                                    if k < n:
                                        if v[len(v) - 1] == key:
                                            nm[key] + v[i]
                                            # print(self.rows[n][i])
                                if nm[key].NumLike(self.rows[n][i]) != 0.0:
                                    self.like[key] = self.like[key] + math.log(nm[key].NumLike(self.rows[n][i]))

                self.got = max(self.like, key=lambda k: self.like[k])
                abcd.Abcd1(self.want, self.got)
        abcd.AbcdReport()


class Sym:
    def __init__(self, tbl, n, val, num, deno, col):
        self.tbl = tbl
        self.val = val
        self.cnt = {}
        self.n = n
        self.m = 2
        self.num = num
        self.deno = deno
        self.i = col

    def symlike(self):
        for key in self.num:
            cn = 0
            for c, data in enumerate(self.tbl.rows):
                if c < self.n:

                    for v in data:
                        if self.val == v and data[len(data) - 1] == key:
                            cn += 1
                            self.cnt[key] = cn
        return self.cnt


class ABCD:
    def __init__(self):

        self.db = "Data"
        self.num = 0
        self.rx = "rx"
        self.a = defaultdict(lambda: 0)
        self.b = defaultdict(lambda: 0)
        self.c = defaultdict(lambda: 0)
        self.d = defaultdict(lambda: 0)
        self.known = defaultdict(lambda: 0)
        self.yes = 0
        self.no = 0

    def Abcd1(self, want, got, x=0):
        self.num += 1
        if self.known[want] == 0:
            self.known[want] += 1
            self.a[want] = self.yes + self.no
            # print(want,self.a[want])
        '''if self.known[want] == 1:
            self.a[want]= self.yes + self.no
            print(want,self.a[want]) '''
        if self.known[got] == 0:
            self.known[got] += 1
            self.a[got] = self.yes + self.no
            # print(got, self.a[got])
        '''if self.known[got] == 1:
            self.a[got]= self.yes + self.no
            print(got, self.a[got])'''

        if want == got:
            self.yes += 1
        else:
            self.no += 1
        # print(self.known)
        for x in self.known:
            # print(x)
            if want == x:
                if want == got:
                    self.d[x] += 1
                else:
                    self.b[x] += 1
            else:
                if got == x:
                    self.c[x] += 1
                else:
                    self.a[x] += 1
                    # print(x,self.a[x])

    # def AbcdReport(self,x,p,q,r,s,ds,pd,pf pn,prec,g,f,acc,a,b,c,d) {
    def AbcdReport(self):
        p = " %4.2f"
        q = " %4s"
        r = " %5s"
        s = " |"
        ds = "----"
        '''print(r s r s r s r s r s r s r s q s q s q s q s q s q s " class\n",
              "db","rx","num","a","b","c","d","acc","pre","pd","pf","f","g")
        print(r  s r s r s r s r s r s r s q s q s q s q s q s q s "-----\n",
              ds,ds,"----",ds,ds,ds,ds,ds,ds,ds,ds,ds,ds)'''
        print(
            "    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class\n")
        print(
            "  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- | -----\n")
        for x in self.known:
            pd = pf = pn = prec = g = f = acc = 0
            a = self.a[x]
            b = self.b[x]
            c = self.c[x]
            d = self.d[x]
            if b + d > 0: pd = round(d / (b + d), 2)
            if a + c > 0: pf = round(c / (a + c), 2)
            if a + c > 0: pn = round((b + d) / (a + c), 2)
            if c + d > 0: prec = round(d / (c + d), 2)
            if 1 - pf + pd > 0: g = round(2 * (1 - pf) * pd / (1 - pf + pd), 2)
            if prec + pd > 0: f = round(2 * prec * pd / (prec + pd), 2)
            if self.yes + self.no > 0:
                # print(self.yes, self.yes + self.no)
                acc = round(self.yes / (self.yes + self.no), 2)
                # print(acc)
            print("{:7s}|".format(self.db) + "{:7s}|".format(self.rx) + "{:7d}|".format(self.num) + "{:7d}|".format(
                a) + "{:7d}|".format(b) + "{:7d}|".format(c) + "{:7d}|".format(d) + "{:7f}|".format(
                acc) + "{:7f}|".format(prec) + "{:7f}|".format(pd) + "{:7f}|".format(pf) + "{:7f}|".format(
                f) + "{:7f}|".format(g) + "{:7s}".format(x) + '\n')


class CrtTbl:
    def __init__(self):
        self.cols = []
        self.rows = []
        self.OID = 1
        self.Num1 = []
        self.sym = []
        self.num = []
        self.goal = []

    def read_line(self, s):
        lnsz = None
        cols = []
        rows = []
        numcol = 0
        flg = 0
        Num1 = []
        dsbl_clm = []

        linesize = None
        for line in s:
            # line=line.splitlines()
            # print(line)

            line = re.sub(r'([\n\t\r]|#.*)', '', line.strip())
            if len(line) > 0:

                line = line.split(',')
                if linesize is None:
                    linesize = len(line)
                # if len(line) == linesize:
                # print(line)
                # else:
                # print("E> skipping line %s" % n, file=sys.stderr)
                # print(len(line))
                # print("t.Col")
                if flg == 0:
                    flg = 1

                    for n, col in enumerate(line):

                        if '?' not in col:
                            self.cols.append(n)
                            # print(n)
                            if '<' in col:

                                Num1.append(Num())
                                self.num.append(n)
                            elif '?' in col:

                                Num1.append(Num())

                                self.num.append(n)
                            elif '!' in col:
                                self.goal.append(n)
                            else:
                                self.sym.append(n)


                elif flg == 1:

                    # rows = [Num[n] + self.dtype(col) for n,(col,val) in enumerate(zip(cols, line))]
                    # self.rows += [row]
                    # row = [Num[n] + self.dtype(col) for n,(col,val) in enumerate(zip(cols, line))]
                    self.rows.append([self.dtype(col.strip()) for n, col in enumerate(line)])
                    # print(self.rows)
                    # self.rows += row

                    # print(n)
                    # print(round(Num1[n].sd(),2))

    def dtype(self, z):
        try:
            int(z); return int(z)
        except:
            try:
                float(z); return float(z)
            except ValueError:
                return z


class Num():
    "Track numbers seen in a column"

    def __init__(self, inits=[]):
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = 10 ** 32, -1 * 10 ** 32
        [self + x for x in inits]

    def delta(self):
        return self.sd()

    def NumLike(self, x):
        var = self.sd() ** 2
        denom = (3.14159 * 2 * var) ** .5
        num = 2.71828 ** (-(x - self.mu) ** 2 / (2 * var + 0.0001))
        return num / (denom + 10 ** -64)

    def expect(self):
        return self.mu

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


def main():
    f = open("weather.csv", "r")

    print("#-----------ZeroR-------------------------------------")
    print("")
    print("weathernon")

    tbl = CrtTbl()
    tbl.read_line(f)
    ZeroR(tbl.rows)

    f = open("diabetes.csv", "r")
    # print(f)
    print("")
    print("diabetes")
    print("")
    tbl2 = CrtTbl()
    tbl2.read_line(f)
    ZeroR(tbl2.rows)
    # print(tbl.goal)
    print("#--------------NB-------------------------------------")
    print("")
    print("weathernon")
    nb = NB(tbl)
    nb.classify()
    print("")
    print("diabetes")
    print("")
    nb2 = NB(tbl2)
    nb2.classify()

    # print(round(numAddInstance.expect(), 2))
    # print(round(numAddInstance.delta(), 2))


if __name__ == "__main__":
    main()

