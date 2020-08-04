def sayHello():                   #함수안에 다른 함수를 넣음
    msg = '니하오'
    def prt():
        print(msg)
    prt()

sayHello()

print('------------------------------------------')

def f1():
    a = 10      # f1의 지역변수 a
    def f2():   #f1안에 있는 중복함수 f2
        nonlocal a     #위에 지역변수에 값을 대입함
        a = 20   #f2의 지역변수 a
    f2() 
    print(a)

f1()

