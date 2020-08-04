#tuple : list와 유사 , 읽기 전용

t = 'a' , 'b' , 'c' , 'd'
print(t,type(t))

t2 = ('a' , 'b' , 'c' , 'd')
print(t2,type(t2))

print(t2 , len(t2)) #len 요소의 갯수
print(t2.count('a')) #a 요소의 갯수
print(t2.index('b')) #index 번호

# x = (1,2,3)
# x[0] = 10
# print(x) #tuple 은 수정이 안됨 
x =(3, 4, 5, 6)
x2 = (3)
x3 = (3,)
print(x2, type(x2))
print(x3, type(x3))
print('------------------------------------')

print("x : ",x)
y = list(x)
y[2] = 30
print(y)
x = tuple(y)
print("x :", x)

print('-------------------------------------')
t1 = (10,20)

a,b = t1
a,b = b,a
t1 =(a,b)
print(t1)

# x = list(t1)
# x[0],x[1] = x[1],x[0]
# print(x)
# t1 = tuple(x)
# print(t1)

