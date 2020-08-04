
# # # 튜플 (tuple)
# # list 비슷, 한번 생성되면 값을 변경 할수 없다. 
# # 불변한 순서가 있는 객체의 집합
# a = (10 , 20 , 30 , 40 , 50)
# print(a[0])



# b = tuple(range(5,10))
# print(b)
# print(b[2]) b의 2번째 자리가 뭔지 알려줌 첫째자리는 0부터 시작

# # b[2] = 100 튜플은 값의 수정이 되지 않는다. 

# print(len(b))   b의 갯수

# # 제어문

# # 문장의 흐름을 제어해주는 명령

# # for 변수 in iterable 자료형:
# #     반복할명령 
# print("----------------------------------------")    
# for i in a:
#     print(i)
# print("test ............................")


# # 1부터 20까지 화면에 출력 
# 1. 단순프린트문으로 출력 
# 2. for문을 사용해서 


# print(range(1,21))


# # k= list(range(1,21))

# for i in range(1,21) :
#     print(i)


# 반복문을 사용해서 구구단 3단을 출력 

# print(list(range(3,30,3)))

# for i in range(3,30,3):
#     print("3 * " + str(int(i/3)) ,"=", i)


# c = list(range(1,10))
# for su in c:
#      print("3 * "+ str(su) + "=" + str(3*su))


# 1부터 10까지 누적합을 출력 
# 1. 1부터 10까지 값을 화면에 출력 
# 2. 누적합을 담을 변수를 선언한다.
# 3. 출력하기전에 1씩 증가하는 값을 누적용변수에 누적해서 담는다 
# 4. 누적값을 출력한다.

# sum = 0 
# for i in range(1,11):
#     sum = sum+i 
#     print("sum : " , sum , "i :", i)


# print("------------------------------")

# z = 0 
# for j in range(1,int(input("숫자입력하세요"))+1):
#     z = z+j
#     print (z)

# print("-----------------------------")

# 입력받은 구구단출력 
# 몇단? 

# k = range(1,10)
# m = int(input("단수를 입력하세요"))
# for r in k:
#      print( m ," * ", r ,"=" , int((m*r)) )

     
dan = int(input("단수를 입력하세요"))

value = 0 
for mu in range(1,10):
      value += mu
      print(str(dan) + " * " + str(mu)  ,  "=" , str(dan*mu) , value)


