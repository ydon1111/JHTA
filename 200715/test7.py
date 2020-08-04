# 숫자형 변수
# 정수형 (integer) ==> int 
# 실수형 (float) 3.14 ==> float
# 복소수 (complex) 1.3 + 1.9j) ==> complex


# 동적타이핑 언어


a = 10 #변수설정 

print(type(a)) #속성확인

b = 3.14 #변수설정 

print(type(b))#속성확인

c = 1.3 + 1.9j #변수설정 

print(type(c))#속성확인

b = 20 #변수설정 

print(b, type(b))#속성확인


c = "10" #변수설정 

# print ( "a : " + a )
#  숫자형 자료는 + 사용 할 수 없음 
#  File "e:\dev\python_workspace\200715\test7.py", line 29, in <module>
#     print ( "a : " + a )
# TypeError: can only concatenate str (not "int") to str

# 형변환 :int() , float() , complex() , str ()
print ( "a : " + str(a) ) #문자열로출력 
print ( "b : " + str(b) ) #문자열로출력
print ( "c : " + c )   

# + == 연결연산자 

# a = 10 , b = 20 
# b = 10 , a = 20

# 임시변수를 만든다 : temp
# 첫번째 변수의 값을 임시변수에 담는다.
# 두번째 변수의 값을 첫번째 변수에 담는다.
# 임시변수의 값을 두번째 변수에 담는다.
# 끝 


temp = 0  #temp 임시값설정 
temp = a  #temp 에 a 값을 담는다  
a = b    
b = temp 

print ("a :" , a ,"b :", b)


# 위에 방식처럼 임시변수를 안만들고 바로 가능

a,b = b,a  #임시값을 설정하지 않고 바로 변경 

print ("a :" , a ,"b :", b)




x = 10
y = 10
z = 10
print ( "x :" , x , "y :" , y , "z :",z )


#파이썬에서 가능 
x = y = z =20  #한번에 변수값 설정 
print ("x :" , x , "y :" , y , "z :",z )

i,j = 100, 200  #한번에 다른 변수값들 설정

print ("i :" , i , "j :" , j)


# 아무것도 없는값 
x = None # 다른언어는 null 파이썬은 None 
print(x)

a = 100 # a변수에 100을 대입한다 . 

# 20을 증가 시킨 후 출력 


# a = a + 20 
# a변수의 값에 20을 더한후에 a변수에 그 값을 대입 


a += 20 #변수값 축약


print(a)

