from table import Tbl

class ZeroR():
    def __init__(self, tbl):
        self.tbl = tbl

    def classify(self, line):
        return self.tbl.symObject[self.tbl.goals[0]].mode

    def train(self, linecount, line):
        self.tbl.Tbl1(linecount, line)
