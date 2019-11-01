import re,math
from collections import Counter, defaultdict
from table import Tbl
from Sym import Sym
from ZeroR import ZeroR
from Abcd import Abcd
from NB import NB



def main():
    print("#--- zerorok -----------------------")
    print("weathernon")
    f = open("weather.csv", "r")
    # ZeroR(f,3)
    abcd = Abcd()
    abcd.Abcds(f, 3, ZeroR(Tbl()))
    f.close()
    print("diabetes")
    f = open("diabetes.csv", "r")
    # ZeroR(f,3)
    abcd = Abcd()
    abcd.Abcds(f, 3, ZeroR(Tbl()))
    f.close()
    print("#--- nbok -----------------------")
    print("weathernon")
    f = open("weather.csv", "r")
    abcd2 = Abcd()
    abcd2.Abcds(f, 4, NB(Tbl()))

    f.close()
    print("diabetes")
    f = open("diabetes.csv", "r")
    abcd2 = Abcd()
    abcd2.Abcds(f, 5, NB(Tbl()))
    f.close()

if __name__ == "__main__":
    main()
