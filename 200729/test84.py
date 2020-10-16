class Animal:
    def __init__(self):
        print("Animal 초기화 함수")
        self.eye = 2
        self.mouth = 1
        self.ears = 2 
        
    def eating(self,eat):
        print(eat,"을 먹어요")

    def sleeping(self):
        print("쿨쿨 자요")
    



class Monkey(Animal):

    def __init__(self):
        print("원숭이 초기화 함수")
        super().__init__()
        self.species = "긴팔원숭이"
        self.name = "원원이"
    
    def TreeClimbing(self):
        print("나무를 타요")

    def sleeping(self):
        print("쿨쿨 자요")
    

if __name__ == "__main__":
    m = Monkey()
    print(m.eye)
    m.TreeClimbing()
    m.eating("바나나")
    m.sleeping()