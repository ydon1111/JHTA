
class Person:
    '''
    인간 클래스
    '''
    def __init__(self):
        print(id(self))
        print('Person 초기화 함수')
        self.name='홍길동'
        self.age =20 
        self.job ="도적"
    
    def eating(self,what):
        print(self.name,"이",what, "을/를 맛있게 먹어요")

    def sleeping(self):
        print("쿨쿨자요")




#상속          (가져올 클래스)   Person 을 상속받은 Superman
class Superman(Person):
    def __init__(self,name,age,job,hobby):
        print("SuperMan 초기화함수")
        self.name=name
        self.age =age 
        self.job =job
        self.hobby=hobby
    
    def fly(self):
        print("비행 : 날아보아요~~")
    
    def laser(self):
        print("지이잉")




sm = Superman("슈퍼맨",20,"신문기자","연애")

sm.fly()
sm.laser()
sm.eating("바나나")
sm.sleeping()
