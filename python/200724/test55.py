a = 10                     #전역변수
def prt():
    global a               # 전역변수 a 에 지역변수 a 를 담음 
    a=20                   # 전역변수 보다 지역변수가 우선됨 
    b=100                   #지역변수  : 해당 함수에서만 사용되고 사라짐
    print(a)
    print(locals())
    # print(b)
prt()
print('-------------------------')

print(locals())
print(a)
# print(b)  

