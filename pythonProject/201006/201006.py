grades = [1,3,-2,4]
#리스트 , 배열

#numpy

import numpy as np

print("합계 :",np.sum(grades))
print("평균 :",np.mean(grades))
print("분산 :",np.var(grades))
print("표준편차 :",np.std(grades))

#ndarray 를 지원

ss = ['tom','james','oscar']

print(ss,type(ss))
print('---------------------------------------------------')

a = np.array([1,2,3])
print(a, type(a))
print(a[0],a[2])
print(a.dtype,a.shape,a.ndim)

#들어있는 데이터 , 요소의갯수, 배열의 차수

print("--------------------------------------------------------")

#1반 학생들의 수학 성적

class1 = [90,60,80,50,30,50]
print("합계 :",np.sum(class1))
print("평균 :",np.mean(class1))
print("분산 :",np.var(class1))
print("표준편차 :",np.std(class1))

print("---------------------------------------")

class1 = [90,60,80,50,30,50]
class2 = [80,50,30,20,40,80]
class3 = [50,10,20,30,80,30]

# 각 class의 합계, 평균,분산,표준편차

print(np.sum(class2))
print(np.mean(class2))
print(np.var(class2))
print(np.std(class2))

print("---------------------------------------")


totclass = [[90,60,80,50,30,50],[80,50,30,20,40,80],[50,10,20,30,80,30]]

print(totclass)
print(totclass[0])
print(totclass[0][3])
print(totclass[1][2])
print(totclass[2][4])
print('-------------------------------------------------')

t = np.array(totclass)
print(t)

print(t.dtype,t.shape,t.ndim)
#     int32   (3, 6)      2
#     32bit    행 열      차원

#각 클래스의 수학 평균 성적

print(t.sum(axis=1)) # 0 = x축 , 1 = y축
print(t.mean(axis=1))
print(t.var(axis=1))
print(t.std(axis=1))

print("-------------------------------------------------")

# 시험문제 5번문항의 오류로 모든학생에게 5점씩 추가

print(t + 5)

print("------------------------------------------------")

classA1 = [90,60,80,50,30,50]
classA2 = [80,50,30,20,40,80]
classA3 = [50,10,20,30,80,30]

classB1 = [80,50,30,20,90,80]
classB2 = [80,90,80,70,50,30]
classB3 = [30,50,90,80,90,85]


#3차원 배열

totschool= np.array([[[90,60,80,50,30,50],
                      [80,50,30,20,40,80],
                      [50,10,20,30,80,30]],
                     [[80,50,30,20,90,80],
                      [80,90,80,70,50,30],
                      [30,50,90,80,90,85]]])

#데이터의 타입 , shape , 몇차배열
print(totschool.dtype , totschool.shape,totschool.ndim)

print("-----------------------------------------------------------------")
# x = np.float32(5)
# print(x)






print("----------------------------------------------------------------------")
#10명의 학생들의 키 정보를 가지고 있는 mheight ndarray 객체 생성

mheight = np.array([140.3,150.4,160.5,170.6,180.7,190.8,141.9,151.1,161.2,171.3],dtype=np.float32)

print(mheight,mheight.dtype,mheight.shape)



print("----------------------------------------------------------------------")
#0부터 9까지 요소를 갖는 ndarray 객체 m을 생성
m = np.arange(10,dtype=np.uint8)
print(m)

n1 = np.array([[1,2,3,4]])
n2 = np.array([[5,6,7,8]])
print(n1)
print(n2)
#각 요소를 더하기
print("----------------------------------------------------------------------")

n3 = n1 + n2
n4 = np.add(n1,n2)
print(n3)
print(n4)
print("-----------------------------------------------------------------------")
n3 = n1 - n2
print(n3)
n4 = np.subtract(n1,n2)
print(n4)
print("-----------------------------------------------------------------------")
n3 = n1 * n2
print(n3)
n4 = np.multiply(n1,n2)
print(n4)
print("-----------------------------------------------------------------------")
n3 = n1 / n2
print(n3)
n4 = np.divide(n1,n2)
print(n4)
print("-----------------------------------------------------------------------")

#행렬 곱
#dot()

n1 = np.array([[1,2],
               [3,4]])
n2 = np.array([[5,6],
               [7,8]])

