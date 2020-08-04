
from test88 import Parent


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("초기화 함수")
        self.name = "홍길동" 
        self.age = 21
        self.height = 181
        self.gender = "남성"
        self.score = 100
    
    def singing(self):
        print("다른노래 부르기 ")



    def club(self):
        print("클럽가기")

if __name__ == "__main__":
    c = Child()
    print(c.score)
    print(c.name)
    print(c.age)
    print(c.country)
    c.eating()
    c.cooking()
    c.singing()           # 상속 받은 값을 변경하기 ,method overriding
    c.club()

    