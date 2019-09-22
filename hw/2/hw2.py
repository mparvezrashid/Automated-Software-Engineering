import re, sys, six
from Num import Num
class Col:
    
    def __init__(self,Num, cols,OID):
        
        
        print("| | add: "+str(cols[0]+1))
        print("| | col: "+str(cols[1])+"\n")
        print("| | hi:"+str(Num.hi)+"\n")
        print("| | lo:"+str(Num.lo)+"\n")
        print("| | m2:"+str(round(Num.m2,2))+"\n")
        print("| | mu:"+str(round(Num.mu,2))+"\n")
        print("| | n:"+str(14)+"\n")
        print("| | OID:"+str(OID)+"\n")
        print("| | sd:"+str(round(Num.sd(),2))+"\n")
class Row:
    def __init__(self, row, OID):
        c=1
        print("t.rows")
        for n,val in enumerate(row,OID):
            print("| "+str(c))
            c+=1
            for x,r in enumerate(val):
                print("| | | "+str(x+1)+": "+str(r))
            OID+=1    
            print("| | cooked")
            print("| | dom= 0")
            print("| | oid="+str(OID))
            OID+=1
            
                  
        

class CrtTbl:
    def __init__(self):
        self.cols=[]
        self.rows=[]
        self.OID=1
        
    def read(self, s):
       for line in s.splitlines():
           print(line)
           yield line

    def read_line(self,s):
        lnsz=None
        cols=[]
        rows=[]
        numcol=0
        flg=0
        Num1=[]
        
        linesize = None
        for line in s.splitlines():
            
            line = re.sub(r'([\n\t\r]|#.*)', '', line.strip())
            if len(line)>0:
                
                line = line.split(',')
                if linesize is None:
                    linesize = len(line)
                if len(line) == linesize:
                    print(line)
                else:
                    print("E> skipping line %s" % n, file=sys.stderr) 
                #print(len(line))
                #print("t.Col")
                if flg==0:
                    flg=1
                  
                    for n,col in enumerate(line):
                      
                        if '?' not in col:
                            cols.append([n,col])
                            if '$' in col:
                              #print(n)
                              Num1.append(Num())
                              
                elif flg==1:
                    
                    
                    #rows = [Num[n] + self.dtype(col) for n,(col,val) in enumerate(zip(cols, line))]
                    #self.rows += [row]
                    #row = [Num[n] + self.dtype(col) for n,(col,val) in enumerate(zip(cols, line))]
                    self.rows.append([self.dtype(col)for n,col in enumerate(line)])
                    #print(self.rows)
                    #self.rows += row
                    
                    for n,col in enumerate(line):
                        val=self.dtype(col)
                        #print(val)
                        if not isinstance(val, six.string_types):
                            Num1[n] + self.dtype(col)
                        

                        #print(n)
                        #print(round(Num1[n].sd(),2))
        for z,n in enumerate(cols):
            self.OID+=1
            if self.OID==2:
                print("t.Col")
            print("| "+str(z+1))
            self.OID+=1
            c=Col(Num1[z],n,self.OID)
            
        r= Row(self.rows,self.OID)    
                            
                                           
    def dtype(self,z):
        try: int(z); return  int(z) 
        except:
            try: float(z); return  float(z)
            except ValueError: return z                    

                


def main():
    file="""
$cloudCover, $temp, $humid, $wind,  $playHours
  100,         68,    80,     0,      3   
  0,           85,    85,     0,      0
  0,           80,    90,     10,     0
  60,          83,    86,     0,      4
  100,         70,    96,     0,      3
  100,         65,    70,     20,     0
  70,          64,    65,     15,     5
  0,           72,    95,     0,      0
  0,           69,    70,     0,      4
  80,          75,    80,     0,      3
  '?',           75,    70,     18,     4
            72,    83,     15,     5
  40,          81,    75,     0,      2
  100,         71,    91,     15,     0
  """

    tbl = CrtTbl()
    tbl.read_line(file)
    


   
    
  
    
    #print(round(numAddInstance.expect(), 2))
    #print(round(numAddInstance.delta(), 2))

   

if __name__ == "__main__":
    main()        
   
