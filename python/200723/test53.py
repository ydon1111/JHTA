#내장함수

print(sum([10,20,30]), sum((10,20)),sum({2,3}))

print(bin(8))                                # 이진수
print(int(2.7),float(3),str(5)+'오')

a = 10
b = eval('a + 5')                          #str 로 되어 있어도 계산 진행

print(b)

print(round(1.2),round(1.6))
print('---------------------------')
import math

print(math.ceil(1.2),math.ceil(1.6))        #정수 근사치중 큰수 
print(math.floor(1.2),math.floor(1.6))      #정수 근사치중 작은수 

print('-------------------------------')

bList = [True,1,False]

print(all(bList)) #True and 1 and False
print(any(bList)) #True or 1 or False


# factorial

# print(factorial(5))

def savg(x):
    print(x)


def do1():
    print('첫번째 함수실행중')

def do2():
    print('두번째 함수실행중')

def do3():
    print('세번째 함수실행중')
    do1()
    do2()
    print('세번째 함수 끝')

do3()                                 #함수에서 다른함수 호출 가능 

print('--------------------------------')


    #재귀적 호출 (무한루프)
def sayHello(cnt):
    cnt-=1 
    print('Hello~~~~~')
    if cnt > 0:
        sayHello(cnt)
    
sayHello(5)


# def factorial(a):
#     k=1
#     for i in range(a,1,-1):
#         k = k*i    
#     print(str(a)+ "! =",k)
#     return k


def factorial2(n):
    if n==1:
        return 1
    return n*factorial2(n-1)
    
    
print(factorial2(5))


def fibonacchi(n):
    if n<=1:
        return n 
    return fibonacchi(n-1)+fibonacchi(n-2)

print(fibonacchi(6))


