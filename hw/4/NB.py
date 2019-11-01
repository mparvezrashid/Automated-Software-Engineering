from table import Tbl
from Sym import Sym
from Num import Num
import re,math

class NB:
    def __init__(self, tbl):
        self.tbl = tbl
        self.subtbl = {}
        self.m = 2
        self.n = -1
        self.k = 1

    def classify(self, line):
        # print(self.subtbl)
        #print("Classifying..............")
        most = -10 ** 64
        guess = ''
        for i, j in self.subtbl.items():
            #print("For "+i)
            like = self.bayestheorem(j, line)
            #print(i)
            if like > most:
                most = like
                guess = i
        #print("Guessed: "+guess)
        return guess

    def bayestheorem(self, stbl, line):
        # print(self.tbl.goals)
        #print(line)
        n1 = stbl.symObject[stbl.goals[0]].c  # number of  goals colum's item count
        #print("n1 "+str(n1)+" n Vallu="+str(self.n))
        like = prior = (n1 + self.k) / (self.n-1 + self.k * len(self.subtbl))
        #print("prior ")
        like = math.log(like)
        #print("prior "+str(like))
        for i, j in enumerate(line[:-1]):
            x = self.tbl.dtype(j)
            if i in self.tbl.nums:
                # print(Num.NumLike(stbl.numObject[i], x))
                like += math.log(Num.NumLike(stbl.numObject[i], x))
                #print("x: " + str(x) + "like: " + str(math.log(Num.NumLike(stbl.numObject[i], x))))
            if i in self.tbl.syms:
                like += math.log(Sym.SymLike(stbl.symObject[i], x, prior, self.m))
                # print("x: " + str(x) + "like: " + str(math.log(Sym.SymLike(stbl.symObject[i], x, prior, self.m))))
        #print("like "+str(like))
        return like

    def train(self, linecount, line):
        self.n += 1
        self.tbl.Tbl1(linecount, line)
        if linecount > 1:  # to avoid the table header
            if line[-1].strip() not in self.subtbl:  # creating a  sub table for classes in the goal column
                self.subtbl[line[-1].strip()] = Tbl()
                self.subtbl[line[-1].strip()].Tbl1(1, self.tbl.realcols)  # creating column in sub table
                self.subtbl[line[-1].strip()].Tbl1(linecount, line)
                #print(self.subtbl[line[-1]].realcols)
            else:
                self.subtbl[line[-1].strip()].Tbl1(linecount, line)
