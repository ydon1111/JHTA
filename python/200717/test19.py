# a = 1 

# while a != 5:
#     print(a)
#     a +=1


# for i in 컬렉션:
#     처리할문장
#     처리할문장

# while 조건:
#     처리할문장
#     처리할문장    
#     조건을 변경할 문장   

# k = 1
# while True:
#     k+=1
#     print("무한반복",k)

# for i in range(5):          #0,1,2,3,4
#     for j in range(3):        #0,1,2
#         print('i : ', i , 'j :', j)
#                                                    # 0,1,2 을 돌려서 위에 for문에 넣음 
print('---------------------------------------')

# i 의 값을 1~9까지 출력 
# for dan in range(2,10):
#     for i in range(1,10):
#          print(str(dan)+" * "+str(i)+"="+str(dan*i))
#     print('--------------------------')


#1
#12
#123
#1234

# print(1)
# print(1,2)
# print(1,2,3)
# print(1,2,3,4)
j=1
for i in range(1,5):
    print()
    for j in range(1,i+1):
            print(j,end='')
      


'''
11111
22222
33333
44444
55555
'''
print('')
for j in range(1,6):
    for i in range(1,6):
        print(j,end="")
    print()

 
# 제어문
# 조건 분기문
# 주어진 조건 발생하면 다른 문장이 실행되게 처리 
'''
if 조건:
    처리할문장
    처리할문장
elif 조건:
    처리할문장2
    처리할문장2
    처리할문장2
else: 
    처리할문장3
    처리할문장3
'''
