

# factorial(a) # 3! ==> 3*2*1

# factorial(b) # 5! ==> 5*4*3*2*1



# def factorial(a):
#     k=1
#     for i in range(a,1,-1):
#         k = k*i    
#     print(str(a)+ "! =",k)
#     return k



# x = factorial(3)
# y = factorial(5)

# print("x :",x,"y: ",y , "x+y =",x+y)

# 5*4*3*2*1 =120 형식으로 출력하는 factorial2() 함수를 정의하세요 
def factorial2(n):
    '''
    factorial함수
    '''
    k=1
    for i in range(n,0,-1):
        k = k*i
        if i >= 2:
            print(i,'*',end="  ")
        else:
            print(i,'=',end="  ")
    print(k)


factorial2(10)

# print(factorial2.__doc__)               #함수의 주석(document)을 보기 위해 사용하는 함수 
help(factorial2)                          #함수의 주석(document)을 보기 위해 사용하는 함수 
  
