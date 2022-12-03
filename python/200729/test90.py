import random
import math
class Agar:

    def __init__(self,color,nickname):
        self.radius = 5
        self.color = color
        self.nickname = nickname
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.weight = 10
    
    def feeding(self,other):
        if other.weight < self.weight:
            self.weight += other.weight
        else: 
            self.weight += 17
            print("먹이주기")
    
    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print("셀 먹기")


    def split(self):
        self.weight =self.weight//2
        print("분해")
    
    
    
    def move(self):
        print("이동하기")

    #@xxxxxxxxxx  ==> 데코레이터 
    @staticmethod                 #정적, 인스턴스가 없어도 사용가능
    def getArea(radius):
        return radius * radius * math.pi    



print(Agar.getArea(50))

a1 = Agar("green","망국이다")
a1.move()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.split()
