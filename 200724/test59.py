'''
정규표현식(regular expression) : 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
'''
import re

# re.match('패턴','문자열')

print(re.match('Hello','Hello python world'))

#문자열: .find()

i = 'Hello python world'
print(i.find('Hello'))

#첫글자가 H 시작인 글자 찾기  ^
#^H 
print(re.search('^H','Hello python world'))
#마지막 글자가 d 인 글자찾기  $ ????
#d$ ????
print(re.search('d$','Hello python world'))

print('------------------------------------')
# 010-1234-5678
print(re.match('[0-9+]','1234'))  # + --> 1개 이상
print(re.match('[0-9*]','1234'))  # * --> 0개 이상

#aaabbb => a가 1개이상 있는지?

print(re.match('a+','aaabbb'))

print(re.match('a+b','aaabbb'))


# msg = "aaa bbb 필라테스 힘들어 육체노동 eee smith@naver.com 010-1234-5678 aaa@gamil.com".split()



# print(list(filter(lambda x : x.find('@') != -1,msg)))

print(re.match('a+b','aaabbb'))
print(re.match('[가-힣]+','불금달료보자.'))

# + : 1개이상, * : 0개이상 , ? : 0 or 1 

#ab9cd , ab9999cd
print(re.match('ab[0-9]?cd','ab9cd' ))
print(re.match('ab[0-9]?cd', 'ab99999cd'))

