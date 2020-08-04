#1.랜덤하게 10개의 숫자를 생성 (1~990 사이 숫자)
#2.이것을 리스트에 담는다.
#3.임시변수를 선언한다. 
#4.리스트의 모든 요소와 비교해서 큰값을 임시변수에 담는다.
#5.임시변수에 들어있는 값이 최대값 출력



import random

data = []                              
for i in range(10):
    n = random.randint(1,990)
    data.append(n)                       #랜덤숫자를 리스트에 담음 append
print(data)

temp = -1
for j in data:                           # 반복문을 사용해서 리스트에 모든 요소를 출력
    if  j > temp :
        temp = j 

print(temp)

temp = 999999999999
for j in data:
    if j < temp:
        temp = j

print(temp)

print(min(data),max(data))