
from animal import Animal


class Whale(Animal):

    def __init__(self,foots):
        print("고래 초기화 함수")
        super().__init__(foots)
        self.species = "흰수염고래"
        self.name = "고래야"
    
    def Dive(self):
        print("물속을 잠수해요")
    

    
if __name__ == "__main__":
    w = Whale(0)
    print(w.eyes)                          #왜 안돼?
    w.Dive()
    w.eating("플랑크톤")
    w.sleeping()