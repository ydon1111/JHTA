
'''
1.   object , class , instance 란? 

클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고(과자 틀), 
객체(object)란 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)을 뜻한다.
'사과'는 클래스이구요, '내가 엊저녁에 먹은 사과 다섯 개 중에 두 번째 것'이라고 콕 찍어서 말해주면 실체(instance)


''
2.   
m = Man()

print(m.name) # 홍길동
print(m.eye) # 2 
print(m.gender)# 남
print(m.arm) # 2
print(m.age) # 20
print(m.job) # 도적
print(m.character)# 스틸 

m.steal() # 내꼬내꼬 다 내꼬얌!!! 
m.run() # "헛둘 헛둘"
m.runrun() # 땀나게 달려요
m.magic_move() # 동해 번쩍 서해 번쩍
'''


# class Man:
#     def __init__(self):
#         self.name = "홍길동"
#         self.eye = 2
#         self.gender = "남"
#         self.arm = 2
#         self.age = 20
#         self.job = "도적"
#         self.character = "스틸"

#     def steal(self):
#         print("니꼬내꼬 다 내꼬얌!!!")
    
#     def run(self):
#         print("헛둘 헛둘")
#     def runrun(self):
#         print("땀나게 달려요")
#     def magic_move(self):
#         print("동해 번쩍 서해번쩍")
    
# m = Man()

# print(m.name) # 홍길동
# print(m.eye) # 2 
# print(m.gender)# 남
# print(m.arm) # 2
# print(m.age) # 20
# print(m.job) # 도적
# print(m.character)# 스틸 

# m.steal() # 내꼬내꼬 다 내꼬얌!!! 
# m.run() # "헛둘 헛둘"
# m.runrun() # 땀나게 달려요
# m.magic_move() # 동해 번쩍 서해 번쩍

'''
3.	변수명명법?
'''

# 카멜(Camel) 표기법
# 카멜표기법은 낙타등처럼 내려갔다 올라가는 모양? 인데 
# woman+age 처럼 단어 여러개가 붙을때 맨 앞에오는 단어만 소문자로 표기하고, 
# 뒤에오는 단어는 대문자로 표기하는 방법이다. (세단어 이상일경우도 맨앞만 소문자)

# 파스칼(pascal) 표기법
# 파스칼 표기법은 그냥 모든단어가 대문자로 시작한다.
# 함수명이나 클래스명을 파스칼표기법으로 작성하는 경우가 많은데, 보통 카멜과 파스칼표기법을 섞어 적절히 사용하기도한다.

# 스네이크(snake) 표기법
# 언더바(_) 를 붙여 단어를 구분짓는 표기법이다.
# 사실 변수명을 선언할 때는 종종 쓰이기도 하지만 잘 쓰이진 않는것같다.

# 영문자(대, 소문자 구분), 숫자, 언더바(_)를 사용할 수 있다.
# 첫 자리에는 숫자를 사용할 수 없다.
# 파이썬 키워드는 변수 명으로 사용할 수 없다.

# 명명규칙	함수, 변수, Attribute는 소문자로 단어 간은 밑줄(_)을 사용하여 연결한다	예: total_numbers
# 클래스는 단어 첫 문자마다 대문자를 써서 연결하는 CapWords 포맷으로 명명한다	예: CoreClass
# 모듈명은 짧게 소문자로 사용하며 밑줄을 쓸 수 있다. 패키지명 역시 짧게 소문자를 사용하지만 밑줄은 사용하지 않는다.	예: serial_reader
# 모듈 상수는 모두 대문자를 사용하고 단어마다 밑줄로 연결하는 ALL_CAPS 포맷으로 명명한다	예: MAX_COUNT = 100
# 클래스의 public attribute는 밑줄로 시작하지 말아야 한다	예: name
# 클래스의 protected instance attribute는 하나의 밑줄로 시작한다	예: _initialized
# 클래스의 private instance attribute는 2개의 밑줄로 시작한다	예: __private_var
# 인스턴스 메서드는 (객체 자신을 가리키기 위해) self 를 사용한다	예: def copy(self, other):
# 클래스 메서드는 (클래스 자신을 가리키기 위해) cls 를 사용한다	예: def clone(cls, other):


'''
4. 
	ex4.py 
----------------------------------------
	class Triangle 
	width , height
	getArea()
----------------------------------------	
	triangle =	Triangle (100,200) # 너비 100, 높이 200 
	print(triangle.getArea())  # 삼각형의 너비 구하기 
'''






'''
5. 
	ex5.py
----------------------------------------
	class Rectangle
	width , height
	getArea()
----------------------------------------
	r = Rectangle(200,300)
	print(triangle.getArea())  # 사각형의 너비 구하기 
'''


'''
6.
	ex6.py
	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
	작성하세요 
'''


'''
7. 
	Rectangle, Triangle 은 Figure 클래스의 구현클래스로 코드를 변경합니다.

	Rectangle, Triangle 의 getArea() 는 Figure 클래스 의 getArea() 를 
	method overriding 시켜줍니다. 

8. 
	Rectangle, Triangle 의 getArea() 는 Figure 클래스 의 getArea() 를 
	method overriding 시켜줍니다. 
'''

'''
9.
	두점 사이의 거리를 계산하는 pythagoras()를 완성하세요 

	print(util.pytagoras(100,100, 200 ,200))
	
	참고 : math.sqrt(4) ==> 2 
'''
# import math
# class util:
#     @staticmethod
#     def pytagoras(a,b,c,d):
#         return math.sqrt((c - a)*(c - a) + (d -b)*(d -b))    
   
    
# print(util.pytagoras(100,100, 200 ,200))

'''
10.	아래의 명령이 수행될수 있는 Point 클래스를 작성하세요 

	p = Point(100,100) # (x, y) 좌표 
	p.set_x(200)  # x좌표값을 200으로 변경
	p.set_y(300)  # y좌표값을 300으로 변경

	p.get_xy() # (200,300) 형태로 출력 
	
	p.move(500,300) # (200,300) ==> (500,300)
	                     # 메세지를 출력하고 x <= 500 y <=300을 담는다.
	
	참고 ) 모든 메세드는 인스턴스 메서드 모든 속성는 인스턴스 속성
'''

class Point:
    def __init__(self,x,y):
        self._x = x 
        self._y = y

    def set_x(self,x):
        self._x = x
       
    def set_y(self,y):
        self._y = y
    
    def get_xy(self):
        print(self._x,self._y)

    def move(self,x,y):
        print('(',self._x,',',self._y,')','===>','(',x,',',y,')')
        self._x = x
        self._y = y
     




p = Point(100,100) # (x, y) 좌표 
p.set_x(200)  # x좌표값을 200으로 변경
p.set_y(300)  # y좌표값을 300으로 변경
p.get_xy()
p.move(500,300)

