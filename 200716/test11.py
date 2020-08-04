print(1+1)                   #더하기
a=10
print(a)
a=float(a)                   #실수로 출력 
print(a)
print(complex(1.3,1.4j))     #복소수로 출력 

print("-----------------------------------------")

# x = input("아무 값이나 하나 입력하세요")
# print("aaa", "bbb","cccc")
# print("x 의 값은 : " + x)

# "" , '' , ''' ''', """ """

print(3>5)  

a = 100 
b = 200
print(a<b) 
c = None 
print(c) 

print(100>2 and 300>100) #true
print(100>2 and 300>100 or 100>200)  #true

x = True 
y = False

print(x and y)  #true and true == true

print("-------------------------------------------")

print(True and True) 
print(False or True)  


print(not True) #true 가아니다 

a=300
b=200
print(a == b ) # == 같다 를 표시
print( a != b ) # !=  다르다 를 표시 

#국어 , 영어 ,수학 점수를 입력받기
# 60점 이하가 있다면 False(실패), True(합격)


x,y,z = input("국어, 영어 , 수학 점수를 입력하세요").split() #값을 입력받아 출력 
x = int(x)
y = int(y)
z = int(z)

print(x > 60 , y > 60 , z > 60)  # 입력 받은 값이 60보다 작으면 false
print("Total  :" , x >= 60 and y >= 60 and z >= 60) 

print("평균 :" )



  



