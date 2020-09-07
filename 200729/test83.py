from animal import Animal

#부모클래스 , base class , superclass, parent

#자식 클래스 , derived class , child

class Rabbit(Animal):

    def __init__(self,foots):
        super().__init__(foots)
        print("토끼 초기화 함수")
        self.species = "앙골라"
        self.name = "토순이"
    
    def jump(self):
        print("깡총깡총 뛰어요")
    
    def sleeping(self):
        print("쿨쿨 자요")
    
if __name__ == "__main__":
    r = Rabbit(4)
    print(r.eyes)
    r.jump()
    r.eating("당근")
    r.sleeping()
    print(r.foots)