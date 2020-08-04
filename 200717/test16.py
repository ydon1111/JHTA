'''
자료형 :
'''

s = 'sequence'

print(s,len(s),s.count('e'),s.find('e'))
print(s.find('e',3),s.rfind('e'))


ss = 'mbc'

print('mbc', type(ss), id(ss))

print("문자열 자르기")

print(s, s[2:4], s[:3], s[3:], s[3::2]) 

msg = "          Hello Python             "
print(msg)
print(msg.strip())
print(msg.rstrip()+"^^")
print(msg.lstrip())

msg = "구정,  신정,  크리스마스,   초파일,   추석"

# m 리스트 
# 반복문 출력 

m = msg.split(",")

for i in m:
    print(i)


msg3 = list('hello')
print(msg3)

str_time = ['10','44','30']
print(":".join(str_time))

#문자열을 , 단위로 짤라서 리스트 ==> split(",")
#리스트에 , 문자를 붙여서 문자열로 ==> ",".join(리스트)

msg3 = list('hello')
print(msg3)

print(msg3[4])
msg3[0] = 'm'
print(msg3)