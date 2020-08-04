'''
car 클래스
제조사
차명
색상
연식
바퀴 
핸들 
전진()
후진()
깜빡이()
가속()
감속()
정지()
'''

'''
OOP : Object Oriented Programming : 자원의 재활용
클래스를 사용해 객체(instance)생성 
클래스는 새로운 이름 공간을 지원하는 단위

forward(), backward()
isinstance(변수,클래스명)
''' 


class Car:
    def __init__(self,brand,name,color,year):
        print('초기화 함수 호출')
        self.brand = brand       #인스턴스 변수
        self.name = name
        self.color = color
        self.year = year
        self.tire = 4
        self.handle = 1  
    def forward(self):             #인스턴스 함수(메서드)
        print("앞으로 가")
    def backward(self):
        print("뒤로 가")
    def light(self):
        print("방향지시등 켜")
    def accelerating(self):
        print("달려")
    def slowing(self):
        print("속도줄여")
    def breaking(self):
        print("멈춰")
    def status(self):
        print("제조사 :", self.brand)
        print("이름 :" ,self.name)
        print("색깔 :" ,self.color)
        print("연식 :" ,self.year)
        print("타이어 :" ,self.tire)
        print("핸들 :" ,self.handle)


c=Car("volvo","volvo c 90","white",2020)
c.status()

c.forward()
c.backward()
c.light()
c.accelerating()
c.slowing()
c.breaking()

ns = Car("닛산","멕시마","silver",2019)
ns.status()

#파이썬 메서드의 첫번째 파라미터명은 관례적으로 self 이름 사용
#호출시 호출한 객체 자신이 전달되기 떄문 self 이름 사용
ns.forward()
Car.forward(c)
c.backward()

print(isinstance(c,Car))





