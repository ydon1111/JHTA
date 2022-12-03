import random                #랜덤값 출력

for i in range(10):
    print(random.random()) # 0~1 사이의 실수값

for j in range(100):
    print(random.randint(1,6)) #1~6 사이의 정수값

print('----------------------------------------------------')

m= list(range(1,46)) #순서 0 , 중복 0 

print(m)

#랜덤하게 두개의 값을 출력

for i in range(1000):            
    a = random.randint(0,44)
    b = random.randint(0,44)

    # print("m[",a,"] :" ,m[a] , ",m[",b,"] :" ,m[b])
    m[a],m[b] = m[b],m[a]
    # print("m[",a,"] :" ,m[a] , ",m[",b,"] :" ,m[b])

n = list(range(6))
for j in range(6):  
      n[j] = m[j]             #위에선 랜덤으로 뽑는 수를 6개로 담음
n.sort()      
print(n)
print('------------------------------------------------------')

for i in range(6):
    print(n[i], end="\t")
print()


     

# m 리스트의 요소중 1개를 랜덤하게 뽑아 출력

# a = random.randint(0,44)
# print(m[a])
#print(m[random.randint(0,44)])
print('------------------------------')



# 1~46
# cnt 를 for 
# 1~46 자리꾸기 * 1000
# 1~6 자르기
# 정렬하기
# 프린트


cnt = int(input("몇번 : "))           #입력값 받기
m = list(range(1,46))                 #리스트 만들기
for k in range(cnt):                  #입력받은 수많큼 반복
    for i in range(1000):             # 1000번 섞음 
        a = random.randint(0,44)      # 0~44까지의 임의의 인덱스 번호 뽑음 
        b = random.randint(0,44)      # 0~44까지의 임의의 인덱스 번호 뽑음 
        m[a],m[b] = m[b],m[a]         #뽑은 인덱스 번호로 자리를 섞음

# m = [1,2,3,4,5,7, 6... 45]      

# a = 5
# b = 6

# m[5], m[6] = m[6], m[5]

m = []

    
    n= m[0:6]
    n.sort()
    print(n)
    
    # print(m) 