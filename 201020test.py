# for i in range (1,10):
#     print(5 , "*" , i , "=", 5*i )

# x ,y ,z = input (' 국 영 수 점수 입력 : ').split()

# x = int(x)
# y = int(y)
# z = int(y)

# totsum = x + y + z 
# totavg = totsum/3

# print(totsum, totavg)


# i = [4,9,2,6,1,3,8,0,7,5]


# temp = 0 


# x = int(input ('숫자입력 : '))


# if x%2 ==0:
#     print( x ,'는 짝수입니다.')
# else :
#     print( x ,'는 홀수입니다.')


# class Human:
#     def __init__(self,name,age,job):
#         self.name = name
#         self.age = age
#         self.job = job
#     def status(self):
#         print(self.age,'살',self.name,'는',self.job,"입니다.")

# p = Human('펭수',20,'직장인')

# p.status()


t = [4,9,2,6,5151,1,3,8,0,7,5,123,4234]

# print(len(t))
# if i[0] > i[1]:
#     i[0],i[1] = i[1],i[0]
# elif i[0] > i [2]:
#     i[0],i[2] = i[2],i[0]
# elif i[0] > i [3]:
#     i[0],i[3] = i[3],i[0]
# elif i[0] > i [4]:
#     i[0],i[4] = i[4],i[0]
# elif i[0] > i [5]:
#     i[0],i[5] = i[5],i[0]
# elif i[0] > i [6]:
#     i[0],i[6] = i[6],i[0]
# elif i[0] > i [7]:
#     i[0],i[7] = i[7],i[0]  



for i in range(len(t)):
    for r in range(len(t)):
        if t[i] < t[r]:
            t[i],t[r] = t[r],t[i]


print(t)

