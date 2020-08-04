
# class 클래스명: 
#     속성

#     함수,method()
#     객체 : 사물
#     class: 설계도
#     대상 : instance 

class Human:
    #__ 메서드를 매직메서드 
    def __init__(self):
        print("초기화 함수")
    def eating(self):
        print("냠냠 맛있게 먹어요")
    def sleeping(self):
        print(" 쿨쿨.. 쿨쿨 zzzzz") 



hong = Human() #instance    다른언어에서는 hong = new Human() 통해 새로만듬 
print(hong)
hong.eating()
hong.sleeping()

print('--------------------------------------------------------')

lucy = Human()
lucy.eating()
lucy.sleeping()

