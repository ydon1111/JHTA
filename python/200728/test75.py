class Human:
    def __init__(self,a,b,c):
        print('초기화 함수 호출')
        self.name = a
        self.age = b
        self.job = c
        self.eye = 2
        self.mouth = 1
        self.ears = 2  
    def eating(self):
        print("냠냠 맛있게 먹어요")
    def walking(self):
        print("두발로 걸어어요 아장아장")
    def sleeping(self):
        print("쿨쿨자요")
    def thinking(self):
        print("생각한다 고로존재한다.")
    def status(self):
        print("이름 :",self.name)
        print("나이 :",self.age)
        print("직업 :",self.job)
        print("눈 :",self.eye)
        print("입 :",self.mouth)
        print("귀 :",self.ears)

p = Human("펭수",20,"직장인")
p.status()

print('-----------------------')

d = Human("둘리",1000000000,"백수")
d.status()