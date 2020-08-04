# has - a 관계

# Aggregation Relationship : 경찰 < ===> 총 
# 느슨한 관계 

#Composition Relationship : 자동차 < ==> 엔진
# 둘 사이가 밀접 

class Engine:
    def __init__(self):
        print("GDI(Gasoline Direct Injection ) 엔진")
    
    def start(self):
        print("엔진 동작하는중")


class Car:
    def __init__(self):
        print("붕붕카..")
        self.engine = Engine()
        print("엔진 장착")

    def run(self):
        self.engine.start()


c = Car()
c.run()

