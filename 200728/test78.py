import time
import log
class ATM:
    def __init__(self):
        print('초기화 함수 호출됨')
        self.balance = 0 
        self.name='홍길동'

    def deposit(self,money):
        self.balance += money
        print(money,"원 입금합니다.")
        print("현재 잔액 : ", self.balance)
        log.saveLog("./200728/bank.log", money, self.balance,False)
       
        
    def withDraw(self,money):
        #db에 연결해서 현재 진짜 잔액이 존재하는지
        # 권한은 있는지 
        # 감사기록을 남긴다. 

        # 작업디렉토리에 bank.log 파일을 생성 
        # 지금시간, 출금액 , 현재 잔액         
        if self.balance >= money:
            self.balance -= money
            print(money,"원 출금합니다.")
            log.saveLog("./200728/bank.log",money,self.balance,True)
        else:
            print("잔액이 부족합니다.")
        print("현재 잔액 ",self.balance)

    
       


auto = ATM()

print(auto)

auto.deposit(600)
auto.withDraw(100)