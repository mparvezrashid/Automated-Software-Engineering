from Num import Num
from Sym import Sym

class Symdiv:
    def __init__(i,first,last,type):
        i.xis=type
        i.lst=sorted(last)
        i.fst=first
        #print(i.lst)
        i.lst_stat=type(first)
        i.gain = 0
        i.step = int(len(i.lst) ** .5)
        i.stop = i.lst[-1]
        #print(i.stop)
        i.start = i.lst[0]
        i.ranges=[]
        i.position=0
        i.cut=0
        i.E=i.lst_stat.variety()*0.3
        #print(i.E)


        i.divide(1, len(i.lst), i.lst_stat, 1)
        i.gain /= len(i.lst)
        print("\n")
        for c,val in enumerate(i.ranges):

            nm=Num(i.fst[i.position:val.n+i.position])
            i.position=val.n+i.position+1
            print(str(c+1)+" x.n "+str(val.n)+" | "+"x.lo "+str(round(nm.lo,5))+" x.hi "+str(round(nm.hi,5))+" | "+"y.mode "+val.mode+" y.ent "+str(val.ent()))
            #print(val)


    def divide(i, start, end, type, rank):
        l = i.xis()
        r = i.xis(i.lst[start:end])
        #print(start, end)
        best = type.variety()
        # i.epsilon = b4.sd() * THE.div.cohen
        cut = None
        for j in range(start, end):
            l + i.lst[j]
            r - i.lst[j]
            if l.n >= i.step:
                if r.n >= i.step:
                    now = i.lst[j - 1]
                    after = i.lst[j]
                    if now == after: continue
                    if r.mode != l.mode:
                        if after != i.start and i.stop != now:
                            xpect = l.xpect(r)
                            if xpect * 1.025 < best:
                                best, cut = xpect, j

        if cut:
            #print(cut)

            ls, rs = i.lst[start:cut], i.lst[cut:end]

            rank = i.divide(start, cut, i.xis(ls), rank) + 1
            rank = i.divide(cut, end, i.xis(rs), rank)
        else:
            i.gain += type.n * type.variety()
            type.rank = rank

            i.ranges +=[type]

        #print(type)
        return rank
