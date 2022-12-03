
#함수를 호출할때 다시 꺼내서 사용하는 함수 : 클로저 (Closure)

def plus_ten():
    a = 10
    def add(b):
        return a+b
    return add

cal = plus_ten()
print(cal(10))

print('----------------------------------------------------')

def plus_ten2():
    a = 10
    return lambda b : a+b 

cal2 = plus_ten2()

print(cal2(100),cal2(200))




