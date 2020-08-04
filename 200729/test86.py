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

    def sleepin(self):
        print("쿨쿨자요")