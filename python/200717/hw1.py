# #1
# for i in range(1,101):
#     print(i)

#2
# print('')
# for i in range(1,6):
#     for j in range(1,7):
#         print(i,end='')
#     print()

# #3
# print('')
# for i in range(9,4,-1):
#     for j in range(1,6):
#         print(i,end="")
#     print()

#4 아직 못품 모름 배낌


# for i in range(1,3):
#     for j in range(1,5):
#         if i < 2: print(j, end = "")
#         else: print(j+4, end ="")
#     print()



#5
# k = 8
# for i in range(1,10):
#     print("8 *",i,"=",k*i)

# #6
# for dan in range(2,10):
#     print('---------------')   
#     for i in range(1,10):
#         print(str(dan)+" * "+str(i)+"="+str(dan*i))
  
# #7
# k = 3
# for i in range(1,10):
#     print(k, "*",i,"=",k*i,end='  ')

# #8
# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#             print(1,end='')


#9 
# for i in range(1,101):
#     print(i)


# #10
# sum = 0 
# for i in range(1,101):
#      sum = sum+i 
# print(sum)


# #11
# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#             print('*',end='')

# for i in range(1,6):
#     print("*"*i)

# #12
# j=1
# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#             print(j,end='')

# msg ='' 
# for i in range(1,6):
#     msg = msg+str(i)
#     print(msg)

    
# #13 
# for j in range(2,10):
#     for i in range(1,10):
#         print(j, "*",i,"=",j*i,end='  ')

# #14
# for i in range(1,6):
#      print()
#      for j in range(7,i+1,-1):
#          print('*',end='')

# #15

# t = int(input('time converter :'))
# day=t//86400
# hour=(t%86400//3600)  #60*60*24
# mine=(t%(3600)//60)   #60*60
# sec=(t%60)

# print(day,hour,mine,sec)


#16

# m = int(input("잔돈 교환기 :"))

# a = m//50000
# b = m%50000//10000
# c = m%10000//5000
# d = m%5000//1000
# e = m%1000//500
# f = m%500//100
# g = m%100//50
# h = m%50//10
# i = m%10//1
# print(a, b ,c ,d ,e ,f, g, h, i )

