
class Parent:
    def __init__(self):
        print("초기화 함수")
        self.name = '홍판사'
        self.age = 50
        self.height = 180
        self.gender = '남자'
        self.country = '한국'
    
    def eating(self):
        print("먹기")
    def sleeping(self):
        print("자기")
    def singing(self):
        print("노래하기")
    def cooking(self):
        print("요리하기")


if __name__ == '__main__':
    p = Parent()
    print(p.name)
    print(p.age)
    print(p.height)
    print(p.gender)
    print(p.country)

    p.eating()
    p.sleeping()
    p.singing()
    p.cooking()  

    p.eating()