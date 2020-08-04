
#Gun 클래스 

class Gun:
    def __init__(self,name,bullet):
        self.bullet = bullet
        self.name = name 
    
    def fire(self):
        if self.bullet >= 1:
            self.bullet -= 1 
            print("빵야~ ")
        else:
            print("틱~")
    def reload(self):
        self.bullet = 20 
        print("20발 재장전 되었습니다.")


# g = Gun("AK47",20)

# for i in range(30):
#     g.fire()

# g.reload()
# g.fire()



class Police():
    def __init__(self,name,position,age):
        self.name = name
        self.position = position
        self.age = age
        self.gun = None
    
    def receive_gun(self,gun):                   #특정 method를 통해서 상속 받지 않고 사용가능 (has) 
        self.gun = gun

    def patrol(self):
        print("순찰중")
    
    def arrest(self,who):
        print(who,"을/를 체포합니다.")
    
    def notify_miranda_rights(self):
        print('당신은 묵비권을....') 

    def eat_donut(self):
        print("냠냠...")

    def use_weapon(self):
        if self.gun != None:
            self.gun.fire()
        else:
            print("총이 없습니다.")



p1 = Police("홍길동","교통과",20)

p1.patrol()
p1.arrest("임꺽정")
p1.notify_miranda_rights()
p1.eat_donut()

# for i in range(10):
#     p1.fire()

# p1.reload()
# print(p1.bullet)

g = Gun("m60리볼버",8)

p = Police("포돌이","순경",20)

p.receive_gun(g)

p.use_weapon()