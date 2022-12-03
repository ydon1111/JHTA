
class GuGuDan:
    def __init__(self):
        self.dan = 2
    
    def print(self):
        for r in range(1,10):
            print(self.dan, "*",r,"=",self.dan * r)


g =GuGuDan()

g.dan = 6 

g.print()