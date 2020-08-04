m=[]                                                  #행렬만들기 리스트 

m.append([100,200])
m.append([300,400,500,600,700])
m.append([900,1000,1100])

print(m)

# print(m[1][3])

# for i in range(2):
#     print(m[0][i])
# print(m[0][0])
# print(m[0][1])

# 1번째 행을 출력 

# for j in range(5):
#     print(m[1][j])

# print(m[2][0])
# print(m[2][1])
# print(m[2][2])

# for j in range(3):
#     print(m[2][j])

# print('-----------------------------')
# print(len(m[0]))
# print(len(m[1]))
# print(len(m[2]))

# print('-----------------------------')
# for i in range(3):
#     for j in range(len(m[i])):
#         print(m[i][j])

# print('-----------------------------')

# n 리스트 
# 100,50,30,20
# 200,100,1
# 900,1000,20,20,30,40,50
# 50,70,90

#출력 : 이중 for문을 사용해서 출력

n=[]
n.append([100,50,30,20])
n.append([200,100,1])
n.append([900,1000,20,20,30,40,50])
n.append([50,70,90])

for i in range(4):                            
    for j in range(len(n[i])):
        print(n[i][j])
