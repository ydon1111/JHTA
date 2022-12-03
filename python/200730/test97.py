#서든어택

# Player
#hp
#name


# 수류탄
#데미지 

#칼
#데미지 

#폭탄
#데미지 

#총
#데미지 
class Weaphon:
    def __init__(self):
        pass
    def use(self):
        pass
    def reuse(self):
        pass





class Gun(Weaphon):
    def __init__(self,name,bullet):
        self.bullet = bullet
        self.name = name 
        self.attackPoint = 20
    def use(self):
        self.fire()
    
    def fire(self):
        if self.bullet >= 1:
            self.bullet -= 1 
            print("빵야~ ")
        else:
            print("틱~")
    def reload(self):
        self.bullet = 20 
        print("20발 재장전 되었습니다.")

class Grenade:
    def __init__(self,name,bullet):
        self.bullet = bullet
        self.name = name 
        self.attackPoint = 50
    def fire(self):
        if self.bullet >= 1:
            self.bullet -= 1 
            print("펑~ ")
        else:
            print("수류탄이 없다~")
    def reload(self):
        self.bullet = 3 
        print("3발 재장전 되었습니다.")


class Bomb:
    def __init__(self,name,bullet):
        self.bullet = bullet
        self.name = name 
        self.attackPoint = 100
    def fire(self):
        if self.bullet >= 1:
            self.bullet -= 1 
            print("펑~ ")
        else:
            print("폭탄이 없다~")
    def reload(self):
        self.bullet = 3 
        print("3발 재장전 되었습니다.")

class Knife(Weaphon):
    def __init__(self,name):
        self.name = name 
        self.attackPoint = 5
    def use(self):
        self.equip()
    def equip(self):
        print(self.name,"을 착용하였습니다.")




class Player:
    def __init__(self,name):
        self.name = name 
        self.hp = 100
        self.grenade =None
        self.knife = None
        self.bomb =None
        self.gun = None

    # def receive_grenade(self,grenade):
    #     self.grenade = grenade   
    # def receive_knife(self,knife):
    #     self.knife = knife
    # def receive_bomb(self,bomb):
    #     self.bomb = bomb
    # def receive_gun(self,gun):
    #     self.gun = gun

    def receive(self,weaphon):
        self.weaphon = weaphon
    def use(self):
        self.weaphon.use()
    



    def use_weapon(self):
        if self.gun != None:
            self.gun.fire()
        else:
            print("총이 없습니다.")
        
        if self.grenade != None:
            self.grenade.fire()
        else:
            print("수류탄이 없습니다.")
        if self.knife != None:
            print("칼을 착용했습니다.")
        else:
            print("칼이 없습니다.")
        if self.bomb != None:
            self.bomb.fire()
        else:
            print("폭탄이 없습니다.")            







    
p1 = Player("홍길동")

g= Gun("ak",20)
k= Knife("칼")
gd= Grenade("수류탄",3)
b= Bomb("폭탄",3)

p1.receive(g)
p1.receive(b)
p1.receive(gd)
p1.receive(k)


p1.use()