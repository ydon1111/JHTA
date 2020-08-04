def show_info(name,job,age,addrs,height):
    print("이름 : {0}, 직업: {1}, 나이: {2}, 사는곳: {3}, 키: {4}".format(name,job,age,addrs,height))


p = {'name':'홍길동','job':'도적','age':20,'addrs':'율도국','height':180.3}
# show_info('홍길동','도적',20,'율도국',180.3)
#이름:홍길동 직업:도적 나이:20 사는곳:율도국 키:180.3

# show_info(**p)      #** ==>  value 값 알려줌
# print('------------------------------------------------------------')
# show_info(*p)      #*   ==>  key 값 알려줌
# print('------------------------------------------------------------')
# def test(a,b,c):
#     print("a :", a)
#     print("b :", b)
#     print("c :", c)

# test(b=20,a=10,c=30)



# x = [10,20,30]
# def sumValue(a,b,c):
#     return a+b+c    

# print(sumValue(*x))   # * ==> 여러개를 가지고 있음

# #가변인수로 함수 만들수있다.
# def sumValue2(*args):
#     print("b :", args)

# sumValue2(x)


# def show_info2(**kwargs):
#     for kw,arg in kwargs.items():
#         print(kw,":",arg,seq='')

# # print(p)

# show_info2(name="홍길동")
# show_info2(**p)

# find_birth("880101-1234567")
# 88년 1월 1일 


def find_birth(ssn):
    print(ssn[0:2]+"년"+ssn[2:4]+"월"+ssn[4:6]+"일")

find_birth("880101-1234567")
