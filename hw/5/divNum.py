from Num import Num
from Sym import Sym
from divSym import Symdiv

class Numdiv:
    def __init__(i,first,last,type):
        i.xis=type
        i.lst=sorted(last)
        #print(i.lst)
        i.fst = first
        i.lst_stat=type(first)
        i.gain = 0
        i.step = int(len(i.lst) ** .5)
        i.stop = i.lst[-1]
        #print(i.stop)
        i.start = i.lst[0]
        i.ranges=[]
        i.E=i.lst_stat.variety()*0.3
        #print(i.E)
        i.position = 0
        i.cut = 0

        if type==Num:
            i.divide(0, len(i.lst), i.lst_stat, 1)
            i.gain /= len(i.lst)

            for c, val in enumerate(i.ranges):
                nm = Num(i.fst[i.position:val.n + i.position])
                i.position = val.n + i.position + 1
                print(str(c + 1) + " x.n " + str(val.n) + " | " + "x.lo " + str(round(nm.lo, 5)) + " x.hi " + str(
                    round(nm.hi, 5)) + " | " + "y.lo " + str(round(val.lo, 5)) + " y.hi " + str(round(val.hi, 5)))
            # print(val)
        else:
            print("in sym")
            sym=Symdiv(first,last,type)
            sym.divide(0, len(sym.lst), sym.lst_stat, 1)
            sym.gain /= len(sym.lst)

            for c, val in enumerate(i.ranges):
                nm = Num(sym.fst[i.position:val.n + sym.position])
                sym.position = val.n + sym.position + 1
                print(str(c + 1) + " x.n " + str(val.n) + " | " + "x.lo " + str(round(nm.lo, 5)) + " x.hi " + str(
                    round(nm.hi, 5)) + " | " + "y.mode " + val.mode + " y.ent " + str(val.ent()))
                # print(val)



    def divide(i, start, end, type, rank):
        #print("in divide")
        l = i.xis()
        r = i.xis(i.lst[start:end])
        #print(start, end)
        best = type.variety()
        #i.step = int(len(i.lst[start:end]) ** .5)
        # i.epsilon = b4.sd() * THE.div.cohen
        cut = None
        for j in range(start, end):
            #print(j)
            l + i.lst[j]
            r - i.lst[j]
            if l.n >= i.step or r.n >= i.step:
                #print("ln step")
                if l.n >= i.step:
                    #print("Rn step")
                    now = i.lst[j - 1]
                    after = i.lst[j]
                    if now == after: continue

                    #print(str(r.mu)+"-"+str(l.mu)+" = "+str(r.mu - l.mu))
                    if abs(r.mu - l.mu) >= i.E:
                        #print("abs")
                        #print(j)
                        #print(after)
                        #print(i.start)
                        #print(str(after - i.start)+" "+str(i.E))
                        if after - i.start >= i.E:
                            #print("aftr")
                            if i.stop - now >= i.E:
                                #print("stop")
                                xpect = l.xpect(r)
                                if xpect * 1.025 < best:
                                    #print("xpct")
                                    best, cut = xpect, j
                                    # print(j)
        if cut:
            print(cut)
            ls, rs = i.lst[start:cut], i.lst[cut:end]
            print("Ls")
            print(ls)
            print("Rs")
            print(rs)
            rank = i.divide(start, cut, i.xis(ls), rank) + 1
            rank = i.divide(cut, end, i.xis(rs), rank)
        else:
            i.gain += type.n * type.variety()
            type.rank = rank
            i.ranges += [type]
        print(i.ranges)
        return rank
