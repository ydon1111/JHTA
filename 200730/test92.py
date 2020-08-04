class Car:
    def __init__(self,handle=1,wheel=4,eye=2,nose=1,mouse=1):
        self.handle = handle
        self.wheel = wheel
        self.eye = eye
        self.nose = nose
        self.mouse = mouse
        print("초기화 함수 호출..")

    def __add__(self,otherCar):
        print("충돌났어요")

    def __sub__(self,otherCar):
        print("지붕만 남았어요")

    def run(self):
        print(self.wheel,"달려")

    def stop(self):
        print("정지")

    def smell(self,what):
        print(what,"냄새 맡는중")

    def talk(self):
        print("대화중")

c1 = Car()

c1.talk()
c1.run()
print(c1.handle)


class InheritedCar(Car):    
    def lightOn(self):
        print("라이트를 켜요")

    def run(self):                   #override
        print("오픈카로 달려")

ic1 = InheritedCar()

c1.smell("꽃")
c1.run()
ic1.smell("장미")
ic1.lightOn()
ic1.run()


c1+ic1 #일반적으로는 + 안됨, __add__연산자를 통해서 + 가능하게함 
c1-ic1 

