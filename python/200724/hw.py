# 1.
# 	다음을 람다식으로 수정하세요 

# def test(x):
# 	return x+10

# lambda x : x+10

'''
2. 
	"Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "

	문자열중 공백을 기준으로 몇글짜씩인지 알아 내려고한다. 파이썬 코드로 작성하세요 
'''
# import re 

# i = "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "
# k = re.findall('[A-Za-z가-힣()!]+',i)  

# for i in k:
#     print(len(i))
    


'''
3. 
	2번 문자열중 글자가 4자이상인 단어만 출력하세요 
'''
# for i in k:
#     if len(i) >=4:
#         print(i)


'''
4. 	도명: 도청소재지 로 만들어진 dictionary 가 있다. 
	do_city  = { "경기도":"수원", "강원도":"춘천"}
	
	dictionary 내포 표현식으로 출력 하세요 
'''
# do_city = { "경기도":"수원", "강원도":"춘천"}

# result = {city : do for city,do in do_city.items()}   #items ?????

# print(result)


'''
5. 
	지역변수와 전역변수의 차이점? 
'''

# 지역변수는 지역에서 사용되고 사라짐
# 전역변수는 계속 사용됨 


'''
6..
	다음 코드를 실행한후에 화면에 출력 되는 a의 값은 얼마인가? 
	a  = 100 
	def show():
	    a = 200
	    b = 100
	    print(a)  ==>ㄹ
	show()
	print(a)  ==>

	왜 차이가 날까요? 	
'''
# a = 100 전역변수를 우선으로 출력하고 
# 200 은 지역변수라 밖에서 출력 시 인식못함



'''
7. 
	a  = 100 
	def show():
	    ____________________
	    a = 200
	    b = 100
	    
	show()
	print(a) 

	200 으로 출력되게 해주려고한다. __________ 들어갈 코드는 ? 
'''

# global a



'''
8. 
	지역변수의 목록을 확인하려면 어떤 명령을 사용할까? 
'''

# locals()



'''
9.

	def fx():
	    data1  = 500    
	    def fx2():   
	        _____________________
	        data1 = 300  
	    fx2()
	    print(data1)
	fx()

	이 코드를 실행했을때 화면에 어떤값이 출력될까? 
'''
# 500 
# 지역 변수에 지역변수이므로 상위 지역변수값을 출력함 

# def fx():
# 	data1  = 500    
# 	def fx2():   
# 	    data1 = 300  
# 	fx2()
# 	print(data1)
# fx()


'''
10.
	출력 결과를 300 이 나오게 하려면 __________ 에 알맞은 코드는? 
'''
#  nonlocal data1

'''
11.
	일급함수의 특징 3가지를 정리하세요
'''
#함수를 다른 함수의 인수로 전달할수 있다
#반환값으로 함수를 사용할수 있다.
#변수에 지정할수 있다. 

'''
12.
	def  tax():
	    a = 1.1
	    def cal(b):
	        return a*b
	 return cal
	
	getTax = tax()
	print(getTax(1000))   # 출력결과는 ? 
'''

# 1100



'''
13.

	12번에서 cal 함수는 getTax 함수 호출할때 다시 꺼내서 사용되어지는데 
	이런 함수를 _________ 라고 한다. 
'''
# 클로저 (Closure)

'''
14. 
	일정한 규칙(패턴)을 가진 문자열을 표현하는 방법  ______________ 이라 한다.
'''

# 정규표현식(regular expression)

'''
15. 
	사용순서 
		1. 
		2. 
		3. 
'''
# 사용순서 
# 		1. import re
# 		2. 패턴 re.compile('[찾고자하는문자열]+')
# 		3. 문자열 검색 

'''
16.
	
	"Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 " 

	문자열중 전화번호만 찾아서 출력하고자한다. 
	파이썬 코드로 작성하시오.
'''

# i = "Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 ".split()

# print(list(filter(lambda x : x.find('-') != -1,i)))

'''
17.
	16번 문제를 정규표현식으로 작성하시오 
'''	

# import re 
# i = "Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 "
# k = re.findall('[0-9]+-[0-9]+-[0-9]+',i)  
# print(k)