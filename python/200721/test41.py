'''
    함수: 여러개의 실행문을 하나의 묶음으로 만든 실행단위 
    내장함수: 설치후에 포함되어있는 함수 
    사용자정의함수: 만들어 사용하는 함수     
'''



#*
#**
#***
# #****
# #*****

# #def 함수명():
# #      문장
# #      문장
# #      [return 반환값]

# def printStar(num):
#     for i in range(1,num):
#         print("*"*i)

# printStar(8)
# printStar(10)
# printStar(4)

# #  구구단 3단출력


# def gugudan(dan):
#     for i in range(1,10):
#         print(dan, " * ",i,"=",dan*i)

# gugudan(2)
# gugudan(9)

#1부터 지정한 숫자까지 누적된 값을 출력하는 함수

# def hap(num):
#     sum = 0 
#     for i in range(1,num+1):
#         sum += i 
#     print("1부터",num,"까지의 합은",sum)
# #지금 계산한 값을 날 호출(실행)한 코드에 전달하고 싶다.
#     return sum
#     print("하하하하하") #deadcode 

# print(hap(100))

# x= hap(50)
# y= hap(100)
# print(x+y)


#odd(숫자) 1부터 해당 숫자까지 홀수의 누적합

def odd(num,no):                     # , 를 사용해서 여러 매개변수를 만들수 있음
    sum = 0
    for i in range(1,num+1):
        if i%no == 0:
            sum += i
    print(sum)
    return sum                     #값을 내보내기 위해서 사용해야함 안쓰면 none 출력됨



a = odd(8,2)
b = odd(9,3)

print(a+b)







