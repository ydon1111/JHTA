class player:

    #클래스 속성
    cnt = 0
    bag = []
    
    
    def __init__(self,name):
        print('초기화 함수')
        self.name = name
        player.cnt += 1            #클래스명.속성명 

    def put(self,obj):
        player.bag.append(obj)

    #class method 
    @classmethod
    def getBag(cls):
        print("아이템습득",cls.bag)

    def attack(self,other):
        print(other.name +"를 공격합니다.")
    def greeting(self,other):
        print(other.name+"  야이 바보야")

p1 = player('에코')
print(p1.cnt)
p1.put("권총")
print('--------------------------')

p2 = player('야스오')
print(p2.bag)
print(player.bag)
print('--------------------------')

print(p1.cnt)
print(p2.cnt)
#클래스 속성은 인스턴스끼리 공유

p1.greeting(p2)
p1.attack(p2)

print('--------------------------')

p1.getBag()

p2.getBag()