class Marine:
    def __init__(self):
        self.hp = 100
        self.attackPoint = 4
        print('객체 초기화')
    def attack(self,other):
        if other.hp > 4:
            other.hp -= self.attackPoint
        else:
            print("고마해라..많이 묵었다")
        print("체력이 %d 상태입니다"%other.hp)
    def useSteamPack(self):
        if self.hp >= 6:
            print("힘이 쏫아요!!")
            self.hp -= 5
            print("체력이 %d 상태입니다"%self.hp)
        else:
            print("체력이 부족합니다.")

    def move(self):
        print("gogo")

class Medic:
    def __init__(self):
        self.hp = 150
        self.x = 100
        self.y = 100
        self.mp = 50
        self.healPower = 7
        self.defense = 3 
    def heal(self,target):
        target.hp += self.healPower
        print('hp :',target.hp,'입니다')
    
    def move(self):
        print("gogogo")
    def hold(self):
        print("stop")

m1 = Marine()
m2 = Marine()
me = Medic()


for i in range(5):
    m1.useSteamPack()

me.heal(m1)



