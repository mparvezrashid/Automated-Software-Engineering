import re,math
from collections import Counter, defaultdict
from table import Tbl
from ZeroR import ZeroR
from NB import NB

class Abcd:

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

    def Abcds(self, file, wait, classify):

        linecount = 0

        '''for line in file:            
            linecount+=1
            line = re.sub(r'([\n\t\r]|#.*)', '', line.strip())
            if len(line)>0:
                line = line.split(',')
            if wait<linecount:
                self.Abcd1(line[-1],zr.classify(line))
            zr.train(tbl,linecount,line)   
            #tbl.Tbl1(linecount,line)
        self.AbcdReport()  
        linecount=0'''
        for line in file:
            linecount += 1
            line = re.sub(r'([\n\t\r]|#.*)', '', line.strip())
            if len(line) > 0:
                line = line.split(',')
            if wait < linecount:
                #print(line[0])
                #print(line[-1] + classify.classify(line))
                #print(classify.classify(line)+line[-1])
                self.Abcd1(line[-1], classify.classify(line))
                #self.Abcd1('yes', 'yes')

            classify.train(linecount, line)
        '''print(classify.tbl.cols)
        print(classify.tbl.nums)
        print(classify.tbl.syms)
        print(classify.tbl.goals)
        # tbl.Tbl1(linecount,line)'''
        #print(classify.subtbl)
        self.AbcdReport()

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
