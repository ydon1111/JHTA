     
# dan = int(input("단수를 입력하세요"))

# value = 0 
# for mu in range(1,10):
#       value += mu
#       print(str(dan) + " * " + str(mu)  ,  "=" , str(dan*mu) , value)

      #디버그 == 숫자 옆에 빨간점을 찍고 확인해봄  단축키 'f9' 


# 1부터 50 사이의 홀수를 리스트로 만들어 반복문으로 화면에 출력 




# for ev in range(1,50,2):
#     print(ev)

# k = [ 3, 6, 9, 12 ,15 , 18]

# for i in  enumerate(k):
#     print(i)

# enumerate
# k[index] 
# 인덱스 번호 , 컬렉션의 엘리먼트 ==> tuple 형태로 반환


# 리스트
m=[]
m.append(100) # 리스트에  추가 
m.append(200) # 리스트에  추가 
print(m)

#n 리스트에 500, 300 두개의 요소를 추가 
n=[]
n.append(500) # 리스트에  추가 
n.append(300) # 리스트에  추가 
print(n)

print(m+n)

print(list("닭백숙"))




# "880101-1234567"
# 88년 01월 01일  1 

id = "880101-1234567"
print(str(id[0:2])+'년',str(id[2:4]+"월"),str(id[4:6]+"일"),id[7])



s = "천만 탈모인 희소식 들판 야생화에서 발모제 성분 발견".split()
print(s)

# index
print(s[0])


print(s[3])


print(s[-1]) #뒤에서 부터 문자를 찾음 


print(s[1:3]) #list를 자르는 특별한 문법. 

print(s[1:5]) #리스트명[시작인덱스:종료인덱스:stop]종료인덱스의 원소는 포함되지 않고 바로 앞요소까지만 포함


# 들판 야생화에서 발모제 
# s리스트에서 일부를 슬라이싱 해서 k 리스트를 만들고 
# k 출력
k = s[3:6]
print(k)



t = "동해물과 백두산이 마리고 닳도록 하느님이 보우하사 우리나라 만세".split()
t2 = t[4:] #t2 = t[:] 처음부터 끝까지 
print(t2)

# 반복문을 사용해서 출력 

for song in t2:
    print(song)


print("--------------------------")

print(t[::2]) #건너뛰고 불러오기 

print(t[::-1]) #뒤에서 부터 출력 



#정렬해서 출력
#정렬
# 
# bubble sort 
# 
a = [3,0,1,8,7,2,5,6,9]
a.sort()     #숫자정렬
print(a)
a.reverse()  #숫자 역으로 정렬
print(a)




def bubbleSort(x):
	length = len(x)-1
	for i in range(length):
		for j in range(length-i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x 





#1부터 100까지의 값을 요소를 갖는 k리스트를 작성 
#25~45번까지 요소를 잘라 v 리스트를 생성

#반복문을 사용해서 홀수번째 요소만 출력
print("------------------------------------")

k = list(range(1,101))  #리스트 만들기 숫자 넣어서
v = k[24:45]



# for ev in v:
#     print(ev)

# for ev in v[::2]:
#     print(ev)

# for ev in v: 
#    if((ev%2)==1):
#        print(ev)
   

