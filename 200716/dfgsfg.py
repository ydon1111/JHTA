k = list(range(10,20,2))  
print(k)

print(list(range(100,0,-1)))

print(list(range(3,1000,3)))


b = tuple(range(5,10))
print(b) 

print(b[2])
print(len(b))


for i in range(2,10):
    for j in range(1,10):
        print(i*j , end="---")
        print('')