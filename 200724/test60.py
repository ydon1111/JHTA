import re

p = re.compile('[a-z]+')
print(p,type(p))
#패턴 : 정규식을 컴파일한 결과 

#문자열 검색 
#match() : 문자열의 처음부터 정규식과 매치되는지 조사
#search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사 
#findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
#finditer() : 정규식과 매치되는 모든 문자열을 반복가능한 객체로 돌려준다.

m= p.match('regular expression')
print(m)

if m:
    print(m.group())
else:
    print("no match")


print('-----------------------------------------------------')
result = p.search("99999999 aaaaaabbbbb")
print(result)

result2 = p.findall('hello pyton world today is monday')
print(result2)

#for문으로 1개씩 출력 
for i in result2:
    print(i)

print('----------------------------------------------------')

result3 = p.finditer('today is monday life is a blow')
print(result3)
for data in result3:
    print(data)
    print(data.group())
    print(data.start(), ":", data.end())


msg = '999,999 smartphone bbb@naver.com aaa@gmail.com'

#이메일만 선택해서 출력 

p2 = re.compile('[a-zA_Z0-9.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+')      #찾아낼 조건을 부여 
print(p2)

result4 = p2.findall(msg)                                       #찾아낸 조건을 리스트로 만듬
print(result4) 
for email in result4:                                           #for 문을 이용해 하나씩 꺼냄
    print(email)

