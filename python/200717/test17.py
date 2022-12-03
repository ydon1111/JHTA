#리스트
#순서 0 중복 0 변경 0


a = [1,2,3]
print(a, type(a))

b = [10,a,True,'문자열']

print(b[1])
print(b[1][2])


c = [[1,2],[3,4,5],[6,7,8,9]]
print(c)
print(c[1][1]) #리스트안에 있는 리스트에서 찾기
print(c[2][2])

print("--------------------------------------------------")

# 동물

pet = ['강아지','고양이','거북이','고슴도치']
print(pet)
pet.append('열대어') #리스트에 추가 
print(pet)
pet.remove('거북이') #리스트에서 제거 
print(pet)
pet.insert(0,'이구아나') #위치를 설저앻서 추가
print(pet)
pet.extend(['토끼','햄스터'])
print(pet)
pet += ['돼지']
print(pet)

print(len(pet))
del pet[3]
print(pet)
# pet.remove('고슴도치')
# print(pet)

animal = pet

print('animal :' , animal)
print('pet :' , pet)

pet[0] = '멍멍이'
print('----------------------------------')
print('animal :' , animal)
print('pet :' , pet)

print(id(animal),id(pet)) #같은 대상을 참조 
