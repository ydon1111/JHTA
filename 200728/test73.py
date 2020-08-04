class Person:
    '''
    인간 클래스
    '''
    def __init__(self):
        print(id(self))
        print('초기화 함수')
        self.name='홍길동'
        self.age =20 
        self.job ="도적"
    
    def eating(self,what):
        print(self.name,"이",what, "을/를 맛있게 먹어요")

p1 = Person()
print("id p1" , id(p1))



print(p1.name)
print(p1.age)
print(p1.job)

p1.eating("사과")
print('------------------------------------------')

p2 = Person()
print(p2.name)
print('------------------------------------------')
print('id(p1) :' , id(p1), 'id(p2) :', id(p2))