n3 = np.dot(n1,n2)
print(n3)
print("-----------------------------------------------------------------------")

# 5행 5열짜리 배열  n차배열 요소의 값이 0 행렬 k

k = np.array(  [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
             )
print(k,k.shape)

k2 = np.zeros((5,5))
print(k2)

#5행 7열짜리 요소 0인 행렬 k3

k3 = np.zeros((5,7))
print(k3)

k4 = np.ones((3,3))
print(k4)
print("-----------------------------------------------------------------------")

# 단위 행렬
# 대각선 요소는 모두 1 나머지는 모두 0으로 설정되어 있는 정방행렬

m1 = np.eye(3)
print(m1)
print("-----------------------------------------------------------------------")

#모든 요소가 5인 3행 3열짜리 m2
m2 = np.ones((3,3)) * 5
print(m2)
m3 = np.full((3,3),5)
print(m3)
print("-----------------------------------------------------------------------")


totclass = [[90,60,80,50,30,50],
            [80,50,30,20,40,80],
            [50,10,20,30,80,30]]

tot = np.array(totclass)
print(tot)

tot1 = np.zeros_like(tot)
print(tot1)

tot2 = np.ones_like(totclass)
print(tot2)
print("-----------------------------------------------------------------------")
# 0부터 19까지 범위를 갖는 배열 n
n = np.arange(20)
print(n)
print(range(20))

n2 = np.array(range(20))
print(n2)
print("-----------------------------------------------------------------------")

n3 = np.array(range(20))
print(n3,n3.shape)
n4 = n3.reshape((4,5))
print(n4)

# n4의 요소의 값이 10 이상인 것만 출력
tem = []
for i in n4:
    for r in i:
        if r > 10:
            tem.append(r)
print(tem)

idx = n4 > 10
print(idx)
print(n4[idx])

#boolean 타입 배열
m5 = np.array([True,True,False,True],dtype=bool)
print(m5)

m6 = np.array([1,2,3,4])
print(m6,m6.dtype)
# 형변환 : astype 함수를 사용하여 정수형 데이터 배열을 실수형 데이터 배열 변환

m7 = m6.astype(np.float64)
print(m7,m7.dtype)

print("-----------------------------------------------------------------------")

m8 = np.array(["1","2","3","4"])
print(m8,m8.dtype)
m9 = m8.astype(np.int64)
print(m9)

# 0부터 99 사이의 숫자로 이루어져있는 행렬 k1 생성
# k2 : 10행 10열로 변환
# k3 : 정수에서 실수형 데이터로 변환
# k4 : 90 이상의 값만 추출

k1 = np.arange(100)
k2 = k1.reshape(10,10)
print(k2.dtype)
k3 = k2.astype(np.float32)
idx = (k3 >= 90)
k4 = k3[idx]

print(k4)

print("-----------------------------------------------------------------------")
m1 = np.arange(12)
m2 = m1.reshape((3,4))
m3 = np.arange(12).reshape((3,4))
m4 = m3[[1,1,2,2],[1,2,1,2]]
print("m4 : ",m4)
m5 = m3[1:3,1:3]
print(m5)
print("-----------------------------------------------------------------------")
print(m3)


#짝수값만 출력
#요소의 값이 짝수면 True ,홀수면 False
idx = (m3 % 2 ==0)

print(m3[idx])
print(m3^[idx])

print("-----------------------------------------------------------------------")

# 0 부터 90사이값을 요소로 하는 9행 10열짜리 배열 n
# n배열의 요소값이 3의 배수인 값만 뽑으세요
n = np.arange(90).reshape((9,10))
print(n)

print(n[n%3==0])

print("-----------------------------------------------------------------------")

m = np.loadtxt(fname="E:/dev/PycharmProjects/pythonProject/201006/class1.txt",delimiter="\t",skiprows=1)
print(m, m.shape, m.dtype,m.ndim)
n = m[0:4,1:4]
print(n.sum(axis=0))
print(n.mean(axis=0))
print(n.var(axis=0))
print(n.std(axis=0))

print("-----------------------------------------------------------------------")

x = np.arange(1,16).reshape(3,5)
print(x)

y = np.array([[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2]])
print(y)
print(x+y)
print("-----------------------------------------------------------------------")

# 크기가 다른 배열간의 연산 : broadcasting
x = np.array([[10,10,10,10,10],[11,11,11,11,11],[22,22,22,22,22]])
y = np.array([1,1,1,1,1])
print(x+y)

print("-----------------------------------------------------------------------")
x = np.array([10,10,10,10,10])
# 행과 열을 뒤집기
x = x[:,np.newaxis]
print(x,x.shape)
y = np.array([1,1,1,1,1])
print(x+y)

print("-----------------------------------------------------------------------")
# 값이 0인 3행 5열짜리 m배열
# 초기화 되지 않은 값으로 배열을 생성해줍니다
# 초기화 하지 않으므로 쓰레기값이 있을 수 있다
m = np.zeros([3,5])+9
print(m)

print(np.empty((3,5)))
print(np.empty_like(y))
print("-----------------------------------------------------------------------")


#방정식
#2x - y       =0
#-x +2y -u    =0
#    -y+2u -v =0
#       -u+2v =1

m=np.array([[2,-1,0,0],[-1,2,-1,0],
            [0,-1,2,-1],[0,0,-1,2]])
print(m)
n=np.array([0,0,0,1])
#Linear algebra( 식, 값)
print(np.linalg.solve(m,n))
# [0.2 0.4 0.6 0.8]
#   x   y   u   v
print("-----------------------------------------------------------------------")

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
# np.save("이름",배열)
np.save("test",a)
temp =np.load("test.npy")
print(temp)
print("-----------------------------------------------------------------------")
data = np.arange(0,10,2)
print(data)

np.savetxt("test2.txt",data)
temp = np.loadtxt("test2.txt")
print(temp)

# 1부터 100까지 1행 100열 인 행렬 k 를 생성한다.
k = np.arange(1,101)
# print(k)

# 10행 10열로 모양을 변경 한다.
k1 = k.reshape(10,10)
# print(k1)

# 각 행이 관측치 라고 가정하고 행별 합계, 평균을 구한다.
k1_sum = k1.sum(axis=1)
k1_mean = k1.mean(axis=1)
k1_mean = k1_mean.astype(np.int32)
# print(k1_sum,k1_sum.dtype)
# print(k1_mean,k1_mean.dtype)

# k4 = np.append(k1,k1_sum)
# print(k4)
print('----------------------------------------')

a = np.array([[10,20,30],[40,50,60]])
print(a.shape)

b= np.array([70,80,90]).reshape(1,3)
print(b.shape)

print(np.concatenate((a,b),axis=0))


print('----------------------------------------')
k3 = np.column_stack([k1,k1_sum])
k3 = np.column_stack([k3,k1_mean])
print(k3)

# 이 값(합계,평균)을 k 행렬에 추가한다.
#  k.data 라는 파일로 k 행렬을 저장한다.
np.save("kdata",k3)

# k.data 파일을 읽어 m 행렬로 읽어온다.
m =np.load("kdata.npy")
print(m)

# m 행렬의 shape, dtype , ndim 은 얼마인가?
print(m.shape,m.dtype,m.ndim)
# 12행 12열  짜리 단위 행렬  n 을 생성 (대각선값은 1 나머지는 0 )
n = np.eye(12)
n = n.astype(np.int32)
print(n)

# m 행렬에 2행을 추가 (임의의값) 12행 12열
u = np.arange(1,13)
u1 = np.arange(1,13)
m = np.vstack([m,u])
m = np.vstack([m,u1])

print(m)
# m+n 결과 result 행렬 ?

result = m+n
print(result)

#result 행렬을 result.txt 파일로 저장

np.savetxt("result.txt",result)

# result.txt 파일에서 읽어서 tmp 변수에 담는다.

tmp = np.loadtxt("result.txt")

# tmp 행렬에서 요소의 값이 50 이상인 값만 슬라이싱 하고 tmp2 에 담는다.

idx = tmp > 50
print(idx)
tmp2 = tmp[idx]
print(tmp2.shape)
tmp2 = tmp2.reshape(5,13)
print(tmp2.shape)
# tmp2 행렬을 전치 행렬로 만든다 (행과 열의 뒤집음 )
tmp2 = tmp2.T
print(tmp2.shape)
# tmp2 행렬을 final.npy 로 저장한다.

np.save("final.npy",tmp2)