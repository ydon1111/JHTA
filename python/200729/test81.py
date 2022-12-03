import time
class ATM:
    def __init__(self):
        print('초기화 함수 호출됨')
        self.__balance = 0      # 변수명 앞에 _ 를 사용하면 내부에서만 사용하자는 약속 하지만 외부에서 작동은함 __ 사용하면 강제로
        self.name='홍길동'
        #setter, getter 접근이 제한된 요소들에 접근하기 위해서 
    def get__balance(self):
        print('잔액 : ',self.__balance)

    def set__balance(self,balance):
        self.__balance = balance 
        
    def deposit(self,money):
        self.__balance += money
        print(money,"원 입금합니다.")
        print("현재 잔액 : ", self.__balance)
      
       
        
    def withDraw(self,money):       
        if self.__balance >= money:
            self.__balance -= money
            print(money,"원 출금합니다.")
          
        else:
            print("잔액이 부족합니다.")
        print("현재 잔액 ",self.__balance)

auto = ATM()

print(auto)

auto.deposit(100)
auto.set__balance(5000)             #set 을 사용해서 내부변수를 변경함 
auto.__balance = 99999999999999     #변수명만 같다고 생각하고 새로운 항목으로 인식하고 만듬 
# print(auto.__balance)
auto.withDraw(10000)