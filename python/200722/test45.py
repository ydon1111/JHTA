# def add(a,b):
#     '''add dang'''
#     return a + b

# def minus(a,b):
#     '''minus dang'''
#     return a - b 



# x = add(100,200)
# y = minus(200,100)

# print(x + y)

# help(add)
# help(minus)
# print('------------------------')

# def add_minus(a,b):
#     return a+b ,a-b


# x,y = add_minus(300,100)    # x  ==> a+b // y ==> a-b
# print("x : ",x,"y : ",y)

# i,j=(1,2)           둘다 tuple
# i,j = 1,2
# i,j =[1,2]


# 함수의 리턴 값 : 정수 , 문자 , 실수 ,튜플, 리스트 ....

 #합계를 리턴합니다...: 300
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return True if n % 2 == 0 else False

result = map(is_even, target)
# result = filter(is_even, target)

print(list(result))
