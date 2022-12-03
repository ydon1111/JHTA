class Test:
    def __init__(self,balance):
        print('초기화 함수')
        self.balance = balance
    
    def print(self):
        print("잔액 : ",self.balance)

t = Test(500)
t.aaa = 200

t.print()
print(t.aaa)