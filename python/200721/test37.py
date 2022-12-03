'''
    dict : 키 : 값 의 쌍으로 이루어짐 , 순서 x
    키 와 값 으로 매핑되어 있는 순서가 없는 집합

    언어 : JSON  

'''

mydic = dict(k1=1,k2='abc',k3=3.4)
print(mydic)

dic = {'파이썬':'뱀','자바':'커피','오라클':'예언자'}

print(dic,len(dic))
print(dic['자바'])
dic['스미스']='백그라운드프로세스'
print(dic)
dic['neo']='주인공'
dic['스미스']='bg'
print(dic)
dic['neo']='잘생김'
print(dic)
# print(dic[0])  안됨
# dic.clear()
# print(dic)

print('-----------------')
for key in dic:
    print(key,dic[key])


print('-----------------')
# value 들만 출력 
for val in dic.values():
    print(val)
print('-----------------')
#key,value 모두 한꺼번에 출력 
for key,val in dic.items():
    print('key = ',key,', value = ',val)
    print('key = {key} , value  = {val}'.format(key=key, val=val))
print('-----------------')
print('neo' in dic)
print('-----------------')
#neo 삭제
del dic['neo']
print(dic)
print('-----------------')
dic['game']=['대항해시대','바람의나라','문명6','토탈워']
print(dic)
dic['broadcasting_co']=['kbs','mbc','sbs','ytn','jtbc']
print(dic)
print('-----------------')

from pprint import pprint as pp 

pp(dic)



#과일명 와 과일생산지 을 dictionary 로 작성

fruit ={'딸기':['논산','하우스'],'사과':'대구','귤':'제주도','망고':'필리핀'}


#딸기 생산지를 출력
print(fruit['딸기'])
#망고 생산지를 출력 
print(fruit['망고'])
#과일명:새안지 형식으로 전체 출력

for key,val in fruit.items():
    print(key,val)
    
















