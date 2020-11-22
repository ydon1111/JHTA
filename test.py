'''
1.  사용자로부터 국어 , 영어, 수학 점수를 입력받아  총점과 평균을 출력 
'''

# x = int(input('국어점수 : '))
# y = int(input('영어점수 : '))
# z = int(input('수학점수 : '))

# totsum = x+y+z
# totmean = totsum/3
# print('총점 :' , totsum , '평균 :',totmean)

# x,y,z = input('국어, 영어, 수학 점수 입력 :').split() #한번에 여러숫자를 받음 split 을 통해서 받는값 구분
# x=int(x) #숫자로 출력 
# y=int(y) #숫자로 출력 
# z=int(z) #숫자로 출력 
# print('국어 :',x ,'영어 :',y, '수학 :', z)
# i = x+y+z #입력값 더하기 
# j = (x+y+z)/3 #입력값 더하고 나누기 


# x , y ,z = input("국어 ,영어 ,수학점수 입력 : ").split()
# x = int(x)
# y = int(y)
# z = int(z)


'''
2.
	1부터 100까지 출력 
'''

# for i in range(1,101):
#     print(i)
# print(list(range(1,101)))


'''
3. 아래의 결과를 출력하는 코드를 작성하세요 

1
2
3
4
..
99
100
'''

# for i in range(1,101):
#     print(i)

'''
4.

11111
22222
33333
44444
55555
'''

# for i in range(1,6):
# 	print(str(i)*5)

# for i in range(1,6):
#     # print(i,i,i,i,i)
#     print(str(i)*5)

'''
5

99999
88888
77777
66666
55555
'''

# for i in range (9,4,-1):
# 	print(str(i)*5)


# for i in range(9,4,-1):
#     # print(i,i,i,i,i)
#     print(str(i)*5)

'''
6.  이중for문 사용 
1234
5678
'''

# for i in range(2):
# 	for r in range(1,5):
# 		print(i*4+r, end = ' ')
# 	print(' ')


# for i in range(1,3):
#     for r in range(1,5):
#         if i <2 : 
#             print(r, end='')
#         else:
#             print(r+4,end='')
#     print()

# for i in range(2):
#     for r in range(1,5):
#         print(i*4+r, end='')
#     print()

'''
7. 

구구단8단 출력 
'''

# for i in range(1,10):
#     print('8' + '*' +str(i) + '=' +str(i * 8))

'''
8.

2단부터 9단까지 출력 
'''

# for i in range(2,10):
#     print(str(i)+"단")
#     for r in range(1,10):
#         print(str(i) + "*" + str(r) + '=' + str(i*r))

'''
9.  구구단 3단 을 옆으로 출력 

3   * 1 =  3   3 * 2 = 6   3 * 3 = 9 ...    3  * 9  = 27
'''

# for i in range(1,10):
#     print("3" + "*" + str(i) +'='+ str(3*i),end='  ')


'''
10. 

1
11
111
1111
11111
'''


# for r in range(1,6):
#     print('1'*r)

'''
11 .  5의 배수만 출력 
	0
	5
	10
	...
	100
'''

# for i in range(0,21):
#     print(str(5*i))


'''
12  1부터 100 합계를 출력
	5050
'''

# temp = 0
# for i in range(1,101):
# 	temp += i
# print(temp)

# sum1 = 0
# for i in range(1,101):
#     sum1 += i 
# print(sum1)


'''
13
	*
	**
	***
	****
	*****
'''
# for i in range(1,6):
#     print('*'*i)


'''
14
	1
	12
	123
	1234
	12345
'''
# a = ''
# for i in range(1,6):
# 	a = a+ str(i)
# 	print(a)

# a= ''
# for i in range(1,6):
#     a = a+ str(i)
#     print(a)


# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


'''
15.
	time Converter 

	시간입력:90061

	1일 1시간 1분 1초 입니다.	
'''
# timeConverter = input('초를 입력하세요')
# x = int(timeConverter)

