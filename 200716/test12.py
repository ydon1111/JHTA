#문자열

name = 'my name is "KS" ' #문자열에 종류별로 사용 
print(name)

sorry = "i'm sorry"         #문자열에 종류별로 사용 

print(sorry)

hobby = " cyber \t fishing "    #문자열에 종류별로 사용 
print(hobby)


print("----------------------------------")

# 5개의 정수형 변수에 10 20 30 40 50 값을 대입 

# a = 10
# b = 20
# c = 30 
# d = 40
# e = 50

a,b,c,d,e = 10 ,20 ,30 , 40, 50
print(a,b,c,d,e)

#리스트 
#목록 :[] 대괄호 묶어 준다. 각각의 값을 Element 
# element의 구분은 , 로 한다 

a = [10,20,30,40,50] #a에 숫자를 목록으로 담음
print(a)

print(a[0])
#40을 출력
print(a[3])

print("--------------------------------------")


# 빈 리스트 작성
m = []
# 연속된 값 만들기

print(range(0,10))
m = list(range(0,10)) 
print(m)

#10부터 19까지 10개의 연속된 숫자로 된 k list를 만들고 화면에 출력 

k = list(range(10,20,2))  
print(k)

print(list(range(100,0,-1)))  # 100부터 줄여가며 나열 

# 1부터 1000 사이의 3의 배수를 목록으로 출력

print(list(range(3,1000,3))) # 3부터 1000까지 3의 배수로 출력 

# 달의 표면 온도 밤 : -170   낮 120 도  3도씩 상승한다고 가정 했을때 
# 온도의 변화를 리스트로 만들어 출력

print(list(range(-170,121,3) ))

print(m)
print("m[3] :" ,m[3])  #m에 3추가 

m[3] = 200             #m에 있는 3을 200으로 변경
print("m[3] :" ,m[3])

# 각각의 요소에 값을 추가 , 변경 , 삭제 


