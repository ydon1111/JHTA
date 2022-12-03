# 1.변수명규칙
# A-Z , a-z , 0-9 
# 대소문자구분
# 첫글자는 문자 (숫자로 시작할수 없다 )
# 단_ 시작가능
# 특수문자는 사용할수 없다.(+,-,*,/,$,@,&,%)
# 예약어 x (if, for, while , and , or , ...) 
# 의미 있게 
# 2.
# def square(x):
#     return x*x 

# print(square(5))

# 3.
# print((lambda x : x*x)(5))

# 4.
# m = list(range(1,101)) 

# # def triple(m):
# #     k =[]
# #     for i in m:
# #         r = i*3
# #         k.append(r)
# #     return k
# def triple(n):
#     return n*3

# print(list(map(triple,m)))
# print(triple(m))    

# 5. 
# #map 리스트의 값을 하나씩 뽑아옴
# print(list(map(lambda i : i*3 ,m)))

# 6.
# import random 
# data = []
# for i in range(10):
#     k = random.randint(1,100)
#     if k in data:
#         continue
#     else:
#         data.append(k)
       
# print(data)
# print(max(data))
# print(min(data))

# 7.
# k = list(range(1,101))

# 8.
# print([k for i in range(1,101)])

# 9.
# print([i for i in range(1,101) if i%2 ==0])