# day = x//(24*60*60)
# hour = x%(24*60*60)//(60*60)
# minute = x%(24*60*60)%(60*60)//60
# sec =  x%(24*60*60)%(60*60)%60
# print(str(day)+ '일' +str(hour)+ '시' + str(minute) +'분' +str(sec)+'초')

# print(divmod(x,24*60*60)[0])
# print(divmod(divmod(x,24*60*60)[1],60*60)[0])
# print(
#     divmod(
#         divmod(
#             divmod(x,24*60*60)
#             [1],60*60)
#         [1],60*60)[0])


timeConverter = input('초를 입력하세요')
x = int(timeConverter)
day , na = divmod(x,24*60*60)
hour, na = divmod(na,60*60)
minute , na = divmod(na,60)
sec  = na
print(day,hour,minute,sec)


'''
16.

	잔돈교환기(큰 단위 화폐순으로 ) 

	입력 : 67921 

	50000권 : 1매
	10000권 : 1매
	5000권  : 1매
	1000권  : 2매
	500권   : 1개
	100권   : 4개
	50권    : 0개
	10권    : 2개
	1원     : 1개 
'''
# coin = input('돈을 입력하세요 : ' )
# coin = int(coin)
# money = [50000,10000,5000,1000,500,100,50,10,1]

# for i in range(9):
# 	mok, coin = divmod(coin,money[i])
# 	print(str(money[i])+'권 : '+str(mok)+'개')


'''
17. 	아래의 리스트를 정렬해서 출력하세요 
	[  4, 9 , 2, 6, 1, 3, 8 , 0,7,  5 ]
'''

# i = [  4, 9 , 2, 6, 1, 3, 8 , 0,7,  5 ]
# r = sorted(i)
# print(r)


'''
18.
	파이썬의 버젼확인 DOS명령은? 
'''
# python --version

'''
19. 파이썬에서 객체와 속성 또는 메소드 간의 연결을 위해 그들 사이에 쓰는 연산자는?
'''
# dot (.)

'''
20. import 키워드는 언제 가용하는가? 
'''

# 모듈사용할때 

'''
21. 파이썬 내장 객체중  딕셔너리의 특징은 ?
# '''
# key와 values값이 짝으로 이루어짐 
# key 값이 중복이 안됨


'''
22 .아래의 리스트를 set으로 변경하려고 한다. 변환 한 후에 결과를 출력하면 어떻게 될까?  
	m = [ 1, 2, 3, 2, 1, 5 3, 3, 2, 1]  
'''
# m = [ 1, 2, 3, 2, 1, 5, 3, 3, 2, 1] 
# print(set(m))

'''

23. 다음 코드가 실행될수 있는 class를 작성하세요 

sm = SuperMan("슈퍼맨", 20, "신문기자")

sm.fly()
sm.laser()
sm.eating("바나나")
sm.sleeping()

비행 : 날아보아요.~~~ 
어린시절 모두 해봤잖아요 : 비행... 비행청소년 ... 
찌이잉~~~~
바나나 을 먹어요 
쿨쿨 잡니다.
'''
# class SuperMan:
# 	def __init__(self,name,age,job):
# 		self.name = name
# 		self.age = age
# 		self.job = job
# 	def fly(self):
# 		print('비행 : 날아보아오.~~~')
# 	def laser(self):
# 		print('찌이잉~~~~')
# 	def eating(self,x):
# 		print(x+ '을 먹어요')
# 	def sleeping(self):
# 		print('쿨쿨 잡니다.')


# sm = SuperMan("슈퍼맨", 20, "신문기자")

# sm.fly()
# sm.laser()
# sm.eating("바나나")
# sm.sleeping()



'''
24.  아래 결과를 출력하는 GuGuDan 클래스를 작성하세요 

g = GuGuDan()

g.dan = 7

g.print()


'''

# class GuGuDan:		
# 	dan = None	
# 	def print(self):
# 		if self.dan == None:
# 			print('단을 입력하세요.')
# 		else:
# 			for i in range(1,10):
# 				print(str(self.dan) + "*" + str(i) + "=" + str(self.dan * i))

# g = GuGuDan()
# g.dan = 7
# g.print()




