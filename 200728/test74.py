class Human:
    def __init__(self):
        print('초기화 함수 호출')
        self.name = '고길동'
        self.age = '30'
        self.job = '고위공직자'
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
     

print(Human,id(Human),type(Human))

ko = Human() #인스턴스 변수 = 클래스명() #클래스의 초기화 함수가 호출

#이름을 출력 
print(ko.name)   # 연산자의 의미 : 주소를 찾아가 .. ~~
#나머지 변수값도 출력 
print(ko.age)
print(ko.job)
print(ko.eye)
print(ko.mouth)
print(ko.ears)
ko.thinking()
#함수도 호출
ko.eating()
ko.walking()
ko.sleeping()
ko.status()

#펭수

p = Human()
p.name = "펭수"
p.age = 10
p.job = "ebs 직장인"
p.status()