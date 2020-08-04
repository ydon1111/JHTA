
#객체 : mutable , immutable 

#immutable : bool , int, float, tuple,str 
# mutable : list , set,dict

a = 100  # a변수에 100라는 값을 대입
b = a    # b변수에 a변수의 값을 대입


print(type(a),type(b))

print(id(a), id(b))
a = a +1
print(id(a), id(b))

print('-------- list ----------')
m= [1,2,3]
n=m
print(id(m),id(n))

print(n[0])
n[0] = 100

print("n[0] :", n[0], "m[0] :", m[0])
print("id(n) : ", id(n),"id(m) : ", id(m))

print('--------------------')
k=m[:]
print(id(m),id(k))

print("k[0] :", k[0], "m[0] :", m[0])
print("id(k) : ", id(k),"id(m) : ", id(m))


print('--------------------')

c = [10,20,30]
d = c[:]

print(id(c),id(d))
print(c==d)               #내용이 같은지 확인

print(c is d)             #id가 같은지 확인
print('----------------------------------------------------------------')

q = [[1,2],[3,4]]

p = q[:]                     #id를 변경하게 만듬

print(id(q),id(p))           #다른 값
print(id(q[0]),id(p[0]))     #내부의 객체는 같은주소 

q[0][0]=5

print(q[0][0],p[0][0])
print(id(q),id(p))           #다른 값
print(id(q[0]),id(p[0]))     #내부의 객체는 같은주소 

#shallow copy

#deep copy
import copy

s = [[1,2],[3,4]]        
t = copy.deepcopy(s)    #내부 객체도 다른주소로 복사
print("id(s) :",id(s),"id(t) :",id(t))
print("id(s[0]) :",id(s[0]),"id(t[0]) :",id(t[0]))

s[0][0] = 300
print(s[0][0],t[0][0])
print("id(s) :",id(s),"id(t) :",id(t))
print("id(s[0]) :",id(s[0]),"id(t[0]) :",id(t[0]))
