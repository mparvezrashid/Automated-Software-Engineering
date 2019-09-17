import re, sys
from Num import Num
from collections import Counter, defaultdict

class THE:
    sep = ","
    num = "$"
    less = "<"
    more = ">"
    skip = "?"
    NUMCOL  = r'([<>\\$])'
    GOALCOL = r'([<>!])'
    LESS    = "<"
    doomed = r'([\n\t\r ]|#.*)'


class Mine:
    oid = 0

    def identify(self):
        Mine.oid += 1
        self.oid = Mine.oid
        return self.oid

    def __repr__(i):
        pairs = sorted([(k, v) for k, v in i.__dict__.items()
                        if k[0] != "_"])
        pre = i.__class__.__name__ + '{'
        q = lambda z: "'%s'" % z if isinstance(z, str) else str(z)
        return pre + ", ".join(['%s=%s' % (k, q(v))
                                for k, v in pairs]) + '}'


class Tbl(Mine):
    listOfRead = []  # processed output from read
    listOfRow = []  # list of row objects
    listOfCol = []  # list of col object
    listOfMy = []
    NUMCOL=[]
    table=[]
    GOALCOL=[]
    NUMCOLVAL=[]
    Cell=[]
    
    def __init__(self):
        self.identify()  # oid implementation need improvement

    def read(self, file):
        for n, cell in enumerate(cells(cols(rows(string(file))))):
            #print(Tbl.table)
            Tbl.Cell.append(cell)
            '''if n == 0:  # check init title list is empty
                self.listOfCol = [Col(i, t) for i, t in enumerate(cell)]
            else:
                
                self.listOfRow += [Row(cell, [], 0)]  # each row is a Row object'''
        for n, cell in enumerate(Tbl.Cell):
        #print(Tbl.Cell)
            if n == 0:  # check init title list is empty
                self.listOfCol = [Col(i, t) for i, t in enumerate(cell)]
                self.listOfMy = [My(i, t) for i, t in enumerate(cell)]
                        
    
    def dump(self):
        [print(c) for c in self.listOfCol]
        [print(m) for m in self.listOfMy]
        
class My(Mine):
    
    def __init__(self, pos=0, txt=None):
        goal=[]
        self.identify()
        print(self.__class__.__name__)
        for a,b,c in Tbl.table:
            
            if a[1]=='goals':
                goal.append(b[1])
        self.goals=goal    
        


class Col(Mine):
    
    def __init__(self, pos=0, txt=None):
        #self.identify()
        #self.pos = pos
        #print(self.__class__.__name__)
        self.txt = txt
        #print(Tbl.table)
        for a,b,c in Tbl.table:
            #print(b)
            print("| "+str(b[1]+1)+"\n")
            if b[0] == txt:
               #print(a)
               if a[0]=='Num1':
                  #print(c)
                  numAddInstance = Num()
                  exp=0
                  
                  for colval in c:
                      #print(colval)
                      numAddInstance + colval
                      
                  print("| | |"+"Num1")        
                  self.mu=(round(numAddInstance.expect(), 2))
                  self.hi= numAddInstance.hi
                  self.lo= numAddInstance.lo
                  self.m2= round(numAddInstance.m2,2)
                  self.sd= round(numAddInstance.sd(),2)
                  self.n=len(c)
                  self.col=b[1]+1
               else:
                   #print(c)
                   sym1 = Sym1()
                   self.add="Sum1"
                   self.mode = sym1.mode(c)
                   self.most = c.count(self.mode)
                   self.n=len(c)
                   self.col=b[1]+1
                   self.cnt=sym1.count(c)
                       


class Sym1:
    cnt=0
    def mode(self,col=[]):
        #col = ['rainy', 'sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy']
        count = 0
        #for n, cell in enumerate(col):
        count = col.count(max(col,key=col.count))
        print(count)
        return (max(col,key=col.count))
    def count(self,col=[]):
        print(Counter(col))
        return Counter(col)    
              
          



class Row(Mine):
    def __init__(self, cells=[], cooked=[], dom=0):
        self.identify()
        self.cells = cells
        self.cooked = cooked
        self.dom = dom


