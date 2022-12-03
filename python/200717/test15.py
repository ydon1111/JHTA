# 자료형 확인
a = 10 
type(a)
print(type(a))
b = 10.5
print(type(b))
A=  1
print(A,a)


#진법 

print(bin(10), oct(10), hex(10))
#       2진수    8진수    16진수 

print(10,0o12,0xa,0b1010)

print(7+2j, type(7+2j))

#연산자 

v1=3  # = ==> 대입 연산자 
v1 = v2 = v3 = 5
# v1 = 5 ; v2 = 5 ; v3 = 5 
a=10 
b=20
print(a, b)

#자리바꿈
a,b = b,a 
print(a, b)

print("----------------------------------")

# *을 사용해서 리스트로 담음
a , *b = 1 , 2,  3, 4 ,5

print("a : ", a ,"b :", b)

print("----------------------------------")

*a,b,c = 10, 20 , 30 , 40 ,50 

print("a : ", a ,"b :", b , "c :", c )


#출력 
print(format(1.2345,'10.2f')) # c 
print("나는 나이가 20 살입니다") 
age = 20
print("나는 나이가" + str(age)+ "살입니다.")
print("나는 나이가 %d 살입니다."%21)             #숫자 %d
print("나는 나이가 %s 살입니다."%'스물한살')     #문자 %s 사용해서 변경 가능 

print("오늘은 %d월 %d일 이고 , %s 입니다"%(7,17,'제헌절'))  #여러개도 가능함 

print("이름은 %s이고 키가 %4.1f 입니다"%('홍길동', 199.9))
print("----------------------------------------------------")

print("이름은{0}, 나이는 {1} ".format('뽀로로',13))
print("이름은{1}, 나이는 {0} ".format('뽀로로',13))
print("이름은{}, 나이는 {} ".format('뽀로로',13))
print("이름은{0}{0}{0}, 나이는 {1} ".format('뽀로로',13))

#연산자 
print(5+3, 5-3, 5*3 , 5/3 , 5//3 , 5%3 , divmod(5,3))
#divmod (몫 , 나머지 )
print(5**3) #5의 3승 
print( 5>3 , 5==3 , 5<=3)
print(5>3 and 4<3 , 5>3 or 4<3 , not(5>3))

print("대"+"한"+"민국"+"만세")
print("나이 :" +str(5000), str(5) + '3')

print("만세"*10)

print("----------------------------------------------------------")

a = 5 
# a = a + 1 
a += 1 # a++ , ++a  안됨  
print(a)
print("부호 변경",a,-a, a*-1,-a)

print('boolean : ', bool(0),bool(1),bool(2))
print(bool(-2), bool(None), bool(''), bool(True), bool(False))

# print('c:\\name\python\\table') #\ 사용시 \n , \t 등으로 인해 다른게 나옴 \\ 또는 / 사용해서 경로변경 
print(r'c:/name/python/table') #raw data 

