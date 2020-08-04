'''
1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 


def avg(a, b):
    pass


avg(200,100)    
'''
def avg(a, b):
    return int((a+b)/2)

if __name__ == "__main__":  
    print(avg(200,100))  


'''
2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.

sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

def max_min(listData):
'''


sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

def max_min(listData):
    import math 
    print(max(listData),min(listData))

if __name__ == "__main__":         
    max_min(sList)

'''
3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.


def get_list(path):
    pass
'''

def get_list(path):
   import os
   for i in os.listdir(path):
    if i.endswith('.txt'):    #??
        print(i)

if __name__ == "__main__":
    print(get_list('e:/dev/python_workspace/'))


'''
4. 오늘의 월 일을 출력하는 함수를 작성하세요 

def get_todate():
    pass


print(get_todate())   # 7월 27일 
'''

def get_todate():
    import time
    r = time.ctime().split()
    
    return print(r[1],'월',r[2],'일')

if __name__ == "__main__":
    get_todate()



'''
5.  다음 함수를 작성하세요 


def get_triangle_area(width, height):
    pass


print(get_triangle_area(100,200))  # 10000
'''
def get_triangle_area(width, height):
    return int((width * height)/2)

if __name__ == "__main__":
    print(get_triangle_area(100,200))


'''
6. 


def get_circle_area(radius):
    pass


print(get_circle_area(10))  # 314.1592653589793
'''
def get_circle_area(radius):
    import math
    return radius * radius * math.pi

if __name__ == "__main__":
    print(get_circle_area(10))



'''
7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 

nList = []
'''

import random

nList = []                              
for i in range(20):
    n = random.randint(1,100)
    nList.append(n)    

if __name__ == "__main__":   
    print(nList)

'''
8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 

print(get_odd(nList))  # n
'''

def get_odd(nList):
    r = []
    for i in nList: 
        if i%2 != 0:
            r.append(nList)
    return len(r)

if __name__ == "__main__":
    print(get_odd(nList))

'''
9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 

wordList = []   # wordList = ['abcde', 'xwdsd, ....]
'''

import random
wordList = [] 
for r in range(20):
    k = []
    for i in range(5):
        r = chr(random.randint(97,122))
        k.append(r)
    p = ''.join(k)
    wordList.append(p)

if __name__ == "__main__":
    print(wordList)


rand_small = [chr(random.randint(97, 122)) for i in range(5)]

wordList = ''.join(rand_small)

if __name__ == "__main__":
    print(wordList)

'''
10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요

print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]
'''

def get_last_word(wordList):
    k= []
    for i in wordList:
        i = i[2:5]
        k.append(i) 
    return k 
if __name__ == "__main__":
    print(get_last_word(wordList))