def string(s):
    """read lines from a string"""
    for line in s.splitlines():
        yield line


def rows(src):
    """convert lines into lists, killing whitespace
    and comments. skip over lines of the wrong size"""
    linesize = None
    for n, line in enumerate(src):
        line = re.sub(THE.doomed, '', line.strip())
        if line:
            line = line.split(THE.sep)  # breakup a string and add the data to a string array
            if linesize is None:
                linesize = len(line)
            if len(line) == linesize:
                yield line
            else:
                print("E> skipping line %s" % n, file=sys.stderr)  # To print to STDERR


def cols(src):
    """skip columns whose name contains '?'"""
    usedCol = []
    for cells in src:
        # usedCol = usedCol or [n for n, cell in enumerate(cells) if not THE.skip in cell]
        if len(usedCol)==0:
            #usedCol = [n for n, cell in enumerate(cells) if not THE.skip in cell]
            for n, cell in enumerate(cells):
                if not THE.skip in cell:
                    usedCol.append(n)
                    if re.search(THE.NUMCOL,cell):
                        Tbl.NUMCOL.append(n)
                        if '<' in cell:
                            Tbl.table.append([["Num1","goals"],[cell,n,-1],[]])
                        else:
                            Tbl.table.append([["Num1","goals"],[cell,n,1],[]])
                        
                    else:
                        #re.search(THE.GOALCOL,cell):
                        #Tbl.GOALCOL.append(n)
                        if '!' in cell:
                            Tbl.table.append([["Sym1","goals"],[cell,n,1],[]])
                        else:
                            Tbl.table.append([["Sym1","xs"],[cell,n,1],[]])
                #print(Tbl.table)
        #print("Hello")        
        #print(cells[n] for n in usedCol)                  
        yield [cells[n] for n in usedCol]


def cells(src):
    """convert strings into their right types"""
    one = next(src)
    #print("Hello")
    #print(one)
    fs = [None] * len(one)  # [None, None, None, None]
    yield one  # the first line

    def ready(n, cell):
        #print(type(cell))
        #print(cell)
        if cell == THE.skip:
            return cell  # skip over '?'
        #elif C
        fs[n] = fs[n] or prep(one[n])  # ensure column 'n' compiles
        #fs[n] = fs[n] or prep(cell)
        #print("baal")
        #print(fs[n](cell))
        val = prep(cell)
        #print(Tbl.table[n])
        if Tbl.table[n][0][0]=='Num1':
            Tbl.table[n][2].append(val)
            Tbl.NUMCOLVAL.append(val)
        elif Tbl.table[n][0][0]=='Sym1':  
            Tbl.table[n][2].append(val)  
                  
        return val
        #return fs[n](cell) # compile column 'n'
        

    for _, cells in enumerate(src):
        #print("cells:", cells)
        #print("???????????????????????")
        #print([ready(n, cell) for n, cell in enumerate(cells)])
        yield [ready(n, cell) for n, cell in enumerate(cells)]


def prep(x):
    """return something that can compile strings"""
    #print(x)
    def num(z):
        #print(z)
        """if type(z)!= <type 'str'>
            f = float(z)
            i = int(f)
            return i if i == f else f"""
        try: int(z); return  int(z) 
        except:
            try: float(z); return  float(z)
            except ValueError: return z    
        #else return z    
    
    # --------------------------------------------------------
    for c in [THE.num, THE.less, THE.more]:
        if c in x:
            return num
    return num(x) 

