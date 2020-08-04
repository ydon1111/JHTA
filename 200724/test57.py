#파이썬의 함수는 모두 일급 함수 
#함수를 다른 함수의 인수로 전달할수 있다
#반환값으로 함수를 사용할수 있다.
#변수에 지정할수 있다. 


def add(a,b):
    return a+b 

# print(add(100,200))

plus = add

print(plus(500,400))

def appendFunction(f1,c,d):
    return f1(c,d)

print(appendFunction(add,1000,2000))


