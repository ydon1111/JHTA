'''
set : 순서  x , 중복 x 
'''

a = {1,2,3,1}

print(a , type(a))

# print(a[0]) 
b = {3,4}

print(a.union(b)) #합집합

print(a.intersection(b)) #교집합

print(a-b,a|b,a&b) #차,합,교 집합

b.add(5)             #추가 
print(b)

b.update({6,7})
print(b)

b.update((8,9))
print(b)

b.update([10,11])
print(b)

b.discard(7)        #제거
print(b)

b.remove(8)
print(b)

print('-----------------------------------------')
c = set()
c = b 
print(c)
c.clear()
print(c)

# 다음 리스트이 중복된 값을 제거하려고 한다. 
m = [ 2, 3, 11,29,3,2,7,8,11]

m = set(m)
m = list(m)     #형변환
print(m)
m.sort()        #정렬
print(m)