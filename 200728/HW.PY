# class Marine:
#     def __init__(self):
#         self.hp = 100
#         self.attackPoint = 4
#         self.name = 'Marine'
#         print('객체 초기화')

#     def attack(self,other):
#         if other.hp > 4:
#             other.hp -= self.attackPoint
#             print("마린이",other.name,"공격하였습니다")
#         else:
#             print("고마해라..많이 묵었다")
#         print("체력이 %d 상태입니다"%other.hp)

#     def useSteamPack(self):
#         if self.hp >= 6:
#             print("힘이 쏫아요!!")
#             self.hp -= 5
#             print("체력이 %d 상태입니다"%self.hp)
#         else:
#             print("체력이 부족합니다.")

#     def move(self):
#         print("gogo")

# class Medic:
#     def __init__(self):
#         self.hp = 150
#         self.mp = 50
#         self.healPower = 7
#         self.defense = 3 
#         self.name = 'Medic'

#     def heal(self,target):
#         if target.name != 'SiegeTank':
#             target.hp += self.healPower
#             print('매딕이' ,target.name,'치료하였습니다','체력이',target.hp,'입니다')
#         else:
#             print("치료 못합니다.")
#         self.mp -= 10
    
#     def move(self):
#         print("gogogo")
#     def hold(self):
#         print("stop")

# class Ghost:
#     def __init__(self):
#         self.hp = 200
#         self.mp = 200
#         self.attackPoint = 4
#         self.nuclear = 4000
#         self.defense = 3 
#         self.name = 'Ghost'

#     def attack(self,other):
#         if other.hp > 4:
#             other.hp -= self.attackPoint
#             print("고스트가",other.name," 공격하였습니다")
#         else:
#             print("고마해라..많이 묵었다")
#         print("체력이 %d 상태입니다"%other.hp)       

#     def Nuclear(self):
#         print("고스트가 핵공격하였습니다")
#         self.mp -= 100
#         print("마나가 %d 상태입니다"%self.mp)    

# class SiegeTank:
#     def __init__(self):
#         self.hp = 400
#         self.x = 100
#         self.y = 100
#         self.attackPoint = 10
#         self.defense = 3 
#         self.name = 'SiegeTank' 

#     def attack(self,other):
#         if other.hp > 4:
#             other.hp -= self.attackPoint
#             print("시즈탱크가",other.name," 공격하였습니다")
#         else:
#             print("고마해라..많이 묵었다")
#         print("체력이 %d 상태입니다"%other.hp)     
    
#     def SiegeMode(self):
#         self.attackPoint += 30
#         print("시즈모드로 데미지가 30 늘어났습니다.")
#         print("공격력이 %d 상태입니다"%self.attackPoint)







# m1 = Marine()
# m2 = Marine()
# me = Medic()
# g1 = Ghost()
# g2 = Ghost()
# s1 = SiegeTank ()

# m1.attack(g1)
# me.heal(g1)
# g1.attack(m1)
# g1.attack(me)
# g1.attack(g2)
# g1.Nuclear()


# s1.SiegeMode() 
# m1.attack(s1)
# me.heal(s1)
# g1.attack(m1)
# g1.attack(me)
# g1.attack(g2)
# g1.attack(s1)
# s1.attack(m1)
# s1.attack(me)



# class TV:
#     def __init__(self): 
#         self.change = 1     
    
#     def turnOn(self):
#         print("tv가 켜졌습니다.")
#     def turnOff(self):
#         print("tv가 꺼졌습니다.")
#     def changeChannel(self,change):
#         print("tv 채널이 ",change,"로 변경되었습니다")

# t1 = TV()

# t1.turnOn()
# t1.turnOff()
# t1.changeChannel(5)


# class HandPhone:
#     def __init__(self): 
#         self.phone_number =' 011-1111-2222 ' 
      
#     def call(self,phone):
#         print(self.phone_number ,"에서",phone,"번으로 전화거는중")
 
#     def connect_internet(self):
#         print("인터넷이 연결되었습니다.")

# hp = HandPhone()
# hp.call("010-1234-5678")
# hp.phone_number = "010-1234-5678"
# hp.call("010-3333-4444")
# hp.connect_internet()