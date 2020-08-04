'''
1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 


def avg(a, b):
    pass


avg(200,100)    
'''
# def avg(a, b):
#     return int((a+b)/2)

# print(avg(200,100))  


'''
2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.

sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

def max_min(listData):
'''


# sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

# def max_min(listData):
#     import math 
#     print(max(listData),min(listData))
          
# max_min(sList)

'''
3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.


def get_list(path):
    pass
'''

# def get_list(path):
#    import os
#    for i in os.listdir(path):
#     if i.endswith('.txt'):    #??
#         print(i)

# print(get_list('e:/dev/python_workspace/'))


'''
4. 오늘의 월 일을 출력하는 함수를 작성하세요 

def get_todate():
    pass


print(get_todate())   # 7월 27일 
'''

# def get_todate():
#     import time   
#     return print(time.gmtime().tm_mon,'월',time.gmtime().tm_mday,'일')

# get_todate()



'''
5.  다음 함수를 작성하세요 


def get_triangle_area(width, height):
    pass


print(get_triangle_area(100,200))  # 10000
'''
# def get_triangle_area(width, height):
#     return int((width * height)/2)


# print(get_triangle_area(100,200))


'''
6. 


def get_circle_area(radius):
    pass


print(get_circle_area(10))  # 314.1592653589793
'''
# def get_circle_area(radius):
#     import math
#     return radius * radius * math.pi

# print(get_circle_area(10))


'''
7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 

nList = []
'''

# import random

# nList = []                              
# for i in range(20):
#     n = random.randint(1,100)
#     nList.append(n)    

# print(nList)

'''
8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 

print(get_odd(nList))  # n
'''

# def get_odd(nList):
#     r = []
#     for i in nList: 
#         if i%2 != 0:
#             r.append(nList)
#     return len(r)

# print(get_odd(nList))

'''
9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 

wordList = []   # wordList = ['abcde', 'xwdsd, ....]
'''

# import random
# wordList = [] 
# for r in range(20):
#     k = ''
#     for i in range(5):
#         r = chr(random.randint(97,122))
#         k += r
#     wordList.append(k)
# print(wordList)


# rand_small = [chr(random.randint(97, 122)) for i in range(5)]

# wordList = ''.join(rand_small)

# print(wordList)

'''
10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요

print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]
'''

# def get_last_word(wordList):
#     k= []
#     for i in wordList:
#         i = i[2:5]
#         k.append(i) 
#     return k 

# print(get_last_word(wordList))






'''
11. 지금까지 만들어진 함수를 test 라는 모듈로 작성하세요
'''


'''
12. 현재 파일에서 실행할때만 테스트 결과가 출력되게 작성하세요 
'''
'''
13. ex1.py 파일을 작성하고  test. get_circle_area(300)을 실행시켜보세요
'''

'''
14. 다른 모듈의 함수를 불러 사용하는 방법 3가지를 정리하세요 
'''
#임포트 하는 방법 3가지
# 1.import 모듈명

# import random
# import math

# 2. from 모듈명 import 함수명 

# from random import randint
# from deabak import randint  다른 모듈에 동일한 함수가 있을 경우 충돌날 우려 있음

# n = randint(100,200)
# print(n)

# print(dir())

# 3. from 모듈명 import *

# from random import *
# print(dir())
'''
15. 비의 깡 가사를 rain.txt 파일에 저장하세요 
'''
# ggang = """
# Yeah 다시 돌아왔지
# 내 이름 레인(RAIN)
# 스웩을 뽐내 WHOO!
# They call it! 왕의 귀환
# 후배들 바빠지는 중!
# 신발끈 꽉 매고
# 스케줄 All Day
# 내 매니저 전화기는
# 조용할 일이 없네 WHOO!

# 15년을 뛰어
# 모두가 인정해 내 몸의 가치
# 허나, 자만하지 않지
# 매 순간 열심히 첫 무대와 같이
# 타고난 이 멋이 어디가
# 30 sexy 오빠
# 또 한번 무대를 적셔
# 레인이펙트
# 나 비 효과

# 화려한 조명이 나를 감싸네
# 시간이 멈추길 기도해
# but, I’m not gonna cry yeah
# 불 꺼진 무대 위 홀로 남아서
# 떠나간 그대의 목소릴 떠올리네
# 나 쓰러질 때까지 널 위해 춤을 줘

# 허세와는 거리가 멀어
# 난 꽤 많은 걸 가졌지
# 수많은 영화제 관계자
# 날 못 잡아 안달이 나셨지
# 귀찮아 죽겠네 알다시피
# 이 몸이 꽤 많이 바빠
# 섭외 받아 전세계 왔다 갔다
# 팬들이 하늘을 날아 WHOO!

# TV 드라마, 영화 yeah!
# I get it all
# 이젠 모두를 붙잡을 노래를 불러
# 볼륨은 올리고
# 재 등장과 동시
# 완전 물 만나 call me 나쁜 오빠
# 무대를 다시 한번 적시지
# 레인이펙트
# 나 비 효과

# 화려한 조명이 나를 감싸네
# 시간이 멈추길 기도해
# but, I’m not gonna cry yeah
# 불 꺼진 무대 위 홀로 남아서
# 떠나간 그대의 목소릴 떠올리네
# 나 쓰러질 때까지 널 위해 춤을 줘
# """

# with open("./day9/rain.txt", "w", encoding="utf-8") as file:
#     file.write(ggang)




'''
16.
	rain.txt 에서 4글자 단어는 모두 몇개인가? 
'''




# with open("./200727/rain.txt",'r',encoding='utf-8') as file:
#     data = file.read().split()
#     k = []
#     for i in data:
#         if len(i) == 4:
#            k.append(i)
#     print(len(k))




# total = 0
# for i in range(len(msg)):
#     if len(msg[i])==4:
#         total = total+1   카운트할때 사용 
 



'''
17.
	
	
	사용자가 입력한 디렉토리의 파일과 디릭토리 목록을 dir.txt 파일에 저장하세요
	
	입력: c:/
'''

# data = input("c:/")

# with open("./200727/dir.txt",'w',encoding='utf-8') as file:
#     file.write(data)
   




'''
18.
	로또 번호를 생성해서  lotto.txt 파일에 한줄씩 저장하세요 
ex)
	3
	15
	29
	32
	35
	41
'''

# lotto = []
# import random 
# i =0
# while i<6:
#     num = random.randint(1,45)
#     if num in lotto:
#         continue                  
#     else:
#         lotto.append(str(num))
#         i+=1
#     lotto.sort()


# with open("./200727/lotto.txt",'w') as file:
#     file.writelines('\n'.join(lotto))



'''
19.
	랜덤하게 소문자 3자를 생성해서  randomchar.txt 파일에 저장하세요 
'''
# import random
# k = ''
# for i in range(3):
#     k += chr(random.randint(97,122))
#    
# print(k)

# with open("./200727/randomchar.txt",'w') as file:
#     file.write(k)



'''
20.  다음 내용을 stock.csv 로 저장하세요 

	종목번호  회사명   현재주가 
	035720  카카오   326500
 	005930  삼성전자  55600
	047820  초록뱀     1590 
'''


# with open("./200727/stock.csv",'w') as file:
#     file.write(
#         '\n035720,카카오,326500'
#  	    '\n005930,삼성전자,55600'
# 	    '\n047820,초록뱀,1590'
#     )