class ABCD:
    def __init__(self):

        self.db="Data"
        self.num = 0
        self.rx="rx"
        self.a=defaultdict(lambda: 0)
        self.b=defaultdict(lambda: 0)
        self.c=defaultdict(lambda: 0)
        self.d=defaultdict(lambda: 0)
        self.known=defaultdict(lambda: 0)
        self.yes=0
        self.no=0
      

    def Abcd1(self,want, got, x=0):
        self.num += 1
        if self.known[want] == 0:
            self.known[want] +=1
            self.a[want]= self.yes + self.no
            print(want,self.a[want])
        '''if self.known[want] == 1:
            self.a[want]= self.yes + self.no
            print(want,self.a[want]) '''
        if self.known[got] == 0:
            self.known[got] +=1
            self.a[got]= self.yes + self.no
            print(got, self.a[got])
        '''if self.known[got] == 1:
            self.a[got]= self.yes + self.no
            print(got, self.a[got])'''     
        
        if want == got : self.yes+=1
        else : self.no+=1
        print(self.known)
        for x in self.known:
            #print(x)
            if want == x: 
                if want == got:
                    self.d[x]+=1 
                else: self.b[x]+=1
            else: 
                if got == x : self.c[x]+=1 
                else: 
                    self.a[x]+=1
                    print(x,self.a[x])
      
#def AbcdReport(self,x,p,q,r,s,ds,pd,pf pn,prec,g,f,acc,a,b,c,d) {
    def AbcdReport(self) :
        p = " %4.2f"
        q = " %4s"
        r = " %5s"
        s = " |"
        ds= "----"
        '''print(r s r s r s r s r s r s r s q s q s q s q s q s q s " class\n",
              "db","rx","num","a","b","c","d","acc","pre","pd","pf","f","g")
        print(r  s r s r s r s r s r s r s q s q s q s q s q s q s "-----\n",
              ds,ds,"----",ds,ds,ds,ds,ds,ds,ds,ds,ds,ds)'''
        print("    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class\n") 
        print("  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- | -----\n")  
        for x in self.known:
            pd = pf = pn = prec = g = f = acc = 0
            a = self.a[x]
            b = self.b[x]
            c = self.c[x]
            d = self.d[x]
            if b+d > 0 : pd   = round(d     / (b+d),2) 
            if a+c > 0 : pf   = round(c     / (a+c),2) 
            if a+c > 0 : pn   = round((b+d) / (a+c),2) 
            if c+d > 0 : prec = round(d     / (c+d),2) 
            if 1-pf+pd > 0 : g=round(2*(1-pf) * pd / (1-pf+pd),2) 
            if prec+pd > 0 : f=round(2*prec*pd / (prec + pd),2)   
            if self.yes + self.no > 0 :
                #print(self.yes, self.yes + self.no)
                acc  = round(self.yes / (self.yes + self.no),2)
                #print(acc)
            print("{:7s}|".format(self.db) + "{:7s}|".format(self.rx) + "{:7d}|".format(self.num) + "{:7d}|".format(a) + "{:7d}|".format(b) + "{:7d}|".format(c) + "{:7d}|".format(d) + "{:7f}|".format(acc) + "{:7f}|".format(prec) + "{:7f}|".format(pd) + "{:7f}|".format(pf) + "{:7f}|".format(f) + "{:7f}|".format(g) + "{:7s}".format(x) + '\n')
        

def Abcd():
    #print("Abcd")
    abcd = ABCD()
    for j in range(6): abcd.Abcd1("yes", "yes")
    for j in range(2): abcd.Abcd1("no", "no")
    for j in range(5): abcd.Abcd1("maybe", "maybe")
    
    abcd.Abcd1("maybe","no")
    abcd.AbcdReport()

def main():
    file="""
  outlook, ?$temp,  <humid, wind, !play
rainy, 68, 80, FALSE, yes # comments
sunny, 85, 85,  FALSE, no
sunny, 80, 90, TRUE, no
overcast, 83, 86, FALSE, yes
rainy, 70, 96, FALSE, yes
rainy, 65, 70, TRUE, no
overcast, 64, 65, TRUE, yes
sunny, 72, 95, FALSE, no
sunny, 69, 70, FALSE, yes
rainy, 75, 80, FALSE, yes
sunny, 75, 70, TRUE, yes
overcast, 72, 90, TRUE, yes
overcast, 81, 75, FALSE, yes
rainy, 71, 91, TRUE, no
  """

    tbl = Tbl()
    tbl.read(file)
    
    tbl.dump()
    #print(tbl.table)
    Abcd()


   
    
  
    
    #print(round(numAddInstance.expect(), 2))
    #print(round(numAddInstance.delta(), 2))

   

if __name__ == "__main__":
    main()
