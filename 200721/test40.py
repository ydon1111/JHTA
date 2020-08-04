
a = [3,0,1,8,7,2,5,4,6,9]
# print(a)
# print(len(a))


# if a[0]>a[1]:
#      a[0],a[1] = a[1],a[0]

# print(a)

print('------------------')


#버블정렬
for j in range(9,0,-1):
    for i in range(j):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        print(a)
    print('-----------------')


