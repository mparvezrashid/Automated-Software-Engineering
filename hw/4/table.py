import re,math
from collections import Counter, defaultdict
from Num import Num
from Sym import Sym

class THE:
    sep = ","
    num = "$"
    less = "<"
    more = ">"
    skip = "?"
    NUMCOL  = r'([<>\\$])'
    #GOALCOL = r'([<>!])'
    GOALCOL = "!"
    LESS    = "<"
    doomed = r'([\n\t\r ]|#.*)'


class Tbl:

    def __init__(self, norows=True):
        self.syms = []
        self.nums = []
        self.xnums = []
        self.xsyms = []
        self.goals = []
        self.xs = []
        self.w = []
        self.cols = []
        self.rows = []
        self.norows = norows
        self.numObject = {}
        self.symObject = {}
        self.realcols = []

    def Tbl1(self, r, lst):

        if (r == 1):
            self.realcols = lst
            for c, v in enumerate(lst):
                if THE.skip not in v:
                    #print(v)
                    self.TblCols(c, v)

        else:
            if self.norows:
                for c, v in enumerate(lst):
                    v = self.dtype(v.strip())
                    if c in self.cols:
                        if c in self.nums:
                            self.numObject[c] + v
                        if c in self.syms:
                            self.symObject[c] + v

                            # print(Sym.SymLike(self.symObject[0],"rainy",1,2))

    def TblAbout(self):
        self.syms = []
        self.xnums = []
        self.xsyms = []
        self.goals = []
        self.xs = []
        self.w = {}

    def TblCols(self, c, v):
        # if v in CLASSCOL: = c
        self.cols.append(c)
        if THE.less in v or THE.more in v or '$' in v:
            self.nums.append(c)
            self.numObject[c] = Num()
        else:
            self.syms.append(c)
            self.symObject[c] = Sym()
        if THE.GOALCOL in v:
            self.goals.append(c)

        else:
            self.xs.append(c)
        if c in self.xs and c in self.nums: self.xnums.append(c)
        if c in self.xs and c in self.syms: self.xsyms.append(c)
        if "/>/" in v: self.w[v] = 1
        if "/</" in v: self.w[v] = -1

    def TblHeader(self, lst, c):
        lst = []
        for c in self.cols:
            lst[c] = self.cols[c]

    def dtype(self, z):
        try:
            int(z); return int(z)
        except:
            try:
                float(z); return float(z)
            except ValueError:
                return z


class Col:
    def __init__(self, c, v):
        IGNORE = "?"
        self.n = 0
        self.col = c
        self.txt = v

    def Col1(self, v, add):
        if v in IGNORE:
            return v
        add = self.add
        return add(self, v)
